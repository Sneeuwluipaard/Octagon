from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import books, categories
from app.db.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """При старте приложения гарантируем наличие таблиц в БД."""
    init_db()
    yield


app = FastAPI(
    title="Books Catalog API",
    version="1.0.0",
    description="API для управления каталогом книг и категорий (FastAPI + SQLAlchemy + PostgreSQL).",
    lifespan=lifespan,
)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["health"])
def health():
    """Проверка, что сервис жив."""
    return {"status": "ok"}