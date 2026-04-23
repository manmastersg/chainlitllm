"""
PageIndex Service — Vectorless RAG for Chainlit

Uses PageIndex for hierarchical tree-based document indexing and agentic retrieval.
Routes to the user's configured LLM (from llm_settings.json), not OpenAI default.
"""
import json
import os
import threading
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger("pageindex_service")

# ─────────────────────────────────────────────────────────────────────────────
# Configure litellm BEFORE PageIndex is imported
# PageIndex calls litellm internally, so env vars must be set first.
# ─────────────────────────────────────────────────────────────────────────────

_config_path = Path(__file__).parent / "llm_settings.json"
if _config_path.exists():
    with open(_config_path) as f:
        _llm_config = json.load(f)
    for _provider in _llm_config.get("providers", []):
        if _provider.get("is_active"):
            # litellm uses OPENAI_API_BASE and OPENAI_API_KEY for OpenAI-compatible APIs
            os.environ["OPENAI_API_BASE"] = _provider["base_url"]
            os.environ["OPENAI_API_KEY"] = _provider["api_key"]
            # Provider-prefixed model so litellm routes to the right endpoint
            _provider_type = _provider.get("provider_type", "openai")
            _raw_model = _provider["model"]
            # litellm model format: "provider/model" (e.g., "openai/minimax-m2.5-free")
            _LITELLM_MODEL = _provider_type + "/" + _raw_model
            break
else:
    _LITELLM_MODEL = "gpt-4o-2024-11-20"

# PageIndex imports (after litellm env vars are configured)
from pageindex import LocalClient  # noqa: E402
from pageindex.client import IndexConfig  # noqa: E402
from agents import set_tracing_disabled  # noqa: E402

set_tracing_disabled(True)

# ─────────────────────────────────────────────────────────────────────────────
# litellm global settings (applies to all PageIndex internal LLM calls)
# ─────────────────────────────────────────────────────────────────────────────
import litellm  # noqa: E402

litellm.request_timeout = 60  # seconds per LLM call — prevents indefinite hangs
litellm.max_retries = 1        # reduced to 1 to fail fast if rate limited


class PageIndexService:
    """
    Singleton service for document indexing and agentic retrieval.
    
    Handles:
    - PDF storage and indexing via PageIndex
    - Agentic retrieval using OpenAI Agents SDK
    - LLM routing (configurable, defaults to user's active provider)
    - Document metadata persistence across restarts
    """
    
    _instance: Optional["PageIndexService"] = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, storage_path: str | None = None):
        if hasattr(self, "_initialized"):
            return
        
        # Storage path for PDFs and PageIndex workspace
        if storage_path is None:
            base_dir = Path(__file__).parent.parent / "data" / "pageindex_documents"
            storage_path = str(base_dir / "workspace")
        
        self._storage_path = Path(storage_path)
        self._storage_path.mkdir(parents=True, exist_ok=True)
        
        # PageIndex client (lazy init)
        self._client: Optional[LocalClient] = None
        self._documents_meta_path = self._storage_path / "documents.json"
        self._documents: dict = {}  # doc_id -> metadata
        
        # Load persisted document metadata
        self._load_documents()
        logger.info("DEBUG: PageIndexService initialized. Loaded %d documents.", len(self._documents))
        
        self._initialized = True
    
    # ─────────────────────────────────────────────────────────────
    # LLM Configuration
    # ─────────────────────────────────────────────────────────────
    
    def _load_llm_config(self) -> dict:
        """Load active LLM config from llm_settings.json."""
        config_path = Path(__file__).parent / "llm_settings.json"
        with open(config_path) as f:
            config = json.load(f)
        
        # Find active provider
        for provider in config.get("providers", []):
            if provider.get("is_active"):
                return provider
        
        raise ValueError("No active LLM provider found in llm_settings.json")
    
    def _get_openai_client(self):
        """Get AsyncOpenAI client configured with user's provider."""
        from openai import AsyncOpenAI
        
        config = self._load_llm_config()
        return AsyncOpenAI(
            base_url=config["base_url"],
            api_key=config["api_key"],
        )
    
    # ─────────────────────────────────────────────────────────────
    # PageIndex Client
    # ─────────────────────────────────────────────────────────────
    
    @property
    def _pageindex_client(self) -> LocalClient:
        """Lazy-init PageIndex client."""
        if self._client is None:
            # IndexConfig with provider-prefixed model for litellm routing
            index_config = IndexConfig(
                model=_LITELLM_MODEL,
                max_page_num_each_node=10,      # was: unlimited — split large nodes sooner
                max_token_num_each_node=8000,   # was: 20000 — smaller chunks = fewer LLM calls
            )
            
            self._client = LocalClient(
                storage_path=str(self._storage_path),
                index_config=index_config,
            )
        
        return self._client
    
    @property
    def _collection(self):
        """Get the default collection."""
        return self._pageindex_client.collection("default")
    
    # ─────────────────────────────────────────────────────────────
    # Document Management
    # ─────────────────────────────────────────────────────────────
    
    def _load_documents(self):
        """Load document metadata from persistent storage."""
        if self._documents_meta_path.exists():
            with open(self._documents_meta_path) as f:
                self._documents = json.load(f)
        else:
            self._documents = {}
    
    def _save_documents(self):
        """Save document metadata to persistent storage."""
        with open(self._documents_meta_path, "w") as f:
            json.dump(self._documents, f, indent=2)
    
    def _run_indexing_background(self, doc_id: str, dest_path: Path, estimated_calls: int):
        """Run indexing in background thread."""
        try:
            from pageindex.utils import _start_pageindex_run, _pageindex_call_counter
            import time
            import threading
            
            _start_pageindex_run(estimated_calls)
            
            # Start a polling thread to watch the pageindex internal counter
            # and update our local dictionary so the frontend API can see it.
            def progress_poller():
                last_count = 0
                while True:
                    if doc_id not in self._documents or self._documents[doc_id].get("status") != "indexing":
                        break
                        
                    current_count = _pageindex_call_counter.get("count", 0)
                    if current_count != last_count:
                        last_count = current_count
                        percent = min(99, int((current_count / max(1, estimated_calls)) * 100))
                        
                        self._documents[doc_id]["progress"] = percent
                        self._documents[doc_id]["completed_calls"] = current_count
                        self._save_documents()
                    
                    time.sleep(1.0)
            
            poller_thread = threading.Thread(target=progress_poller, daemon=True)
            poller_thread.start()
            
            # Run the actual heavy LLM indexing
            try:
                returned_doc_id = self._collection.add(str(dest_path))
            except Exception as inner_e:
                if "Processing failed" in str(inner_e) and estimated_calls <= 20:
                    # PageIndex failed because the document is too small/simple (no TOC)
                    # We will gracefully fall back to a single flat node
                    returned_doc_id = doc_id
                    
                    import PyPDF2
                    with open(dest_path, 'rb') as f_pdf:
                        text = PyPDF2.PdfReader(f_pdf).pages[0].extract_text()
                        
                    # Build faked internal document metadata
                    from pageindex.utils import count_tokens
                    faked_meta = {
                        "filename": dest_path.name,
                        "page_count": 1,
                        "token_count": count_tokens(text),
                        "nodes": [{
                            "node_id": "0000",
                            "title": dest_path.stem,
                            "summary": "Document content.",
                            "start_index": 1,
                            "end_index": 1
                        }]
                    }
                    
                    # Save to pageindex collection storage directly
                    workspace_dir = self._storage_path / "default"
                    workspace_dir.mkdir(parents=True, exist_ok=True)
                    doc_dir = workspace_dir / returned_doc_id
                    doc_dir.mkdir(parents=True, exist_ok=True)
                    
                    with open(doc_dir / "document.json", "w") as f_meta:
                        json.dump(faked_meta, f_meta)
                else:
                    raise inner_e
            
            # Fetch final metadata
            doc_meta = self._collection.get_document(returned_doc_id)
            meta = json.loads(doc_meta) if isinstance(doc_meta, str) else doc_meta
            
            # Mark as ready
            if doc_id in self._documents:
                self._documents[doc_id]["status"] = "ready"
                self._documents[doc_id]["progress"] = 100
                
                # Page count might be in 'page_count' or length of 'pages' list
                page_count = meta.get("page_count")
                if page_count is None and "pages" in meta:
                    pages = meta["pages"]
                    page_count = len(pages) if isinstance(pages, list) else 0
                
                self._documents[doc_id]["page_count"] = page_count or 0
                self._documents[doc_id]["doc_id"] = returned_doc_id # Update to real ID
                
                # Clean up temp ID if changed
                if doc_id != returned_doc_id:
                    self._documents[returned_doc_id] = self._documents.pop(doc_id)
                    
                self._save_documents()
                
                # Emit final completion
                try:
                    from chainlit.context import context as cl_context
                    emitter = cl_context.emitter
                    if emitter:
                        import asyncio
                        loop = asyncio.get_event_loop()
                        if loop.is_running():
                            asyncio.run_coroutine_threadsafe(
                                emitter.emit("pageindex_progress", {
                                    "doc_id": returned_doc_id,
                                    "status": "ready",
                                    "percent": 100
                                }),
                                loop
                            )
                except Exception:
                    pass

        except Exception as e:
            logger.error("PageIndex background error: %s", e)
            if doc_id in self._documents:
                self._documents[doc_id]["status"] = "failed"
                self._documents[doc_id]["error"] = str(e)
                self._save_documents()

    def add_document(self, file_path_str: str) -> dict:
        """
        Add a PDF document to the index (asynchronous).
        
        Args:
            file_path_str: Path to the PDF file
            
        Returns:
            dict with temporary doc_id, filename, status
        """
        import time
        import threading
        from pathlib import Path
        
        file_path = Path(file_path_str)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Create temp doc_id and copy file
        temp_doc_id = file_path.stem + "_" + str(int(time.time()))
        dest_path = self._storage_path / f"{temp_doc_id}.pdf"
        
        import shutil
        import PyPDF2
        shutil.copy2(file_path, dest_path)

        # Count pages for budget
        try:
            with open(dest_path, 'rb') as f:
                page_count = len(PyPDF2.PdfReader(f).pages)
        except Exception:
            page_count = 0

        estimated_llm_calls = max(page_count, 1) * 4
        
        # Store initial pending state
        self._documents[temp_doc_id] = {
            "doc_id": temp_doc_id,
            "filename": file_path.name,
            "status": "indexing",
            "page_count": page_count,
            "progress": 0,
            "total_calls": estimated_llm_calls,
            "added_at": time.time(),
            "path": str(dest_path),
        }
        self._save_documents()
        
        # Start background processing
        thread = threading.Thread(
            target=self._run_indexing_background,
            args=(temp_doc_id, dest_path, estimated_llm_calls),
            daemon=True
        )
        thread.start()
        
        return self._documents[temp_doc_id]
    
    def list_documents(self) -> list:
        """List all indexed documents."""
        return list(self._documents.values())
    
    def get_document(self, doc_id: str) -> dict:
        """Get document metadata."""
        return self._documents.get(doc_id)
    
    def get_document_structure(self, doc_id: str) -> str:
        """Get document tree structure (JSON)."""
        return self._collection.get_document_structure(doc_id)
    
    def get_page_content(self, doc_id: str, pages: str) -> str:
        """
        Get content of specific pages.
        
        Args:
            doc_id: Document ID
            pages: Page range like '1-3', '5,8', '12'
        """
        return self._collection.get_page_content(doc_id, pages)
    
    def delete_document(self, doc_id: str) -> dict:
        """Delete a document from the index."""
        if doc_id not in self._documents:
            raise KeyError(f"Document not found: {doc_id}")
        
        # Delete from PageIndex
        self._collection.delete_document(doc_id)
        
        # Remove file
        doc_path = Path(self._documents[doc_id]["path"])
        if doc_path.exists():
            doc_path.unlink()
        
        # Remove metadata
        del self._documents[doc_id]
        self._save_documents()
        
        return {"deleted": doc_id}
    
    # ─────────────────────────────────────────────────────────────
    # Agentic Retrieval (Router + Query)
    # ─────────────────────────────────────────────────────────────
    
    def should_query_documents(self, user_message: str) -> bool:
        """
        LLM-based router: decides if the query needs document context.
        
        Simple heuristic: if the message mentions KB terms, doc names, or
        asks about specific content, likely needs docs.
        """
        message_lower = user_message.lower()
        
        # Quick keyword check first
        kb_keywords = [
            "document", "pdf", "file", "write", "policy", "procedure",
            "manual", "guide", "documentation", "spec", "requirements",
            # Project-specific terms could be added
        ]
        
        # If no docs are indexed, skip
        if not self._documents:
            return False
        
        # If user explicitly asks about the documents
        for kw in kb_keywords:
            if kw in message_lower:
                return True
        
        # Default: query if we have docs (can be tuned later)
        return bool(self._documents)
    
    def query(self, question: str, doc_ids: list | None = None) -> str:
        """
        Agentic retrieval: runs the PageIndex agent to answer a question.
        
        Uses OpenAI Agents SDK with user's configured LLM (not OpenAI default).
        
        Args:
            question: The user's question
            doc_ids: Optional list of doc IDs to query (queries all if None)
            
        Returns:
            Agent's answer string
        """
        logger.info("DEBUG: PageIndexService.query called with question: %s", question)
        # Create agent tools using the collection
        from agents import Agent, Runner, function_tool
        
        collection = self._collection
        
        # Use the loaded documents dict for retrieve functions
        documents = self._documents
        
        @function_tool
        def get_document(doc_id: str | None = None) -> str:
            """Get document metadata: status, page count, name, description."""
            if doc_id is None:
                # List all docs
                return json.dumps(list(documents.values()))
            return collection.get_document(next(iter(documents.keys())))
        
        @function_tool
        def get_document_structure(doc_id: str | None = None) -> str:
            """Get the document's full tree structure to find relevant sections."""
            doc_id = doc_id or (next(iter(documents.keys())) if documents else None)
            if not doc_id:
                return "No documents indexed"
            return collection.get_document_structure(doc_id)
        
        @function_tool
        def get_page_content(doc_id: str | None = None, pages: str = "1-3") -> str:
            """
            Get the text content of specific pages.
            Use tight ranges: '5-7' for pages 5 to 7, '3,8' for pages 3 and 8.
            """
            doc_id = doc_id or (next(iter(documents.keys())) if documents else None)
            if not doc_id:
                return "No documents indexed"
            return collection.get_page_content(doc_id, pages)
        
        # Get the LLM config for routing
        llm_config = self._load_llm_config()
        
        # Create custom model that routes to user's provider
        from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
        
        openai_client = self._get_openai_client()
        
        # Use OpenAIChatCompletionsModel with custom client for non-OpenAI routing
        chat_model = OpenAIChatCompletionsModel(
            model=llm_config["model"],
            openai_client=openai_client,
        )
        
        AGENT_INSTRUCTIONS = """You are a document QA assistant. Your goal is to answer the user's question based on the provided documents.

Important:
- Call get_document() first to confirm which documents are available and their page count.
- Call get_document_structure() to identify relevant sections.
- Call get_page_content() with tight page ranges (e.g., '5-7', not '1-100').
- Answer based ONLY on the document content. Do not make up information.
- If the documents don't contain the answer, say so clearly."""
        
        agent = Agent(
            name="PageIndex-QA",
            instructions=AGENT_INSTRUCTIONS,
            tools=[get_document, get_document_structure, get_page_content],
            model=chat_model,  # Uses the custom client -> routes to user's provider
        )
        
        # Run the agent
        from agents import RunConfig
        result = Runner.run_sync(agent, question, run_config=RunConfig(tracing_disabled=True))
        return result.final_output
    
    def build_rag_context(self, user_message: str) -> str:
        """
        Build RAG context for a user message.
        
        Returns:
            Context string to prepend to the user's message, or empty string.
        """
        if not self.should_query_documents(user_message):
            return ""
        
        if not self._documents:
            return ""
        
        # Query all indexed documents
        try:
            answer = self.query(user_message)
            if answer:
                context = f"""[Document Context]

The following information is from your knowledge base:

{answer}

---
"""
                return context
        except Exception:
            logger.exception("PageIndex query error")
        
        return ""


# ─────────────────────────────────────────────────────────────
# Singleton accessor
# ─────────────────────────────────────────────────────────────

def get_pageindex_service() -> PageIndexService:
    """Get the singleton PageIndexService instance."""
    return PageIndexService()