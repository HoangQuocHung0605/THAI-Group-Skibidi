# Worker database session
# Celery worker cần session riêng, không dùng Depends(get_db) như FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,         # worker cần ít connection hơn API
    max_overflow=10,
)

WorkerSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_worker_db():
    """
    Dùng với 'with' statement trong Celery task:
        with get_worker_db() as db:
            db.query(...)
    """
    db = WorkerSession()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()