from fastapi.testclient import TestClient

from app.main import app
from app.storage import store

client = TestClient(app)


def setup_function() -> None:
    """Reset in-memory store before each test for isolation."""
    store._todos.clear()
    store._next_id = 1


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_todo() -> None:
    create_response = client.post("/todos", json={"title": "Buy milk"})
    assert create_response.status_code == 201
    todo = create_response.json()
    assert todo["title"] == "Buy milk"
    assert todo["completed"] is False

    get_response = client.get(f"/todos/{todo['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Buy milk"


def test_list_todos() -> None:
    client.post("/todos", json={"title": "Task 1"})
    client.post("/todos", json={"title": "Task 2"})

    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_todo() -> None:
    created = client.post("/todos", json={"title": "Task"}).json()

    response = client.patch(f"/todos/{created['id']}", json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_todo() -> None:
    created = client.post("/todos", json={"title": "Task"}).json()

    delete_response = client.delete(f"/todos/{created['id']}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/todos/{created['id']}")
    assert get_response.status_code == 404


def test_get_nonexistent_todo_returns_404() -> None:
    response = client.get("/todos/999")
    assert response.status_code == 404


def test_create_todo_requires_title() -> None:
    response = client.post("/todos", json={})
    assert response.status_code == 422
