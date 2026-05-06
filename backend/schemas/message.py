from pydantic import BaseModel

class MessageCreate(BaseModel):
    question: str

class MessageResponse(BaseModel):
    id: int
    question: str
    answer: str

    class Config:
        from_attributes = True