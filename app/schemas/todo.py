from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class TodoRequest(BaseModel):
    title: str
    content: str


class TodoResponse(BaseModel):
    id: UUID
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
