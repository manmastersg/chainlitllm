# PageIndex Integration — Implementation Plan

> **Approach B: Full Agentic Retrieval using OpenAI Agents SDK**

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Integrate [PageIndex](https://github.com/VectifyAI/PageIndex) as a vectorless, reasoning-based RAG layer into the Chainlitsec app. Admins upload PDFs via the admin panel → documents are indexed into a PageIndex tree. **Every chat message automatically queries all indexed documents** and injects the most relevant context into the LLM prompt. No manual `/doc` activation needed.

**Retrieval mechanism (verified from source):**

- `PageIndexClient.index(path)` → returns UUID doc_id, builds tree index, persists to workspace JSON
- `PageIndexClient` has **no retrieve() method** — retrieval uses the OpenAI Agents SDK agent loop
- Agent: `get_document()` → `get_document_structure()` → `get_page_content("5-7")` → answer
- Non-OpenAI models routed via `litellm/` prefix: `"litellm/anthropic/claude-sonnet-4-6"`

**Architecture:**

```
Admin uploads PDF → saved to disk → PageIndexClient.index_document() → tree index stored
                                    ↓
User sends ANY message → system queries ALL "ready" docs in parallel via PageIndexClient.retrieve()
                         → top-N relevant context snippets collected
                         → context prepended to user message
                         → LLM answers with document grounding
                         → response streamed back
```

- **No `/doc` command** — document retrieval is always-on when documents are available
- **Fallback** — if no docs are indexed, or if retrieval returns no relevant context, the LLM answers from its own knowledge (existing chat behavior)
- **Automatic deduplication** — if docs are deleted, their context is simply no longer injected

**Tech Stack:** Python backend (existing `auth_test.py`), PageIndex library (`pageindex` + `litellm`), React frontend (existing), local file storage.

---

## Phase 0: Inventory — ✅ COMPLETED

> ⚠️ Read all files listed below before any implementation begins.

✅ All Phase 0 files verified present (summary from context):

- `backend/auth_test.py`, `backend/llm_settings.json`, `backend/chainlit/server.py:813-890`
- `backend/chainlit/__init__.py`, `backend/pyproject.toml`
- `frontend/src/pages/AdminDocuments.tsx`, `frontend/src/components/chat/MessageComposer/index.tsx`
- `frontend/src/components/chat/MessageComposer/UploadButton.tsx`, `frontend/src/hooks/useUpload.tsx`, `frontend/src/router.tsx`

### Key findings from Phase 0:

- `pyproject.toml` — 59 existing deps, no PageIndex packages
- No `backend/.gitignore` — root `.gitignore` at repo root
- No `data/` directory existed before this phase

---

## Phase 1: Infrastructure & Dependencies — ✅ COMPLETED

### Task 1: Add PageIndex + OpenAI Agents dependencies to pyproject.toml — ✅ DONE

- Commit: `a9a2b9a5` — "chore: add pageindex, litellm, openai-agents deps + storage dirs"
- Added: `pageindex>=1.0.0`, `litellm>=1.83.0`, `openai-agents>=1.0.0`, `pypdf>=5.0.0`, `pyyaml>=6.0.0`

### Task 2: Create storage directory for uploaded PDFs — ✅ DONE

- Created: `backend/data/pageindex_documents/workspace/`
- Updated: `.gitignore` → added `backend/data/pageindex_documents/`
- Commit: `a9a2b9a5`

**Next step:** Run `cd backend && uv sync` to install new deps before Phase 2.

---

## Phase 2: Backend — PageIndex Service Layer

### Task 3: Create pageindex_service.py — the core service class

**Objective:** Build a `PageIndexService` singleton that:

1. Stores PDFs to disk and indexes them via `PageIndexClient`
2. Uses the **OpenAI Agents SDK** for agentic retrieval — the agent reasons over the document tree and calls tools (`get_document`, `get_document_structure`, `get_page_content`) to answer queries
3. **CRITICAL:** Routes to YOUR configured LLM provider (opencode/minimax) — not OpenAI's default API
4. Manages document metadata across restarts

> **Critical API notes** (verified against source):
>
> - `client.index(file_path)` → returns a **UUID string** as doc_id (not the path)
> - `client.documents[doc_id]` holds the full document dict after indexing
> - `client.get_document(doc_id)` → returns JSON metadata string
> - `client.get_document_structure(doc_id)` → returns JSON tree string
> - `client.get_page_content(doc_id, "5-7")` → returns JSON list of pages
> - There is **no `retrieve()` method** — retrieval is the agentic tool-calling loop
> - `client.retrieve_model` is **read-only** after construction; set via constructor: `PageIndexClient(retrieve_model="...")`
> - PageIndex uses `litellm/` prefix to route non-OpenAI models: e.g. `"litellm/anthropic/claude-sonnet-4-6"`

> **CRITICAL: LLM Routing Fix** (your provider is NOT OpenAI)
> Your current LLM config in `llm_settings.json`:
>
> - Provider: `opencode`
> - Model: `minimax-m2.5-free`
> - Base URL: `https://opencode.ai/zen/v1`
>
> The Agents SDK by default sends to `api.openai.com` — we must pass a custom `AsyncOpenAI` client with your provider's base_url. The code below handles this correctly.

**Files:**

- Create: `backend/pageindex_service.py`
- Read first: PageIndex source at `https://github.com/VectifyAI/PageIndex/blob/main/pageindex/client.py` and `examples/agentic_vectorless_rag_demo.py`

**Step 1: Write the service**

```python
"""
PageIndex Service — wraps PageIndexClient for the Chainlitsec app.
Manages document indexing, storage, and agentic multi-document retrieval.

Retrieval flow (agentic):
  1. For each indexed doc, spawn an OpenAI Agents SDK agent with tool access
  2. Each agent calls: get_document → get_document_structure → get_page_content
  3. The agent reasons over the tree to find relevant pages, then fetches content
  4. Collect all agent answers as context for the main LLM
"""
import json
import os
import uuid
import asyncio
import concurrent.futures
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

DOCUMENTS_DIR = Path(__file__).parent / "data" / "pageindex_documents"
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
METADATA_FILE = DOCUMENTS_DIR / "documents.json"

# Token budget for combined agent responses
MAX_RETRIEVAL_CHARS = 24_000  # ~6K tokens at 4 chars/token


@dataclass
class DocumentMeta:
    doc_id: str
    filename: str
    original_path: str
    status: str  # "indexing", "ready", "error"
    page_count: int = 0
    error_message: str = ""
    created_at: str = ""
    indexed_at: str = ""


@dataclass
class AgentRetrievalResult:
    doc_id: str
    filename: str
    agent_answer: str
    pages_used: list[int]


def _load_metadata() -> dict[str, DocumentMeta]:
    if not METADATA_FILE.exists():
        return {}
    with open(METADATA_FILE) as f:
        data = json.load(f)
    return {k: DocumentMeta(**v) for k, v in data.items()}


def _save_metadata(meta: dict[str, DocumentMeta]):
    with open(METADATA_FILE, "w") as f:
        json.dump({k: v.__dict__ for k, v in meta.items()}, f, indent=2)


@dataclass
class AgentRetrievalResult:
    doc_id: str
    filename: str
    agent_answer: str
    pages_used: list[int]


class PageIndexService:
    """
    Singleton service for PageIndex document management.

    Responsibilities:
    - Store PDF files to disk
    - Index PDFs via PageIndexClient.index() — returns UUID doc_id
    - Run agentic retrieval across all indexed docs using OpenAI Agents SDK
    - Use YOUR configured LLM from llm_settings.json (not OpenAI default)
    - Persist document metadata across restarts
    """

    _instance: Optional["PageIndexService"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._clients: dict[str, "PageIndexClient"] = {}
            cls._instance._metadata: dict[str, DocumentMeta] = _load_metadata()
            cls._instance._workspace_dir = DOCUMENTS_DIR / "workspace"
            cls._instance._workspace_dir.mkdir(parents=True, exist_ok=True)
        return cls._instance

    def _get_client(self) -> "PageIndexClient":
        """Return a shared PageIndexClient configured with the workspace."""
        from pageindex import PageIndexClient
        return PageIndexClient(workspace=str(self._workspace_dir))

    def _load_or_build_client(self) -> "PageIndexClient":
        """Load client — it will restore all previously indexed docs from workspace."""
        return self._get_client()

    async def index_document(self, file_content: bytes, filename: str) -> DocumentMeta:
        """
        Save a PDF to disk and index it via PageIndexClient.
        Returns DocumentMeta with status='ready' or 'error'.

        Flow:
          1. Save bytes to DOCUMENTS_DIR
          2. Create a PageIndexClient with workspace
          3. Call client.index(abs_path) → returns UUID doc_id
          4. Extract page_count from client.documents[doc_id]
          5. Persist metadata to documents.json
        """
        from datetime import datetime
        from pageindex import PageIndexClient

        doc_id = str(uuid.uuid4())
        safe_name = f"{doc_id}_{Path(filename).name}"
        file_path = DOCUMENTS_DIR / safe_name

        with open(file_path, "wb") as f:
            f.write(file_content)

        meta = DocumentMeta(
            doc_id=doc_id,
            filename=filename,
            original_path=str(file_path),
            status="indexing",
            created_at=datetime.utcnow().isoformat(),
        )
        self._metadata[doc_id] = meta
        _save_metadata(self._metadata)

        try:
            # PageIndexClient with workspace persists doc JSON to disk
            client = PageIndexClient(workspace=str(self._workspace_dir))
            returned_doc_id = client.index(str(file_path.resolve()))

            # Extract page count from the in-memory document dict
            doc_info = client.documents.get(returned_doc_id, {})
            meta.page_count = doc_info.get("page_count", 0)
            meta.status = "ready"
            meta.indexed_at = datetime.utcnow().isoformat()
            self._metadata[returned_doc_id] = meta
            _save_metadata(self._metadata)

            logger.info(f"Indexed document {doc_id} ({filename}): {meta.page_count} pages")

        except Exception as e:
            meta.status = "error"
            meta.error_message = str(e)
            meta.indexed_at = datetime.utcnow().isoformat()
            logger.error(f"Failed to index document {doc_id}: {e}")
            _save_metadata(self._metadata)

        return meta

    def get_document(self, doc_id: str) -> Optional[DocumentMeta]:
        return self._metadata.get(doc_id)

    def get_ready_documents(self) -> list[DocumentMeta]:
        return [m for m in self._metadata.values() if m.status == "ready"]

    def get_doc_info_json(self, doc_id: str) -> Optional[str]:
        """Return JSON string from PageIndexClient.get_document(doc_id)."""
        client = self._load_or_build_client()
        return client.get_document(doc_id)

    def get_doc_structure_json(self, doc_id: str) -> Optional[str]:
        """Return tree structure JSON from PageIndexClient."""
        client = self._load_or_build_client()
        return client.get_document_structure(doc_id)

    def get_page_content_json(self, doc_id: str, pages: str) -> Optional[str]:
        """Return page content JSON from PageIndexClient."""
        client = self._load_or_build_client()
        return client.get_page_content(doc_id, pages)

    def list_documents(self) -> list[DocumentMeta]:
        return list(self._metadata.values())

    def delete_document(self, doc_id: str):
        """Delete from metadata. The workspace JSON file is cleaned up separately."""
        meta = self._metadata.pop(doc_id, None)
        if meta:
            path = Path(meta.original_path)
            if path.exists():
                path.unlink()
        # Remove workspace JSON if it exists
        workspace_file = self._workspace_dir / f"{doc_id}.json"
        if workspace_file.exists():
            workspace_file.unlink()
        _save_metadata(self._metadata)

    # ── Agentic Retrieval ────────────────────────────────────────────────────────

    def _load_llm_config(self) -> dict:
        """
        Load LLM config from llm_settings.json.
        This ensures PageIndex uses the SAME provider as your chat app.
        """
        import json
        config_path = Path(__file__).parent / "llm_settings.json"
        if not config_path.exists():
            # Fallback to environment or default
            return {
                "model": os.environ.get("OPENAI_MODEL_NAME", "gpt-4o"),
                "base_url": os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
                "api_key": os.environ.get("OPENAI_API_KEY", ""),
            }
        with open(config_path) as f:
            config = json.load(f)
        active_provider = next(
            (p for p in config["providers"] if p.get("is_active")),
            config["providers"][0]
        )
        return active_provider

    def _get_openai_client(self) -> "AsyncOpenAI":
        """Get an AsyncOpenAI client configured with your provider (opencode/minimax)."""
        from openai import AsyncOpenAI

        config = self._load_llm_config()
        return AsyncOpenAI(
            base_url=config.get("base_url", "https://api.openai.com/v1"),
            api_key=config.get("api_key", ""),
            timeout=60.0,
            max_retries=2,
        )

    def _run_agent_for_doc(
        self, doc_id: str, doc_name: str, query: str, model: str
    ) -> AgentRetrievalResult:
        """
        Run a single OpenAI Agents SDK agent for one document.
        The agent uses get_document, get_document_structure, get_page_content tools
        to answer the query, then returns a plain-text answer.

        CRITICAL: Uses your configured LLM provider via custom AsyncOpenAI client.
        """
        from agents import Agent, Runner, function_tool
        from agents.models import OpenAIChatCompletionsModel

        client = self._load_or_build_client()

        # Get the AsyncOpenAI client configured with YOUR provider (opencode/minimax)
        openai_client = self._get_openai_client()
        llm_config = self._load_llm_config()

        system_prompt = (
            f"You are a document QA assistant for '{doc_name}'.\n"
            "TOOL USE:\n"
            "1. Call get_document() first to confirm status and page/line count.\n"
            "2. Call get_document_structure() to understand the document layout.\n"
            "3. Call get_page_content(pages='N-M') with tight ranges to fetch specific pages.\n"
            "4. Answer based ONLY on the tool output. Be concise and accurate.\n"
            "If the answer is not in the document, say so clearly.\n"
        )

        @function_tool
        def get_document() -> str:
            """Get document metadata: status, page count, name, description."""
            return client.get_document(doc_id)

        @function_tool
        def get_document_structure() -> str:
            """Get the document's tree structure to identify relevant sections."""
            return client.get_document_structure(doc_id)

        @function_tool
        def get_page_content(pages: str) -> str:
            """
            Get text content of specific pages.
            Use tight ranges: '5-7' for pages 5-7, '3,8' for pages 3 and 8, '12' for page 12.
            """
            return client.get_page_content(doc_id, pages)

        # CRITICAL: Use OpenAIChatCompletionsModel with your custom client
        # This routes to YOUR provider (opencode/minimax), NOT OpenAI's default API
        model_to_use = llm_config.get("model", model or "gpt-4o")

        chat_model = OpenAIChatCompletionsModel(
            model=model_to_use,
            openai_client=openai_client,
        )

        agent = Agent(
            name="PageIndex",
            instructions=system_prompt,
            tools=[get_document, get_document_structure, get_page_content],
            model=chat_model,
        )

        # Run synchronously in a thread to avoid blocking the event loop
        result = Runner.run_sync(agent, query)
        answer = result.final_output if result.final_output else ""

        # Try to extract which pages were used from tool calls
        pages_used = []
        for item in result.items:
            if hasattr(item, "type") and item.type == "tool_call_item":
                args = getattr(item, "raw_item", None)
                if args and hasattr(args, "name") and args.name == "get_page_content":
                    try:
                        parsed = json.loads(args.arguments) if isinstance(args.arguments, str) else args.arguments
                        pages_arg = parsed.get("pages", "")
                        if pages_arg:
                            pages_used.extend(self._parse_page_ranges(pages_arg))
                    except Exception:
                        pass

        return AgentRetrievalResult(
            doc_id=doc_id,
            filename=doc_name,
            agent_answer=answer.strip(),
            pages_used=list(set(pages_used)),
        )

    def _parse_page_ranges(self, pages_str: str) -> list[int]:
        """Parse '5-7' or '3,8' into a list of page numbers."""
        result = []
        for part in pages_str.split(","):
            part = part.strip()
            if "-" in part:
                start, end = part.split("-", 1)
                result.extend(range(int(start.strip()), int(end.strip()) + 1))
            else:
                result.append(int(part))
        return sorted(set(result))

    def _run_agent_thread(
        self, doc_id: str, doc_name: str, query: str, model: str
    ) -> AgentRetrievalResult:
        """Thread-entry wrapper for async agent run."""
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                self._run_agent_for_doc_async(doc_id, doc_name, query, model)
            )
            loop.close()
            return result
        except Exception as e:
            logger.warning(f"Agent failed for doc {doc_id}: {e}")
            return AgentRetrievalResult(doc_id=doc_id, filename=doc_name, agent_answer="", pages_used=[])

    async def _run_agent_for_doc_async(
        self, doc_id: str, doc_name: str, query: str, model: str
    ) -> AgentRetrievalResult:
        """Async wrapper — runs the sync agent in a thread pool."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, self._run_agent_thread, doc_id, doc_name, query, model
        )

    async def retrieve_all(
        self, query: str, model: Optional[str] = None, max_docs: int = 5
    ) -> list[AgentRetrievalResult]:
        """
        Run agentic retrieval across ALL ready documents in parallel.

        1. Collect ready documents (up to max_docs)
        2. Use the configured LLM from llm_settings.json (no normalization needed)
        3. Run one agent per document in ThreadPoolExecutor
        4. Collect non-empty answers
        5. Sort by answer length (longer = more relevant content found)
        """
        ready_docs = self.get_ready_documents()
        if not ready_docs:
            return []

        docs_to_query = ready_docs[:max_docs]

        results: list[AgentRetrievalResult] = []
        lock = asyncio.Lock()

        async def _run_one(meta: DocumentMeta) -> Optional[AgentRetrievalResult]:
            result = await self._run_agent_for_doc_async(
                doc_id=meta.doc_id,
                doc_name=meta.filename,
                query=query,
                model=None,  # Uses llm_settings.json config internally
            )
            if result.agent_answer:
                return result
            return None

        # Run all agents concurrently with a semaphore to cap concurrency
        semaphore = asyncio.Semaphore(min(len(docs_to_query), 4))

        async def _run_bounded(meta: DocumentMeta) -> Optional[AgentRetrievalResult]:
            async with semaphore:
                return await _run_one(meta)

        tasks = [_run_bounded(meta) for meta in docs_to_query]
        completed = await asyncio.gather(*tasks, return_exceptions=True)

        for item in completed:
            if isinstance(item, AgentRetrievalResult) and item.agent_answer:
                results.append(item)
            elif isinstance(item, Exception):
                logger.warning(f"Agent task exception: {item}")

        # Sort by answer length — longer answer = more relevant content found
        results.sort(key=lambda r: len(r.agent_answer), reverse=True)
        return results

    def build_rag_context(
        self, query: str, model: Optional[str] = None, max_docs: int = 5
    ) -> tuple[str, list[AgentRetrievalResult]]:
        """
        Build combined RAG context by running agentic retrieval on all indexed docs.

        Returns (context_string, results).
        context_string is empty if no docs are ready or all agents return empty.
        """
        # Run async retrieval synchronously (called from sync context in Chainlit)
        try:
            loop = asyncio.get_running_loop()
            # If already in async context, use the async method
            results = loop.run_until_complete(
                self.retrieve_all(query, model, max_docs)
            )
        except RuntimeError:
            # No running loop — create one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results = loop.run_until_complete(
                self.retrieve_all(query, model, max_docs)
            )
            loop.close()

        if not results:
            return "", []

        # Build context string with doc labels and answers
        lines = [
            "=== KNOWLEDGE BASE CONTEXT ===",
            f"(Retrieved from {len(results)} document(s) using agentic reasoning)\n",
        ]

        total_chars = 0
        for result in results:
            header = f"--- Document: {result.filename} ---"
            if total_chars + len(header) + len(result.agent_answer) + 10 < MAX_RETRIEVAL_CHARS:
                lines.append(header)
                lines.append(result.agent_answer)
                lines.append("")
                total_chars += len(header) + len(result.agent_answer)

        return "\n".join(lines), results
```

**Step 2: Commit**

```bash
git add backend/pageindex_service.py
git commit -m "feat: add PageIndexService with automatic multi-document retrieval"
```

---

### Task 4: Add API endpoints for PageIndex document management

**Objective:** Add FastAPI endpoints for uploading, listing, retrieving, and deleting documents. Follow the same pattern as the existing `llm-settings` endpoints.

**Files:**

- Modify: `backend/chainlit/server.py` (around line 890, after llm-settings endpoints)
- Read first: `backend/chainlit/server.py:813-890` for the endpoint pattern

**Step 1: Read the endpoint pattern first**

```bash
# Key pattern from the inventory phase:
# @app.get("/project/llm-settings")
# @router.get("/project/llm-settings")
# async def get_llm_settings(current_user: UserParam): ...
#
# Admin guard: if current_user.metadata.get("role") != "admin": raise HTTPException(403)
# UserParam is imported from chainlit module
```

**Step 2: Add the endpoints after the llm-settings section**

```python
# === PageIndex Document Management ===

@app.get("/project/pageindex/documents")
@router.get("/project/pageindex/documents")
async def list_documents(current_user: UserParam):
    """List all indexed PageIndex documents."""
    from pageindex_service import PageIndexService
    service = PageIndexService()
    docs = service.list_documents()
    return JSONResponse(content=[d.__dict__ for d in docs])


@app.get("/project/pageindex/documents/status")
@router.get("/project/pageindex/documents/status")
async def get_docs_status(current_user: UserParam):
    """Return a summary: count of ready docs and total doc count."""
    from pageindex_service import PageIndexService
    service = PageIndexService()
    docs = service.list_documents()
    ready = [d for d in docs if d.status == "ready"]
    return JSONResponse(content={
        "total": len(docs),
        "ready": len(ready),
        "ready_doc_ids": [d.doc_id for d in ready],
    })


@app.post("/project/pageindex/documents")
@router.post("/project/pageindex/documents")
async def upload_document(
    current_user: UserParam,
    file: UploadFile = File(...),
):
    """Upload and index a PDF document."""
    if current_user.metadata.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files supported")

    content = await file.read()
    if len(content) > 50 * 1024 * 1024:  # 50MB limit
        raise HTTPException(status_code=400, detail="File too large (max 50MB)")

    from pageindex_service import PageIndexService
    service = PageIndexService()
    meta = await service.index_document(content, file.filename)
    return JSONResponse(content=meta.__dict__, status_code=201)


@app.get("/project/pageindex/documents/{doc_id}")
@router.get("/project/pageindex/documents/{doc_id}")
async def get_document(current_user: UserParam, doc_id: str):
    """Get document metadata."""
    from pageindex_service import PageIndexService
    service = PageIndexService()
    meta = service.get_document(doc_id)
    if not meta:
        raise HTTPException(status_code=404, detail="Document not found")
    return JSONResponse(content=meta.__dict__)


@app.get("/project/pageindex/documents/{doc_id}/structure")
@router.get("/project/pageindex/documents/{doc_id}/structure")
async def get_document_structure(current_user: UserParam, doc_id: str):
    """Get the tree index structure of a document."""
    from pageindex_service import PageIndexService
    service = PageIndexService()
    structure = service.get_document_structure(doc_id)
    if structure is None:
        raise HTTPException(status_code=404, detail="Document not found or not ready")
    return JSONResponse(content={"doc_id": doc_id, "structure": structure})


@app.get("/project/pageindex/documents/{doc_id}/content")
@router.get("/project/pageindex/documents/{doc_id}/content")
async def get_page_content(
    current_user: UserParam,
    doc_id: str,
    pages: str = Query(..., description="e.g. '5-7' or '3,8'"),
):
    """Get text content of specific pages."""
    from pageindex_service import PageIndexService
    service = PageIndexService()
    content = service.get_page_content(doc_id, pages)
    if content is None:
        raise HTTPException(status_code=404, detail="Document not found or not ready")
    return JSONResponse(content={"doc_id": doc_id, "pages": pages, "content": content})


@app.delete("/project/pageindex/documents/{doc_id}")
@router.delete("/project/pageindex/documents/{doc_id}")
async def delete_document(current_user: UserParam, doc_id: str):
    """Delete a document and its index."""
    if current_user.metadata.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    from pageindex_service import PageIndexService
    service = PageIndexService()
    service.delete_document(doc_id)
    return JSONResponse(content={"deleted": doc_id})
```

**Step 3: Commit**

```bash
git add backend/chainlit/server.py
git commit -m "feat: add PageIndex REST API endpoints for document management"
```

---

### Task 5: Wire automatic document retrieval into auth_test.py chat handler

**Objective:** Replace the message handler so **every user message** automatically queries all indexed documents. No manual activation needed.

**Key logic:**

1. On every message, call `pageindex_service.build_rag_context(user_message)`
2. If context is returned → prepend it to the system prompt → LLM answers with document grounding
3. If no docs are ready → fall through to existing regular chat behavior
4. Show a subtle "Searching N documents..." status while retrieving

**Files:**

- Modify: `backend/auth_test.py`
- Read first: `backend/auth_test.py` (already done in inventory)

**Step 1: Write the updated auth_test.py**

````python
import chainlit as cl
from openai import AsyncOpenAI
import traceback
import time
import json
import os

# Load LLM Configuration from llm_settings.json
def load_llm_config():
    config_path = os.path.join(os.path.dirname(__file__), "llm_settings.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    active_provider = next((p for p in config["providers"] if p.get("is_active")), config["providers"][0])
    return active_provider

llm_config = load_llm_config()

client = AsyncOpenAI(
    base_url=llm_config["base_url"],
    api_key=llm_config["api_key"]
)

MODEL_NAME = llm_config["model"]

# === PageIndex Service ===
from pageindex_service import PageIndexService
pageindex_service = PageIndexService()

# === Existing auth (keep as-is) ===
users = {
    "admin": {"password": "***", "role": "admin", "name": "Administrator"},
    "user":  {"password": "***", "role": "user",  "name": "Standard User"},
}

@cl.password_auth_callback
async def auth_callback(username: str, password: str):
    if username in users and users[username]["password"] == password:
        user_data = users[username]
        return cl.User(
            identifier=username,
            display_name=user_data["name"],
            metadata={"role": user_data["role"]},
        )
    return None

# === System prompt builder ===
BASE_SYSTEM_PROMPT = "You are a helpful assistant. Provide direct, accurate answers."

def build_system_prompt(rag_context: str = "") -> str:
    """Build the system prompt. If rag_context is provided, include it."""
    if rag_context:
        return (
            f"You are a helpful assistant with access to a knowledge base of documents.\n"
            f"Use the provided KNLEDGE BASE CONTEXT to answer questions accurately and specifically.\n"
            f"If the answer is not in the context, say so clearly — do not hallucinate.\n\n"
            f"{rag_context}"
        )
    return BASE_SYSTEM_PROMPT


@cl.on_chat_start
async def start():
    if cl.user_session.get("history") is None:
        user = cl.user_session.get("user")
        role = user.metadata.get("role", "unknown")
        cl.user_session.set("history", [{"role": "system", "content": BASE_SYSTEM_PROMPT}])

        await cl.Message(
            content=f"Welcome {user.display_name}! Role: **{role}**."
        ).send()


@cl.on_message
async def main(message: cl.Message):
    user_query = message.content.strip()
    if not user_query:
        return

    # === AUTOMATIC DOCUMENT RETRIEVAL (always-on) ===
    ready_docs = pageindex_service.get_ready_documents()
    rag_context = ""
    retrieval_results: list = []

    if ready_docs:
        # Show "searching" status
        status_msg = cl.Message(
            content=f"*🔍 Searching {len(ready_docs)} document(s)...*",
            author="System"
        )
        await status_msg.send()

        try:
            rag_context, retrieval_results = pageindex_service.build_rag_context(
                query=user_query,
                model=MODEL_NAME,
            )
        except Exception as e:
            logger.warning(f"RAG retrieval failed: {e}")
            rag_context = ""

        await status_msg.remove()

        # Log what was retrieved
        if retrieval_results:
            doc_names = [r.filename for r in retrieval_results]
            print(f"[RAG] Query: '{user_query}' → matched docs: {doc_names}")
        else:
            print(f"[RAG] Query: '{user_query}' → no relevant docs found")

    # === Build messages with RAG context ===
    history = cl.user_session.get("history")
    system_content = build_system_prompt(rag_context)

    # Build the messages list: system (with context if available) + last N history
    messages = [{"role": "system", "content": system_content}]

    # Preserve conversation history (skip the base system prompt from history,
    # since we're building our own)
    if len(history) > 1:
        messages.extend(history[1:])  # skip index 0 (old base system prompt)

    messages.append({"role": "user", "content": user_query})

    # Sliding window: keep last 10 user+assistant turns
    if len(messages) > 11:
        messages = [messages[0]] + messages[-10:]

    cl.user_session.set("history", messages)

    # === Call LLM ===
    start_time = time.perf_counter()

    think_msg = cl.Message(content="*Thinking...*", author="System")
    await think_msg.send()

    try:
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream=False,
            extra_body={
                "enable_thinking": llm_config.get("enable_thinking", False)
            }
        )
        duration = time.perf_counter() - start_time

        content = response.choices[0].message.content
        await think_msg.remove()

        if content:
            messages.append({"role": "assistant", "content": content})
            cl.user_session.set("history", messages)

            usage = response.usage
            completion_tokens = usage.completion_tokens if usage else 0
            tokens_per_sec = completion_tokens / duration if duration > 0 else 0

            # Build metrics string
            meta_parts = []
            if retrieval_results:
                meta_parts.append(f"📄 {len(retrieval_results)} doc(s)")
            meta_parts.append(f"⏱️ {duration:.2f}s")
            meta_parts.append(f"🚀 {tokens_per_sec:.1f} tok/s")
            meta_parts.append(f"📝 {completion_tokens} tokens")
            metrics_text = " | ".join(meta_parts)

            await cl.Message(
                content=content,
                elements=[
                    cl.Text(name="Metrics", content=metrics_text, display="inline")
                ]
            ).send()
        else:
            debug_info = f"\n\nRaw Response: ```json\n{response.model_dump_json(indent=2)}\n```"
            await cl.Message(
                content=f"Error: Received empty response from LLM.{debug_info}"
            ).send()

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}\n\n```\n{traceback.format_exc()}\n```"
        await cl.Message(content=error_msg).send()
````

**Step 2: Commit**

```bash
git add backend/auth_test.py
git commit -m "feat: auto-query all indexed documents on every chat message"
```

---

## Phase 3: Frontend — Admin Document Management Panel

### Task 6: Build the Document Management UI in AdminDocuments.tsx

**Objective:** Replace the placeholder in `AdminDocuments.tsx` with a full UI for uploading, listing, and managing indexed documents.

**Files:**

- Modify: `frontend/src/pages/AdminDocuments.tsx`
- Create: `frontend/src/components/admin/DocumentUploader.tsx` (new)
- Create: `frontend/src/components/admin/DocumentList.tsx` (new)
- Read first: `frontend/src/pages/AdminDocuments.tsx` (from inventory), `frontend/src/pages/LLMSettings.tsx` (for UI patterns)

**Step 1: Create DocumentUploader component**

```tsx
import { apiClient } from '@/api';
import { AlertCircle, CheckCircle, FileText, Upload } from 'lucide-react';
import { useCallback, useState } from 'react';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';

interface DocumentUploaderProps {
  onUploadComplete: () => void;
}

export const DocumentUploader = ({
  onUploadComplete
}: DocumentUploaderProps) => {
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [message, setMessage] = useState<{
    type: 'success' | 'error';
    text: string;
  } | null>(null);

  const handleUpload = useCallback(
    async (file: File) => {
      if (!file.name.toLowerCase().endsWith('.pdf')) {
        setMessage({ type: 'error', text: 'Only PDF files are supported.' });
        return;
      }
      if (file.size > 50 * 1024 * 1024) {
        setMessage({ type: 'error', text: 'File too large. Max 50MB.' });
        return;
      }

      setUploading(true);
      setProgress(10);
      setMessage(null);

      try {
        const formData = new FormData();
        formData.append('file', file);
        setProgress(40);

        const response = await apiClient.post(
          '/project/pageindex/documents',
          formData,
          {
            headers: { 'Content-Type': 'multipart/form-data' }
          }
        );

        if (!response.ok) {
          const err = await response.text();
          throw new Error(err || `HTTP ${response.status}`);
        }

        setProgress(100);
        const data = await response.json();
        setMessage({
          type: 'success',
          text: `✅ "${data.filename}" queued for indexing (ID: ${data.doc_id}). Status: ${data.status}.`
        });
        setTimeout(onUploadComplete, 1500);
      } catch (err: any) {
        setMessage({ type: 'error', text: `Upload failed: ${err.message}` });
      } finally {
        setUploading(false);
        setTimeout(() => setProgress(0), 2000);
      }
    },
    [onUploadComplete]
  );

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      const file = e.dataTransfer.files[0];
      if (file) handleUpload(file);
    },
    [handleUpload]
  );

  const handleFileInput = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (file) handleUpload(file);
    },
    [handleUpload]
  );

  return (
    <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
      <CardHeader>
        <CardTitle className="flex items-center gap-2 text-primary">
          <Upload size={20} />
          Upload Document
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          className="border-2 border-dashed border-primary/30 rounded-xl p-8 text-center hover:border-primary/60 transition-colors cursor-pointer"
          onClick={() => document.getElementById('pdf-upload-input')?.click()}
        >
          <input
            id="pdf-upload-input"
            type="file"
            accept=".pdf"
            className="hidden"
            onChange={handleFileInput}
          />
          <FileText className="mx-auto h-12 w-12 text-muted-foreground mb-4" />
          <p className="text-sm text-muted-foreground">
            Drag & drop a PDF here, or click to browse
          </p>
          <p className="text-xs text-muted-foreground mt-2">
            Max 50MB • PDF only
          </p>
        </div>

        {uploading && <Progress value={progress} className="mt-4" />}

        {message && (
          <div
            className={`mt-4 flex items-center gap-2 text-sm ${
              message.type === 'success' ? 'text-green-500' : 'text-destructive'
            }`}
          >
            {message.type === 'success' ? (
              <CheckCircle size={16} />
            ) : (
              <AlertCircle size={16} />
            )}
            <span className="break-all">{message.text}</span>
          </div>
        )}
      </CardContent>
    </Card>
  );
};
```

**Step 2: Create DocumentList component**

```tsx
import { apiClient } from '@/api';
import {
  AlertCircle,
  CheckCircle,
  Clock,
  FileText,
  RefreshCw,
  Trash2
} from 'lucide-react';
import { useCallback, useEffect, useState } from 'react';

import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface DocumentMeta {
  doc_id: string;
  filename: string;
  status: 'indexing' | 'ready' | 'error';
  page_count: number;
  error_message: string;
  created_at: string;
  indexed_at: string;
}

export const DocumentList = () => {
  const [docs, setDocs] = useState<DocumentMeta[]>([]);
  const [loading, setLoading] = useState(true);
  const [deleting, setDeleting] = useState<string | null>(null);

  const fetchDocs = useCallback(async () => {
    try {
      const res = await apiClient.get('/project/pageindex/documents');
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      setDocs(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Failed to load documents:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchDocs();
  }, [fetchDocs]);

  // Auto-refresh while any doc is still indexing
  useEffect(() => {
    const indexing = docs.some((d) => d.status === 'indexing');
    if (!indexing) return;
    const timer = setTimeout(fetchDocs, 5000);
    return () => clearTimeout(timer);
  }, [docs, fetchDocs]);

  const handleDelete = async (docId: string) => {
    if (!confirm('Delete this document? It will no longer be queried.')) return;
    setDeleting(docId);
    try {
      const res = await apiClient.delete(
        `/project/pageindex/documents/${docId}`
      );
      if (!res.ok) throw new Error(await res.text());
      setDocs((prev) => prev.filter((d) => d.doc_id !== docId));
    } catch (err) {
      console.error('Delete failed:', err);
    } finally {
      setDeleting(null);
    }
  };

  const statusIcon = (status: string) => {
    switch (status) {
      case 'ready':
        return <CheckCircle size={14} className="text-green-500" />;
      case 'indexing':
        return <Clock size={14} className="text-yellow-500 animate-pulse" />;
      case 'error':
        return <AlertCircle size={14} className="text-destructive" />;
      default:
        return <Clock size={14} className="text-muted" />;
    }
  };

  const statusBadge = (status: string) => (
    <Badge
      variant={
        status === 'ready'
          ? 'default'
          : status === 'error'
            ? 'destructive'
            : 'secondary'
      }
    >
      {status}
    </Badge>
  );

  const readyCount = docs.filter((d) => d.status === 'ready').length;

  return (
    <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
      <CardHeader>
        <CardTitle className="flex items-center justify-between text-primary">
          <span className="flex items-center gap-2">
            <FileText size={20} />
            Indexed Documents
            {readyCount > 0 && (
              <Badge
                variant="outline"
                className="ml-1 text-green-500 border-green-500/30"
              >
                {readyCount} active
              </Badge>
            )}
          </span>
          <Button
            variant="ghost"
            size="sm"
            onClick={fetchDocs}
            disabled={loading}
          >
            <RefreshCw size={14} className={loading ? 'animate-spin' : ''} />
          </Button>
        </CardTitle>
      </CardHeader>
      <CardContent>
        {loading ? (
          <div className="text-center py-8 text-muted-foreground">
            Loading...
          </div>
        ) : docs.length === 0 ? (
          <div className="text-center py-8 text-muted-foreground">
            No documents indexed yet. Upload a PDF above — it will be
            automatically queried on every chat message.
          </div>
        ) : (
          <div className="space-y-3">
            {docs.map((doc) => (
              <div
                key={doc.doc_id}
                className="flex items-center justify-between p-3 rounded-lg border border-border/50 bg-muted/30 hover:bg-muted/50 transition-colors"
              >
                <div className="flex items-center gap-3 min-w-0">
                  <FileText size={20} className="text-primary shrink-0" />
                  <div className="min-w-0">
                    <p className="font-medium truncate">{doc.filename}</p>
                    <p className="text-xs text-muted-foreground">
                      ID: <code className="text-xs">{doc.doc_id}</code>
                      {doc.page_count > 0 && ` • ${doc.page_count} pages`}
                      {doc.status === 'ready' && doc.indexed_at && (
                        <>
                          {' '}
                          • indexed{' '}
                          {new Date(doc.indexed_at).toLocaleDateString()}
                        </>
                      )}
                      {doc.status === 'error' && doc.error_message && (
                        <>
                          {' '}
                          •{' '}
                          <span className="text-destructive">
                            {doc.error_message}
                          </span>
                        </>
                      )}
                    </p>
                  </div>
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  {statusIcon(doc.status)}
                  {statusBadge(doc.status)}
                  <Button
                    variant="ghost"
                    size="icon"
                    className="text-destructive hover:text-destructive"
                    onClick={() => handleDelete(doc.doc_id)}
                    disabled={deleting === doc.doc_id}
                  >
                    <Trash2 size={14} />
                  </Button>
                </div>
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
};
```

**Step 3: Rewrite AdminDocuments.tsx**

```tsx
import { useCallback, useState } from 'react';
import { Navigate } from 'react-router-dom';

import Page from 'pages/Page';

import { useAuth } from '@chainlit/react-client';

import { DocumentList } from '@/components/admin/DocumentList';
import { DocumentUploader } from '@/components/admin/DocumentUploader';

const AdminDocuments = () => {
  const { user } = useAuth();
  const role = user?.metadata?.role;
  const [refreshKey, setRefreshKey] = useState(0);

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  const handleUploadComplete = useCallback(() => {
    setRefreshKey((k) => k + 1);
  }, []);

  return (
    <Page>
      <div className="container max-w-4xl py-10 animate-in fade-in duration-500">
        <div className="mb-8">
          <h1 className="text-3xl font-bold tracking-tight text-primary">
            Document Knowledge Base
          </h1>
          <p className="text-muted-foreground mt-1">
            Upload PDFs to build a knowledge base. Every chat message
            automatically queries all indexed documents — no commands needed.
          </p>
        </div>

        <div className="space-y-6">
          <DocumentUploader
            key={`uploader-${refreshKey}`}
            onUploadComplete={handleUploadComplete}
          />
          <DocumentList key={`list-${refreshKey}`} />
        </div>
      </div>
    </Page>
  );
};

export default AdminDocuments;
```

**Step 4: Commit**

```bash
git add frontend/src/pages/AdminDocuments.tsx
git add frontend/src/components/admin/DocumentUploader.tsx
git add frontend/src/components/admin/DocumentList.tsx
git commit -m "feat: add PageIndex document management UI for admins"
```

---

## Phase 4: Build & Verify

### Task 7: Build frontend and verify

**Step 1: Build the frontend**

```bash
cd frontend && pnpm build
```

Expected: Clean build with no TypeScript errors.

**Step 2: Restart the app**

```bash
fuser -k 8001/tcp 2>/dev/null
sleep 2

cd /home/rdp/myproject/chainlitsrc/frontend && pnpm build

cd /home/rdp/myproject/chainlitsrc/backend
uv run chainlit run auth_test.py --port 8001 --host 0.0.0.0 --root-path /chats --headless \
  > backend/chainlit_exec.log 2>&1 &
```

**Step 3: Verify via browser**

1. Login as admin → navigate to `/admin/documents`
2. Upload a small PDF (<5MB) → verify it transitions from "indexing" to "ready" (auto-refreshes)
3. Go to chat → send any question → verify the "Searching N document(s)..." status appears
4. Verify the LLM answer is grounded in the document content
5. Delete the doc → verify the chat falls back to regular mode (no "Searching" status)

---

## Phase 5: Optional Enhancements (Future Tasks)

> These are out of scope for v1. Note that the agentic approach (Approach B) is already implemented — these are genuinely new features beyond it.

- **Markdown document support** — `client.index()` auto-detects `.md` files (mode="auto"). Simply upload a `.md` file instead of PDF to index it.
- **Per-user document scoping** — scope docs per user/org instead of globally shared
- **Streaming LLM response** — currently non-streaming. Could stream `client.chat.completions.create(..., stream=True)` for faster perceived latency
- **Document citation** — parse `AgentRetrievalResult.pages_used` and show which page(s) each answer part came from
- **Selective doc exclusion** — allow admin to mark docs as "exclude from auto-search"
- **Agent reasoning budget** — tune `ModelSettings(reasoning={"effort": "low|medium|high"})` for speed vs accuracy tradeoff
- **Agent per-query timeout** — set a timeout on each `Runner.run_sync()` call to avoid hanging on large documents

---

## Summary of Files

| Action | File                                                 |
| ------ | ---------------------------------------------------- |
| Modify | `backend/pyproject.toml`                             |
| Create | `backend/pageindex_service.py`                       |
| Modify | `backend/chainlit/server.py`                         |
| Modify | `backend/auth_test.py`                               |
| Modify | `frontend/src/pages/AdminDocuments.tsx`              |
| Create | `frontend/src/components/admin/DocumentUploader.tsx` |
| Create | `frontend/src/components/admin/DocumentList.tsx`     |
| Create | `backend/data/pageindex_documents/workspace/`        |
| Create | `backend/data/pageindex_documents/`                  |

**Total: 4 modified, 4 created**
