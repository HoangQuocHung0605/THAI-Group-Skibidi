# Database connection module
# HIEP viet lai database up
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings


# Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,   # tự reconnect nếu connection chết
    pool_size=10,
    max_overflow=20,
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Base class cho tất cả models (dùng ở app/models/)
class Base(DeclarativeBase):
    pass


# Dependency inject vào FastAPI endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 