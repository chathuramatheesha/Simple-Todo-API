import uuid
from sqlalchemy import Column, Integer, String, UUID, DateTime
from datetime import datetime, timezone

from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, primary_key=True)
    title = Column(String(30))
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
