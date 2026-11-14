from sqlalchemy.orm import Session
from app.db.models import Category, Book


def create_category(db: Session, title: str) -> Category:
    """Создает новую категорию."""
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int) -> Category | None:
    """Получает категорию по её ID."""
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100) -> list[Category]:
    """Получает список всех категорий."""
    return db.query(Category).offset(skip).limit(limit).all()


def update_category(db: Session, category_id: int, new_title: str) -> Category | None:
    """Обновляет название категории."""
    db_category = get_category(db, category_id)
    if db_category:
        db_category.title = new_title
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int) -> bool:
    """Удаляет категорию по ID. Возвращает True, если удаление прошло успешно."""
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False



def create_book(
    db: Session,
    title: str,
    price: float,
    category_id: int | None = None,
    description: str | None = None,
    url: str = ""
) -> Book:
    """Создает новую книгу."""
    db_book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int) -> Book | None:
    """Получает книгу по её ID."""
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    """Получает список всех книг."""
    return db.query(Book).offset(skip).limit(limit).all()


def get_books_by_category(db: Session, category_id: int) -> list[Book]:
    """Получает все книги определенной категории."""
    return db.query(Book).filter(Book.category == category_id).all()


def update_book(
    db: Session,
    book_id: int,
    title: str | None = None,
    description: str | None = None,
    price: float | None = None,
    url: str | None = None,
    category_id: int | None = None
) -> Book | None:
    """Обновляет данные книги (обновляются только переданные поля)."""
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    if title is not None:
        db_book.title = title
    if description is not None:
        db_book.description = description
    if price is not None:
        db_book.price = price
    if url is not None:
        db_book.url = url
    if category_id is not None:
        db_book.category = category_id

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """Удаляет книгу по ID. Возвращает True, если удаление прошло успешно."""
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
