# Celery tasks
# HIEP viet lai Celery background tasks
from celery import Celery

from app.core.config import settings

# Dùng config thay vì hardcode URL
app = Celery(
    "rag_solution",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Ho_Chi_Minh",
    enable_utc=True,
)


@app.task(bind=True, max_retries=3)
def process_document(self, content: str, metadata: dict = {}):
    """
    Task xử lý ingest tài liệu vào vector DB bất đồng bộ.
    Gọi từ ingest endpoint khi tài liệu lớn.
    """
    try:
        from ai_engine.vector_db import VectorDB
        vdb = VectorDB()
        chunks_count = vdb.add_documents(content=content, metadata=metadata)
        return {"success": True, "chunks_indexed": chunks_count}
    except Exception as exc:
        # Tự retry sau 5s nếu thất bại
        raise self.retry(exc=exc, countdown=5)


@app.task(bind=True, max_retries=3)
def generate_embedding(self, text: str):
    """
    Task tạo embedding cho một đoạn text.
    Dùng khi cần tạo embedding riêng lẻ không qua ingest.
    """
    try:
        from ai_engine.vector_db import VectorDB
        vdb = VectorDB()
        embedding = vdb.embed_text(text)
        return {"success": True, "embedding": embedding}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)