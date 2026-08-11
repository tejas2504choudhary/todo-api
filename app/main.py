from fastapi import FastAPI

from app.routers import todos

app = FastAPI(
    title="Todo API",
    description="A simple task management API built with FastAPI",
    version="0.1.0",
)

app.include_router(todos.router)


@app.get("/", tags=["health"])
def read_root() -> dict:
    """Basic health-check / welcome endpoint."""
    return {"message": "Todo API is running", "docs": "/docs"}


@app.get("/health", tags=["health"])
def health_check() -> dict:
    """Health-check endpoint for monitoring / uptime checks."""
    return {"status": "ok"}
