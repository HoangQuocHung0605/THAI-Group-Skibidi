# Ingest schema
# HIEP viet lai Ingest schema
from pydantic import BaseModel
from typing import Optional


class IngestRequest(BaseModel):
    file_path: Optional[str] = None   # path tới file đã upload
    content: Optional[str] = None     # hoặc truyền thẳng nội dung text
    metadata: Optional[dict] = {}


class IngestResponse(BaseModel):
    success: bool
    message: str
    chunks_indexed: Optional[int] = None  # số đoạn văn bản đã đưa vào vector DB