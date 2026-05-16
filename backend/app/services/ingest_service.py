# Ingest service
# HIEP viet lai Ingest service logic
from app.schemas.ingest import IngestRequest, IngestResponse
from ai_engine.vector_db import VectorDB


class IngestService:
    def __init__(self):
        self.vector_db = VectorDB()

    def ingest_document(self, request: IngestRequest) -> IngestResponse:
        try:
            # Lấy nội dung cần index
            content = request.content

            if not content and request.file_path:
                with open(request.file_path, "r", encoding="utf-8") as f:
                    content = f.read()

            if not content:
                return IngestResponse(
                    success=False,
                    message="Không có nội dung để index",
                )

            # Đưa vào vector DB (Qdrant)
            chunks_count = self.vector_db.add_documents(
                content=content,
                metadata=request.metadata or {},
            )

            return IngestResponse(
                success=True,
                message=f"Đã index thành công",
                chunks_indexed=chunks_count,
            )

        except Exception as e:
            return IngestResponse(
                success=False,
                message=f"Lỗi khi index: {str(e)}",
            )