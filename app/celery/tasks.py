from app.celery.celery_app import celery_app


@celery_app.task
def index_document(path: str) -> dict:
    """Parse -> chunk -> embed -> upsert. The heart of the ingestion pipeline.

    TODO (week 1):
      1. Detect type (.md / .pdf / code) and extract text.
      2. Chunk it (structure-aware: headings for Markdown, functions for code).
      3. Hash each chunk; skip chunks whose hash already exists (idempotency).
      4. embeddings.embed_texts(new_chunks) and upsert into the chunks table.
    """
    raise NotImplementedError("Week 1: implement the ingestion pipeline")
