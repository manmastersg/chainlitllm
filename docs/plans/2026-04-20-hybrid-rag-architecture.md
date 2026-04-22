# Hybrid RAG Architecture: PageIndex + Vector RAG

> **Research & Recommendation Document** — For integrating both RAG systems into Chainlitsec.
> No code changes. Planning only.

---

## Executive Summary

**Goal:** Combine PageIndex RAG (PDFs, reasoning-based) and Vector RAG (PPTX/XLSX/MD/CSV, embedding-based) into a single unified retrieval layer that serves the LLM the most relevant context from all document types.

**Recommended Architecture:** `Parallel Retrieval + Unified Merger` — both pipelines run concurrently on every query, results are scored and merged into a single ranked context fed to the LLM.

**File type routing:**

| File Type | RAG System                     | Reason                                                     |
| --------- | ------------------------------ | ---------------------------------------------------------- |
| `.pdf`    | **PageIndex** (reasoning/tree) | Complex docs, page-level reasoning, no chunking needed     |
| `.pptx`   | **Vector RAG**                 | Slides are self-contained units, semantic chunk works well |
| `.xlsx`   | **Vector RAG**                 | Tabular data — chunks preserve row relationships           |
| `.md`     | **Vector RAG**                 | Markdown structure → natural header-based chunks           |
| `.csv`    | **Vector RAG**                 | Row-based data → semantic chunking preserves columns       |

---

## Part 1: Deep-Dive on Both Systems

### PageIndex RAG — How It Works

PageIndex is a **reasoning-based, vectorless RAG** system. Instead of semantic embedding search, it uses a **hierarchical tree index** built from the document structure.

**Indexing (one-time per PDF):**

```
PDF → Parser (pypdf/ unstructured) → Page extraction
    → Tree construction: root node → section nodes → page nodes
    → Each node tagged with LLM-generated summary
    → Tree stored as JSON/graph structure
```

**Query time (retrieval):**

```
User query → LLM traverses tree (guided reasoning)
    → Identifies relevant branches (sections/pages)
    → Returns the actual page text content as context
```

**Key strengths:**

- **No chunking** — works at page/section granularity, preserves context
- **Reasoning-based** — LLM understands document structure, can navigate logically
- **98.7% accuracy on FinanceBench** — best-in-class for complex financial/legal documents
- **No embedding model needed** — uses the same LLM already configured in the app
- **Transparent reasoning path** — tree traversal can be logged/explained

**Key limitations:**

- PDF only
- Latency per query: ~1-3 LLM calls for tree traversal (not just one API call)
- Cost: lightweight LLM calls during retrieval (but the main answer call is the same)
- Indexing takes time (LLM-generated summaries per section)

---

### Vector RAG — How It Works

**Standard pipeline:**

```
Document → File Parser → Text Extractor
    → Chunking (semantic or fixed-size) → each chunk gets unique ID + metadata
    → Embedding model (e.g., text-embedding-3-small) → vector per chunk
    → Vector DB (ChromaDB) stores (chunk_text, metadata, vector)

Query → Same embedding model → query_vector
    → ANN search (cosine similarity) → top-K chunks
    → Return chunk texts + metadata
```

**Key strengths:**

- Works on **any file type** with the right parser
- Fast (pure vector math, no LLM needed at retrieval)
- Semantic understanding — finds conceptually related content even without exact keyword matches
- Mature ecosystem — ChromaDB, FAISS, pgvector, Qdrant

**Key limitations:**

- **Chunking is lossy** — loses document structure, context between chunks
- Needs an **embedding model** (local or API)
- Needs a **vector database** — additional infrastructure
- Cannot reason about document relationships (e.g., "this section contradicts that table")
- Quality depends heavily on chunking strategy

---

## Part 2: File Type → RAG System Mapping

### Why PageIndex is Best for PDFs

PDFs have rich, complex structure — headers, paragraphs, tables, footnotes, page numbers. Vector RAG's flat chunking destroys this structure. PageIndex preserves it via tree navigation.

Example: A financial report PDF with:

- Table of contents → PageIndex builds tree from TOC structure
- Q: "What was the Q3 revenue?" → PageIndex traverses tree to find financial tables → returns exact page content with numbers in context

Vector RAG would chunk this arbitrarily — might split a table across chunks, lose the header context, retrieve a semantically similar but wrong table.

### Why Vector RAG is Best for PPTX/XLSX/MD/CSV

**PPTX files:**

- Structure: Slides are self-contained visual units
- Text extraction: Each slide's text blocks → semantic chunks
- Chunks preserve slide-level context naturally
- PageIndex would be overkill — PPTX structure is flat (no deep hierarchy like a PDF)

**XLSX/CSV files:**

- Structure: Rows × Columns with headers
- Flattening to text: `"Sheet: Sales, Row: [Q1=100, Q2=200, Q3=300]" → chunk`
- Chunking by row groups preserves tabular relationships
- PageIndex has no advantage here — XLSX is not a "document" with logical sections

**MD files:**

- Structure: Headers (# ## ###) create a natural document tree
- Semantic chunking at header boundaries preserves structure
- Could also use PageIndex for MD (it supports it), but Vector RAG is simpler and sufficient

---

## Part 3: Recommended Architecture

### Overall Flow

```
User message
    │
    ├─────────────────────────────────────────────┐
    │           PARALLEL RETRIEVAL                │
    │                                             │
    │  ┌─────────────────┐  ┌──────────────────┐ │
    │  │  PageIndex RAG  │  │   Vector RAG     │ │
    │  │  (PDFs only)    │  │ (PPTX/XLSX/MD/CSV)│ │
    │  └────────┬────────┘  └────────┬─────────┘ │
    │           │                    │            │
    │           │ Context chunks     │ Chunks     │
    │           │ + source labels   │ + scores   │
    │           └────────┬───────────┘            │
    │                    │                        │
    │           ┌────────▼────────┐               │
    │           │  RESULT MERGER  │               │
    │           │ (score + merge) │               │
    │           └────────┬────────┘               │
    │                    │                        │
    │         Unified ranked context             │
    │                    │                        │
    └────────────────────┼───────────────────────┘
                         │
                         ▼
                  System prompt with
                  unified context
                         │
                         ▼
                    LLM Answer
```

### Component 1: Result Merger (The Core Problem)

When both systems return results, they use **incompatible scoring**:

| System     | Score Meaning                                | Range                |
| ---------- | -------------------------------------------- | -------------------- |
| PageIndex  | LLM confidence in relevance (tree traversal) | arbitrary LLM output |
| Vector RAG | Cosine similarity of embeddings              | 0.0 – 1.0            |

**Three merging strategies, ranked by quality:**

#### Strategy A: LLM-as-Reranker (Best Quality, Higher Cost)

```
1. Collect top-K from each system (e.g., top-5 PageIndex + top-5 Vector)
2. Send ALL retrieved chunks to the LLM with a reranking prompt
3. LLM ranks and selects the most relevant chunks, explains why
4. Return the selected chunks as final context
```

**Pros:** Best quality — LLM understands relevance across both systems
**Cons:** Extra LLM call per query (but lightweight — 500 tokens max)
**Recommendation:** ✅ Use this. The quality gain is worth the extra call.

Prompt for reranking:

```
You are a research assistant. A user asked: "{query}"

I retrieved the following content from their knowledge base:

--- From PDF (PageIndex) ---
{doc_name}, Page N
{page_content}

--- From spreadsheet (Vector RAG) ---
{doc_name}, Sheet: {sheet}, Rows {r1}-{r2}
{chunk_content}

--- From presentation (Vector RAG) ---
{slide_name}, Slide N
{slide_content}

Task: Select the chunks most relevant to the user's question.
Discard chunks that are irrelevant or redundant.
Return the selected chunks in order of relevance.
For each chunk, briefly explain why it's relevant (1 sentence).
```

#### Strategy B: Reciprocal Rank Fusion (Simple, No Extra Cost)

```
Score each result by its rank position across systems:
fusion_score(doc) = Σ (1 / (k + rank_in_system))
```

**Pros:** Zero extra cost, no additional LLM calls
**Cons:** Loses information — doesn't account for quality of match within a rank
**Recommendation:** Use as a fallback if Strategy A latency is too high

#### Strategy C: Hybrid Score Normalization (Balanced)

```
1. Normalize Vector RAG cosine similarity to [0, 1]
2. Normalize PageIndex tree depth/relevance to [0, 1]
   (e.g., tree_level = 1 - (depth / max_depth), confidence = LLM rating)
3. Combined score = (0.4 × normalized_vector_score) + (0.6 × normalized_pageindex_score)
```

**Pros:** Fast (no extra LLM call), interpretable
**Cons:** Requires tuning the weights — might miss cases
**Recommendation:** Use as v1, upgrade to Strategy A once the system is stable

---

### Component 2: Unified Chunk Schema

Both systems must return chunks in the same format so the merger and LLM can handle them uniformly:

```python
@dataclass
class RetrievedChunk:
    chunk_id: str           # unique: "pdf_{doc_id}_p{page}" or "vec_{doc_id}_{chunk_num}"
    source_type: str        # "pageindex" or "vector"
    doc_type: str           # "pdf", "pptx", "xlsx", "md", "csv"
    doc_id: str             # shared document identifier
    doc_name: str           # human-readable filename
    content: str            # the actual text content
    metadata: dict          # source-specific: page number, sheet name, slide number, etc.
    score: float            # 0.0-1.0 normalized relevance score
```

This lets the LLM know exactly where each chunk came from without needing to know which RAG system generated it.

---

### Component 3: Vector RAG Implementation Details

#### File Parsers

```python
# PPTX — each slide becomes a chunk
from pptx import Presentation

def parse_pptx(file_path: str) -> list[dict]:
    prs = Presentation(file_path)
    chunks = []
    for i, slide in enumerate(prs.slides):
        text_parts = []
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text_parts.append(shape.text.strip())
        slide_text = "\n".join(filter(None, text_parts))
        if slide_text:
            chunks.append({
                "content": slide_text,
                "metadata": {"slide_number": i + 1, "total_slides": len(prs.slides)}
            })
    return chunks

# XLSX — rows grouped by semantic context
import pandas as pd

def parse_xlsx(file_path: str) -> list[dict]:
    chunks = []
    xl = pd.ExcelFile(file_path)
    for sheet_name in xl.sheet_names:
        df = xl.parse(sheet_name)
        # Group every N rows to keep chunks manageable (e.g., 20 rows per chunk)
        chunk_size = 20
        for start in range(0, len(df), chunk_size):
            chunk_df = df.iloc[start:start + chunk_size]
            content = f"Sheet: {sheet_name}\n{chunk_df.to_csv(index=False)}"
            chunks.append({
                "content": content,
                "metadata": {"sheet": sheet_name, "rows": f"{start}-{start+len(chunk_df)}"}
            })
    return chunks

# MD — chunk at header boundaries
import re

def parse_md(file_path: str) -> list[dict]:
    with open(file_path) as f:
        content = f.read()

    chunks = []
    sections = re.split(r'\n(?=#+\s)', content)  # split at markdown headers
    for section in sections:
        if section.strip():
            header = section.split('\n')[0]
            body = '\n'.join(section.split('\n')[1:])
            chunks.append({
                "content": f"{header}\n{body}".strip(),
                "metadata": {"header": header.strip()}
            })
    return chunks

# CSV — row groups with header context
def parse_csv(file_path: str) -> list[dict]:
    df = pd.read_csv(file_path)
    chunks = []
    chunk_size = 15
    for start in range(0, len(df), chunk_size):
        chunk_df = df.iloc[start:start + chunk_size]
        header_context = ", ".join(df.columns.tolist())
        content = f"Columns: {header_context}\n{chunk_df.to_csv(index=False)}"
        chunks.append({
            "content": content,
            "metadata": {"rows": f"{start}-{start+len(chunk_df)}", "columns": list(df.columns)}
        })
    return chunks
```

#### Embedding Model Options

| Option                            | Model                                     | Pros                                                       | Cons                                             |
| --------------------------------- | ----------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Recommended: Use same LLM API** | OpenAI `text-embedding-3-small`           | Best quality, no local GPU needed, cheap ($0.02/1M tokens) | Depends on external API, slight latency          |
| **Local (no external API)**       | `sentence-transformers/all-MiniLM-L6-v2`  | Fast, offline, private                                     | Lower quality, CPU-bound, adds ~500MB dependency |
| **Local GPU (if you have one)**   | `sentence-transformers/all-mpnet-base-v2` | Best local quality                                         | GPU required                                     |

**Recommendation:** Use `text-embedding-3-small` via the existing OpenAI-compatible API (same API key as the chat LLM). No new dependencies, consistent with existing architecture.

#### Vector Database Options

| Option                     | Type                 | Pros                                                | Cons                                   |
| -------------------------- | -------------------- | --------------------------------------------------- | -------------------------------------- |
| **ChromaDB** (recommended) | Embedded Python DB   | Zero-config, pip-install, works well with LangChain | Single-node only (fine for your scale) |
| **FAISS**                  | In-memory + disk     | Fast, battle-tested at Meta scale                   | No HTTP server, needs custom API       |
| **pgvector**               | PostgreSQL extension | Production-grade, SQL joins                         | Requires separate PostgreSQL instance  |
| **Qdrant**                 | Standalone container | Cloud-native, rest API                              | Extra service to maintain              |

**Recommendation:** **ChromaDB** — embedded (no separate service), pure Python, integrates with LangChain/LlamaIndex if needed later, sufficient for a single-server app.

---

### Component 4: Hybrid Query Router (Optional Enhancement)

For most queries, both systems will return relevant content. But some queries benefit more from one system than the other:

**Query type → routing hints:**

| Query Pattern                                | Preferred System        | Reason                      |
| -------------------------------------------- | ----------------------- | --------------------------- |
| "What is the Q3 revenue?" (financial data)   | PageIndex               | PDFs have structured tables |
| "Summarize slide 5 of presentation.pptx"     | Vector (slide # lookup) | Exact slide reference       |
| "Find all mentions of 'merger' in documents" | Both (keyword overlap)  | PageIndex + semantic        |
| "Compare the revenue across all sheets"      | Vector RAG              | Tabular, cross-document     |
| "What does the conclusion say?"              | PageIndex               | PDF conclusion section      |
| "List all action items from the PPT"         | Vector RAG              | Bullet points, semantic     |

**Implementation:** A lightweight LLM call to classify the query type, or keyword-based heuristics:

```python
def route_query(query: str) -> list[str]:
    """
    Returns list of systems to query: ['pageindex', 'vector'] or just ['vector'].
    Default: query both.
    """
    query_lower = query.lower()

    # Keywords suggesting PDF/PageIndex relevance
    pdf_keywords = ['report', 'section', 'chapter', 'appendix', 'footnote',
                    'figure', 'table of contents', 'abstract', 'conclusion']

    # Keywords suggesting structured data (Vector RAG)
    structured_keywords = ['sheet', 'column', 'row', 'spreadsheet', 'csv',
                           'slide', 'presentation', 'bullet points', 'action items']

    has_pdf_hint = any(kw in query_lower for kw in pdf_keywords)
    has_structured_hint = any(kw in query_lower for kw in structured_keywords)

    if has_pdf_hint and not has_structured_hint:
        return ['pageindex', 'vector']  # prioritize PageIndex
    elif has_structured_hint and not has_pdf_hint:
        return ['vector']  # skip PageIndex
    else:
        return ['pageindex', 'vector']  # query both (default)
```

**Recommendation:** Start with querying both systems always (parallel). Add the router later if you see latency or quality issues with certain query types.

---

## Part 4: Updated Architecture with Both Systems

### Storage Layout

```
backend/
├── data/
│   ├── pageindex_documents/       # existing
│   │   ├── documents.json        # existing metadata
│   │   └── {doc_id}_{filename}.pdf
│   │
│   ├── vector_documents/         # NEW
│   │   ├── documents.json        # NEW: metadata for vector docs
│   │   └── {doc_id}_{filename}.{ext}
│   │
│   └── chroma_db/                # NEW: ChromaDB persistent storage
│       └── (chroma default files)
```

### Service Architecture

```
UnifiedRAGService
├── PageIndexService (existing)
│   └── get_ready_documents()
│   └── retrieve(query) → list[RetrievedChunk] (pageindex type)
│
├── VectorRAGService (new)
│   ├── ingest(file_path, doc_type) → splits + embeds + stores
│   └── retrieve(query, top_k) → list[RetrievedChunk] (vector type)
│
└── HybridRetriever (new — the orchestrator)
    ├── retrieve_all(query) → runs both in parallel
    ├── merge(results: list[RetrievedChunk]) → unified ranked list
    └── build_context(chunks) → final prompt string
```

### API Endpoints (Frontend additions)

```
Existing:                           New Vector RAG:
GET  /project/pageindex/documents    GET  /project/vector/documents
POST /project/pageindex/documents    POST /project/vector/documents
GET  /project/pageindex/documents/{id}  GET  /project/vector/documents/{id}
DELETE /project/pageindex/documents/{id} DELETE /project/vector/documents/{id}

New unified:
GET  /project/rag/status            → {pageindex: {total, ready}, vector: {total, ready}}
```

### Frontend Additions

The `AdminDocuments` page needs a **file type filter** or **two-tab layout**:

```
┌─────────────────────────────────────────────────────────┐
│  📄 PDF Documents (PageIndex)      │  📊 Other Files (Vector RAG)  │
├─────────────────────────────────────┼──────────────────────────────┤
│  [Upload PDF]                       │  [Upload PPTX/XLSX/MD/CSV]   │
│  Doc list...                        │  Doc list...                  │
└─────────────────────────────────────┴──────────────────────────────┘
```

Or simpler — single list with a "Type" badge:

```
DocumentList (Vector RAG version)
├── filename.pdf    [PageIndex] [green]  🗑️
├── report.pptx     [Vector]   [green]  🗑️
├── data.xlsx        [Vector]   [indexing] 🗑️
└── readme.md        [Vector]   [ready]    🗑️
```

---

## Part 5: New Dependencies

```toml
# Vector RAG additions to pyproject.toml
"chromadb>=0.4.0",
"openai>=1.0.0",                    # for embeddings (already have via LiteLLM)
"python-pptx>=3.5.0",               # PPTX parsing
"pandas>=2.2.0",                     # XLSX/CSV parsing (already have in test deps)
"openpyxl>=3.1.0",                   # XLSX parsing
"beautifulsoup4>=4.12.0",           # HTML in PPTX
# Optional local embeddings (fallback if API fails):
# "sentence-transformers>=2.2.0",
```

---

## Part 6: Implementation Order

### Phase 1: Vector RAG Standalone (after PageIndex is live)

- Build `VectorRAGService` with ChromaDB
- Add file parsers (PPTX, XLSX, MD, CSV)
- Add REST API endpoints
- Extend `AdminDocuments.tsx` with Vector RAG tab
- **No changes to chat yet** — Vector RAG runs independently first

### Phase 2: Hybrid Merger (new task)

- Create `HybridRetriever` that calls both services in parallel
- Implement result merging (start with Strategy C, upgrade to Strategy A)
- Replace `build_rag_context()` in `auth_test.py` with `hybrid_retriever.retrieve()`
- Unified context always includes chunks from both systems

### Phase 3: Query Router (optional)

- Lightweight query classification
- Skip irrelevant system when query type is clear
- Reduces latency for targeted queries

---

## Part 7: Potential Pitfalls & Mitigations

| Pitfall                                                                 | Mitigation                                                                                                |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Latency** — running two retrievers doubles query time                 | Parallel execution (ThreadPoolExecutor), both retrievers run concurrently                                 |
| **Context overflow** — combined chunks from 5+ docs exceed token budget | Hard cap: top-K per system (e.g., top-3 PageIndex + top-5 Vector = 8 chunks max), sort by score, truncate |
| **Conflicting answers** — PageIndex says X, Vector says Y               | LLM-as-Reranker (Strategy A) lets LLM pick the authoritative source and flag contradictions               |
| **Embedding model is down**                                             | Fallback to keyword search (BM25) within stored chunks, or route to PageIndex only                        |
| **Large XLSX files**                                                    | Chunking by row groups with header context, cap at 10K rows per doc                                       |
| **PPTX with images**                                                    | Extract text only (images ignored in v1)                                                                  |
| **CSV encoding issues**                                                 | Detect encoding with `chardet`, fallback to UTF-8                                                         |
| **Missing metadata in chunks**                                          | Always include source doc name, sheet/slide number, row range in chunk metadata                           |
| **Memory growth** — ChromaDB grows unbounded                            | Implement doc deletion (already in plan), periodic cleanup job                                            |

---

## Summary: Key Design Decisions

| Decision               | Choice                                    | Rationale                                                   |
| ---------------------- | ----------------------------------------- | ----------------------------------------------------------- |
| **Retrieval strategy** | Parallel + merge                          | Maximizes coverage, both systems contribute their strengths |
| **Merge method**       | LLM-as-Reranker (Strategy A)              | Best quality, marginal extra cost justified                 |
| **Chunking**           | Semantic/file-structure-aware             | Preserves document semantics (slide, sheet, header)         |
| **Vector DB**          | ChromaDB                                  | Zero-config, embedded, sufficient for app scale             |
| **Embedding model**    | `text-embedding-3-small` via existing API | No new dependencies, consistent with current setup          |
| **Query routing**      | Disabled initially                        | Simplicity first, add when latency is measurable problem    |
| **Context budget**     | 6K tokens (same as PageIndex)             | Shared budget across both systems                           |
| **File routing**       | Extension-based                           | Simple, reliable, no ML needed                              |
