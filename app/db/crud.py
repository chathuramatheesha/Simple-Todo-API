from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from typing import Sequence

from app.schemas.todo import TodoRequest
from app.db.models import Todo


async def create_todo_db(request: TodoRequest, db: AsyncSession) -> Todo:
    new_todo = Todo(title=request.title, content=request.content)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


async def get_todo_by_id_db(todo_id: UUID, db: AsyncSession) -> Todo | None:
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    return result.scalar_one_or_none()


async def get_todos_by_title(
    todo_title: str, db: AsyncSession
) -> Sequence[Todo] | None:
    result = await db.execute(select(Todo).where(Todo.title.like(f"%{todo_title}%")))
    return result.scalars().all()


async def get_todos_db(db: AsyncSession) -> Sequence[Todo] | None:
    result = await db.execute(select(Todo))
    return result.scalars().all()
