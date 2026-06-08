from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO (week 1): warm up the embedding model here
    yield


app = FastAPI(title="rag_engine", version="0.1.0", lifespan=lifespan)
app.include_router(router)
