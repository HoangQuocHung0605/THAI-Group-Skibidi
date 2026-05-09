# History service
# HIEP viet lai History service logic
from sqlalchemy.orm import Session
from typing import List

from app.models.message import Message
from app.schemas.message import MessageResponse


class HistoryService:

    def get_history(
        self,
        db: Session,
        limit: int = 20,
        offset: int = 0,
    ) -> List[MessageResponse]:
        messages = (
            db.query(Message)
            .order_by(Message.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
        return [MessageResponse.from_orm(m) for m in messages]

    def delete_history(self, db: Session) -> bool:
        try:
            db.query(Message).delete()
            db.commit()
            return True
        except Exception:
            db.rollback()
            return False