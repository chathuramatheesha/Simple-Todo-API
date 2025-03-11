from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Path
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.core.dependencies import get_db
from app.db import crud
from app.schemas.todo import TodoRequest, TodoResponse

router = APIRouter()


@router.post("/", response_model=TodoResponse)
async def create_todo(request: TodoRequest, db: AsyncSession = Depends(get_db)):
    result = await crud.create_todo_db(request, db)
    if result is None:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return result


@router.get("/all")
async def get_all_todos(db: AsyncSession = Depends(get_db)):
    result = await crud.get_todos_db(db)
    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Todos found"
        )
    return result


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo_by_id(
    todo_id: UUID = Path(Ellipsis), db: AsyncSession = Depends(get_db)
):
    result = await crud.get_todo_by_id_db(todo_id, db)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo is not found"
        )
    return result
