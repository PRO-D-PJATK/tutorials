# Vector Search and RAG Engineering

Build a minimal retrieval-augmented generation (RAG) or semantic search pipeline and evaluate retrieval quality.

**Points: 15**

---

## Task

1. **Corpus (3 pts)** — Assemble a small document set (public articles, docs, FAQ). Chunk text with a documented strategy.
2. **Embeddings & index (5 pts)** — Embed chunks (open model or API) and index with FAISS / Chroma / similar. Support top-k similarity search.
3. **RAG or search app (3 pts)** — Either:
   - answer questions with retrieved context + an LLM, **or**
   - return ranked passages for a query (search-only is acceptable).
4. **Evaluation (4 pts)** — Create a tiny gold set (≥10 queries). Report Recall@k / MRR (or a judged relevance score). Discuss failure cases (bad chunks, ambiguous queries).

## Deliverables

- Indexing + query code
- Evaluation results on the gold set
- Note on latency, cost, and hallucination risk (if generation is used)
