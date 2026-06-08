# rag_engine — local RAG engine over internal docs

Indexes Markdown / PDF / source code from a repository and answers questions
with citations back to the source. Everything runs locally.

## Architecture

```
                        ┌─────────────┐
  upload ──▶ FastAPI ──▶  RabbitMQ   ──▶ Celery worker
            (/ingest)   └─────────────┘        │
                                               ▼
                                   parse → chunk → embed (bge-m3)
                                               │
                                               ▼
                                   PostgreSQL + pgvector (HNSW)
                                               ▲
   question ─▶ FastAPI (/ask) ─▶ vector search │
                                  → rerank (bge-reranker)
                                  → Ollama (qwen3) ─▶ cited answer
```

- **API / queue:** FastAPI, Celery, RabbitMQ
- **Storage / vectors:** PostgreSQL + pgvector (HNSW index, cosine)
- **Embeddings:** `bge-m3` via sentence-transformers (multilingual, dense + sparse)
- **Reranker:** `bge-reranker-v2-m3` cross-encoder for precision
- **LLM:** `qwen3:8b` via Ollama (swap to `gpt-oss:20b` on a 16GB+ GPU box)

## Quickstart

```bash
cp .env.example .env
docker compose up -d db rabbitmq
pip install -e ".[dev]"
ollama pull qwen3:8b
uvicorn app.main:app --reload
celery -A app.celery.celery_app celery -l info
```

Health check: `curl localhost:8000/health`

## Status

- [x] Week 0 — skeleton: API, queue, DB schema, CI, Docker
- [ ] Week 1 — ingestion pipeline (parse → chunk → embed, idempotent)
- [ ] Week 2 — retrieve → rerank → generate with citations + hybrid search
- [ ] Week 3 — eval harness + Streamlit UI

## Decisions & tradeoffs

- **Why structure-aware chunking** over fixed-size: …
- **Why a reranker** on top of dense search: …
- **HNSW vs IVFFlat** for the pgvector index: …
- **Why local models** (bge-m3 / qwen3) instead of an API: …
- **How retrieval quality is measured** (see `/eval`): …
