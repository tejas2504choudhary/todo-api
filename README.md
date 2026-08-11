# Todo API

A small, clean **FastAPI** web service for managing to-do items. Built as a
ready-to-use starting point — swap the in-memory store for a real database
when you're ready.

## Features

- CRUD endpoints for todos (`create`, `list`, `get`, `update`, `delete`)
- Auto-generated interactive docs via Swagger UI (`/docs`) and ReDoc (`/redoc`)
- Request/response validation with Pydantic
- Unit tests with `pytest` + `httpx`
- Linting with `ruff`
- CI pipeline with GitHub Actions
- Dockerfile for containerized deployment

## Project structure

```
todo-api/
├── app/
│   ├── main.py          # FastAPI app instance & health routes
│   ├── models.py        # Pydantic models
│   ├── storage.py       # In-memory data store
│   └── routers/
│       └── todos.py     # /todos CRUD endpoints
├── tests/
│   └── test_todos.py
├── .github/workflows/ci.yml
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── README.md
```

## Getting started

### 1. Clone and set up a virtual environment

```bash
git clone https://github.com/<your-username>/todo-api.git
cd todo-api
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 3. Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs
at `http://127.0.0.1:8000/docs`.

### 4. Run tests

```bash
pytest -v
```

### 5. Lint

```bash
ruff check .
```

## API endpoints

| Method | Path          | Description         |
|--------|---------------|----------------------|
| GET    | `/health`     | Health check         |
| GET    | `/todos`      | List all todos       |
| POST   | `/todos`      | Create a todo        |
| GET    | `/todos/{id}` | Get a single todo    |
| PATCH  | `/todos/{id}` | Update a todo        |
| DELETE | `/todos/{id}` | Delete a todo        |

### Example: create a todo

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "description": "2% please"}'
```

## Running with Docker

```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

## Next steps

- Swap `app/storage.py` for a real database (e.g. SQLModel + PostgreSQL)
- Add authentication (e.g. OAuth2 / JWT)
- Add pagination and filtering to `GET /todos`
- Add rate limiting for production use

## License

MIT — see [LICENSE](LICENSE).
