from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookResponse])
def list_books(
    skip: int = 0,
    limit: int = 100,
    category_id: int | None = Query(None, description="Фильтр по ID категории"),
    db: Session = Depends(get_db),
):
    """Список книг. Поддерживает ?category_id= для фильтрации."""
    if category_id is not None:
        return crud.get_books_by_category(db, category_id=category_id)
    return crud.get_books(db, skip=skip, limit=limit)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    """Создать книгу. Проверяем существование категории (если указана)."""
    if payload.category_id is not None and not crud.get_category(db, payload.category_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with id={payload.category_id} does not exist",
        )
    return crud.create_book(
        db,
        title=payload.title,
        price=payload.price,
        category_id=payload.category_id,
        description=payload.description,
        url=payload.url or "",
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, payload: BookUpdate, db: Session = Depends(get_db)):
    """Обновить книгу. Обновляются только переданные поля."""
    if payload.category_id is not None and not crud.get_category(db, payload.category_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category with id={payload.category_id} does not exist",
        )
    book = crud.update_book(
        db,
        book_id=book_id,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        url=payload.url,
        category_id=payload.category_id,
    )
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None