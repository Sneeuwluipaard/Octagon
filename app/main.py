from app.db.db import SessionLocal
from app.db import crud


def display_catalog():
    """Читает категории и книги из БД и выводит их на экран."""
    db = SessionLocal()
    try:
        categories = crud.get_categories(db)
        if not categories:
            print("Каталог пуст. Сначала запустите python -m app.init_db")
            return

        print("=" * 50)
        print("КАТАЛОГ КНИГ ИЗ БАЗЫ ДАННЫХ POSTGRESQL")
        print("=" * 50)

        for category in categories:
            print(f"\n[Категория #{category.id}]: {category.title}")
            print("-" * 50)

            books = crud.get_books_by_category(db, category_id=category.id)
            if not books:
                print("  В этой категории пока нет книг.")
                continue

            for book in books:
                print(f"  * {book.title} (ID: {book.id})")
                print(f"    Цена: {book.price} руб.")
                print(f"    Описание: {book.description}")
                print(f"    URL: '{book.url}'")
                print()

    finally:
        db.close()


if __name__ == "__main__":
    display_catalog()
