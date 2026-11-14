from app.db.db import SessionLocal, init_db
from app.db import crud


def seed_data():
    """Создает таблицы и заполняет их начальными данными."""
    init_db()
    
    db = SessionLocal()
    try:
        existing_categories = crud.get_categories(db)
        if existing_categories:
            print("База данных уже содержит данные. Инициализация пропущена.")
            return

        cat_fiction = crud.create_category(db, title="Научная фантастика")
        cat_programming = crud.create_category(db, title="Программирование и IT")
        print(f"Добавлены категории: '{cat_fiction.title}', '{cat_programming.title}'")


        crud.create_book(
            db=db,
            title="Дюна",
            description="Эпический научно-фантастический роман Фрэнка Герберта о пустынной планете Арракис.",
            price=890.00,
            category_id=cat_fiction.id,
            url = "www.imgur.com/a/G6rU8"
        )
        crud.create_book(
            db=db,
            title="Задача трех тел",
            description="Роман Лю Цысиня о первом контакте человечества с инопланетной цивилизацией.",
            price=750.50,
            category_id=cat_fiction.id,
            url = "www.imgur.com/a/G6rU8"
        )
        crud.create_book(
            db=db,
            title="Автостопом по галактике",
            description="Юмористический фантастический роман Дугласа Адамса.",
            price=620.00,
            category_id=cat_fiction.id,
            url = "www.imgur.com/a/G6rU8"
        )


        crud.create_book(
            db=db,
            title="Чистый код",
            description="Создание, анализ и рефакторинг. Руководство от Роберта Мартина.",
            price=1450.00,
            category_id=cat_programming.id,
            url = "www.imgur.com/a/G6rU8"
        )
        crud.create_book(
            db=db,
            title="Грокаем алгоритмы",
            description="Иллюстрированное пособие для программистов и любопытствующих от Адитьи Бхаргавы.",
            price=1190.00,
            category_id=cat_programming.id,
            url = "www.imgur.com/a/G6rU8"
        )
        crud.create_book(
            db=db,
            title="Изучаем Python",
            description="Фундаментальное руководство по языку Python от Марка Лутца.",
            price=2300.00,
            category_id=cat_programming.id,
            url = "www.imgur.com/a/G6rU8"
        )

        print("Книги успешно добавлены в базу данных!")
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
