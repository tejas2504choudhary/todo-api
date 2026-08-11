"""Simple in-memory storage for todos.

This keeps the demo dependency-free. Swap this out for a real database
(e.g. SQLModel + SQLite/Postgres) when you're ready to persist data.
"""

from app.models import Todo, TodoCreate, TodoUpdate


class TodoStore:
    def __init__(self) -> None:
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def list(self) -> list[Todo]:
        return list(self._todos.values())

    def get(self, todo_id: int) -> Todo | None:
        return self._todos.get(todo_id)

    def create(self, todo_in: TodoCreate) -> Todo:
        todo = Todo(id=self._next_id, **todo_in.model_dump())
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def update(self, todo_id: int, todo_in: TodoUpdate) -> Todo | None:
        existing = self._todos.get(todo_id)
        if existing is None:
            return None
        updated = existing.model_copy(
            update=todo_in.model_dump(exclude_unset=True)
        )
        self._todos[todo_id] = updated
        return updated

    def delete(self, todo_id: int) -> bool:
        return self._todos.pop(todo_id, None) is not None


# Single shared instance used by the app (fine for a demo / single worker)
store = TodoStore()
