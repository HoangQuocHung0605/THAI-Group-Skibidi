# Configuration module
# HIEPviet lai Config
from pydantic_settings import BaseSettings
from functools import lru_cache
 
 
class Settings(BaseSettings):
    # App
    APP_NAME: str = "RAG Solution"
    DEBUG: bool = False
 
    # PostgreSQL
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@postgres:5432/rag_db"
 
    # Redis
    REDIS_URL: str = "redis://redis:6379"
 
    # Celery (dùng Redis làm broker)
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/0"
 
    # Qdrant
    QDRANT_URL: str = "http://qdrant:6333"
    QDRANT_COLLECTION: str = "documents"
 
    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Google Gemini
    GOOGLE_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-flash-latest"
    GOOGLE_EMBEDDING_MODEL: str = "models/gemini-embedding-001"
 
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
 
 
@lru_cache()
def get_settings() -> Settings:
    return Settings()
 
 
settings = get_settings()