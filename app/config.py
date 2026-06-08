from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://rag:rag@localhost:5432/ragdoc"
    rabbitmq_url: str = "amqp://guest:guest@localhost:5672//"

    embedding_model: str = "BAAI/bge-m3"
    embedding_dim: int = 1024
    reranker_model: str = "BAAI/bge-reranker-v2-m3"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"

    top_k_retrieve: int = 20
    top_k_rerank: int = 5
    chunk_target_tokens: int = 400


settings = Settings()
