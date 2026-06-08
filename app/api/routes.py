from fastapi import APIRouter, UploadFile
from pydantic import BaseModel

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


class AskRequest(BaseModel):
    question: str


class Source(BaseModel):
    document: str
    chunk_id: int
    score: float
    snippet: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


@router.post("/ingest")
async def ingest(file: UploadFile) -> dict[str, str]:
    """Accept a file and hand it to the indexing queue.

    TODO (week 1):
      1. Save the uploaded bytes somewhere the celery can read.
      2. Enqueue app.celery.tasks.index_document.delay(path).
      3. Return a task id the caller can poll.
    """
    raise NotImplementedError("Week 1: wire up the ingestion task")


@router.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest) -> AskResponse:
    """Retrieve -> rerank -> generate a cited answer.

    TODO (week 2):
      1. retrieval.search(req.question) -> candidate chunks
      2. retrieval.rerank(question, candidates) -> top chunks
      3. llm.answer(question, top_chunks) -> answer + sources
    """
    raise NotImplementedError("Week 2: implement the retrieve/rerank/generate flow")
