from fastapi import APIRouter, HTTPException, status

from app.models import Todo, TodoCreate, TodoUpdate
from app.storage import store

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("", response_model=list[Todo])
def list_todos() -> list[Todo]:
    return store.list()


@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: TodoCreate) -> Todo:
    return store.create(todo_in)


@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    todo = store.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: TodoUpdate) -> Todo:
    todo = store.update(todo_id, todo_in)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> None:
    deleted = store.delete(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
