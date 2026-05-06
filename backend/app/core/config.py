from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Kết nối Postgres (Lưu tại data/postgres)
    DATABASE_URL: str = "postgresql://user:password@db:5432/rag_db"
    # Kết nối Redis cho Background Task & Cache
    REDIS_URL: str = "redis://redis:6379/0"
    
settings = Settings()