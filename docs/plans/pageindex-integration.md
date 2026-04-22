# PageIndex Integration — Implementation Plan (Refined)

> **Approach B: Full Agentic Retrieval using OpenAI Agents SDK**
>
> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Integrate [PageIndex](https://github.com/VectifyAI/PageIndex) as a vectorless, reasoning-based RAG layer into the Chainlitsec app. Admins upload PDFs via the admin panel → documents are indexed into a PageIndex tree. **Every chat message triggers an intelligent router that decides if the query requires document context.**

**Retrieval mechanism (verified from source):**

- `PageIndexClient.index(path)` → returns UUID doc_id, builds tree index, persists to workspace JSON
- `PageIndexClient` has **no retrieve() method** — retrieval uses the OpenAI Agents SDK agent loop
- Agent: `get_document()` → `get_document_structure()` → `get_page_content("5-7")` → answer

> **CRITICAL: LLM Routing Fix** (your provider is NOT OpenAI)
> Your current LLM config in `llm_settings.json`:
>
> - Provider: `opencode`
> - Model: `minimax-m2.5-free`
> - Base URL: `https://opencode.ai/zen/v1`
>
> The Agents SDK by default sends to `api.openai.com` — we must pass a custom `AsyncOpenAI` client with your provider's base_url. The service code handles this correctly.

**Architecture:**

1. **Admin uploads PDF** → saved to disk → PageIndexClient.index_document() $\to$ tree index stored
2. **User sends ANY message**
   - **Step A (The Router):** An LLM-based classifier decides: Is this a "Knowledge Base" question or just "Chat"?
   - **Step B (If Knowledge):** System triggers agentic retrieval across relevant docs via PageIndex.
   - **Step C (The Injection):** Retrieved context is injected into the conversation history for grounding.
3. **Fallback:** If the router determines no search is needed, or if retrieval returns nothing, the agent answers from its own knowledge.

**Tech Stack:** Python backend (existing `auth_test.py`), Pageindex library (`pageindex` + `litellm`), React frontend (existing), local file storage.

---

## Phase 0: Inventory — ✅ COMPLETED

> ⚠️ Read all files listed below before any implementation begins.

✅ All Phase 0 files verified present:

- `backend/auth_test.py` — existing chat handler (entry point)
- `backend/llm_settings.json` — current LLM config
- `backend/chainlit/server.py:813-890` — existing API endpoint pattern (llm-settings)
- `backend/chainlit/__init__.py` — Chainlit module exports
- `backend/pyproject.toml` — dependency management
- `frontend/src/pages/AdminDocuments.tsx` — admin doc panel
- `frontend/src/components/chat/MessageComposer/index.tsx` — message composer
- `frontend/src/components/chat/MessageComposer/UploadButton.tsx` — upload button
- `frontend/src/hooks/useUpload.tsx` — upload hook
- `frontend/src/router.tsx` — route definitions

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

\\

## Phase 2: Backend — PageIndex Service Layer

### Task 3: Create pageindex_service.py — the core service class

**Objective:** Build a `PageIndexService` singleton that:

1. Stores PDFs to disk and indexes them via `PageIndexClient`
2. Uses the **OpenAI Agents SDK** for agentic retrieval — the agent reasons over the document tree and calls tools (`get_document`, `get_document_structure`, `get_page_content`) to answer questions
3. **CRITICAL:** Routes to YOUR configured LLM provider (opencode/minimax) — not OpenAI's default API
4. Manages document metadata across restarts
5. Includes an LLM-based "Router" to decide if the query needs document context

**Files:**

- Create: `backend/pageindex_service.py`

**Step 1: Write the service**

The service MUST include these key methods:

```python
class PageIndexService:
    def _load_llm_config(self) -> dict:
        """Load LLM config from llm_settings.json."""
        import json
        config_path = Path(__file__).parent / "llm_settings.json"
        with open(config_path) as f:
            config = json.load(f)
        return next(p for p in config["providers"] if p.get("is_active"))

    def _get_openai_client(self) -> AsyncOpenAI:
        """Get AsyncOpenAI client configured with YOUR provider."""
        config = self._load_llm_config()
        return AsyncOpenAI(
            base_url=config["base_url"],  # https://opencode.ai/zen/v1
            api_key=config["api_key"],
        )

    def _run_agent_for_doc(self, doc_id, doc_name, query, model):
        """Run agent with custom client to route to YOUR provider."""
        from agents import Agent, Runner, function_tool
        from agents.models import OpenAIChatCompletionsModel

        openai_client = self._get_openai_client()
        llm_config = self._load_llm_config()

        # Use OpenAIChatCompletionsModel with your custom client
        chat_model = OpenAIChatCompletionsModel(
            model=llm_config["model"],  # minimax-m2.5-free
            openai_client=openai_client,  # routes to opencode.ai/zen/v1
        )

        agent = Agent(
            model=chat_model,  # <-- CRITICAL: use chat_model, not string
            tools=[get_document, get_document_structure, get_page_content],
            ...
        )
        result = Runner.run_sync(agent, query)
        return result.final_output
```

**Step 2: Commit**

```bash
git add backend/pageindex_service.py
git commit -m "feat: add PageIndexService with agentic retrieval & router"
```

---

### Task 4: Add API endpoints for PageIndex document management

**Objective:** Add FastAPI endpoints for uploading, listing, retrieving, and deleting documents.

**Files:**

- Modify: `backend/chainlit/server.py`

**Step 1: Add the endpoints after the llm-settings section**
_(Adding docs management, status, and upload/delete endpoints)_

**Step 2: Commit**

```bash
git add backend/chainlit/server.py
git commit -m "feat: add PageIndex REST API endpoints for document management"
```

### Task 4b: Test the API endpoints

**Objective:** Verify all PageIndex API endpoints are working correctly before proceeding to frontend.

**Step 1: Test the endpoints with curl**

```bash
# Assumes you have a session cookie from logging in
COOKIE="..."  # your session cookie

# 1. Get documents status summary
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/status"

# Expected: {"total":0,"ready":0,"ready_doc_ids":[]}

# 2. List all documents
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents"

# Expected: []

# 3. Upload a test PDF (as admin)
curl -s -X POST -H "Cookie: $COOKIE" \
  -F "file=@/path/to/test.pdf" \
  "http://localhost:8001/project/pageindex/documents"

# Expected: {"doc_id":"...","filename":"test.pdf","status":"indexing",...}

# Wait 10s for indexing, then check status again

# 4. Get single document metadata
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/{doc_id}"

# Expected: {"doc_id":"...","filename":"test.pdf","status":"ready","page_count":N,...}

# 5. Get document structure
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/{doc_id}/structure"

# Expected: {"doc_id":"...","structure":"..."} (JSON tree)

# 6. Get page content
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/{doc_id}/content?pages=1-3"

# Expected: {"doc_id":"...","pages":"1-3","content":"..."}

# 7. Delete document
curl -s -X DELETE -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/{doc_id}"

# Expected: {"deleted":"{doc_id}"}

# 8. Verify it's gone
curl -s -H "Cookie: $COOKIE" \
  "http://localhost:8001/project/pageindex/documents/status"

# Expected: {"total":0,"ready":0,"ready_doc_ids":[]}
```

**Step 2: Commit the test results**

```bash
git add -A
git commit -m "test: verify PageIndex API endpoints"
```

---

## Phase 3: Frontend — Admin Document Management Panel

### Task 5: Build the Document Management UI in AdminDocuments.tsx

**Objective:** Replace the placeholder in `AdminDocuments.tsx` with a full UI for uploading, listing, and managing indexed documents.

**Files:**

- Modify: `frontend/src/pages/AdminDocuments.tsx`
- Create: `frontend/src/components/admin/DocumentUploader.tsx` (new)
- Create: `frontend/src/components/admin/DocumentList.tsx` (new)

**Step 1: Create DocumentUploader component**
**Step 2: Create DocumentList component**
**Step 3: Rewrite AdminDocuments.tsx**
**Step 4: Commit**

---

## Phase 4: Build & Verify

### Task 6: Build frontend and verify

- **Build:** `cd frontend && pnpm build`
- **Verification Steps:**
  1. Admin upload test.
  2. Chat testing (verify the "Router" prevents unnecessary searches for simple chat).
  3. Validation of accuracy via "Page-level" citations.
