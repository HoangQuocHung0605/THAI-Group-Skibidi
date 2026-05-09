# History endpoint
# HIEP viet lai History API
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db          # ← dùng Depends, KHÔNG dùng SessionLocal trực tiếp
from app.schemas.message import MessageResponse
from app.services.history_service import HistoryService

router = APIRouter(prefix="/api/history", tags=["history"])


@router.get("/", response_model=List[MessageResponse])
def get_history(
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),            # ← FastAPI tự inject db session
):
    # Thêm .order_by để sắp xếp theo thời gian giảm dần
    service = HistoryService()
    return service.get_history(db, limit=limit, offset=offset)


@router.delete("/")
def delete_history(db: Session = Depends(get_db)):
    service = HistoryService()
    success = service.delete_history(db)
    return {"success": success, "message": "Đã xóa lịch sử" if success else "Xóa thất bại"}