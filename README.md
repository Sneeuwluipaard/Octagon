## Запуск FastAPI

### 1. Установить зависимости
```bash
pip install -r requirements.txt
```

### 2. Подготовить .env
Файл `venv/.env` должен содержать `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.

### 3. Заполнить БД начальными данными (один раз)
```bash
python -m init_db
```

### 4. Запустить сервер
```bash
uvicorn app.main:app --reload
```

### 5. Открыть
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc:      http://127.0.0.1:8000/redoc
- Health:     http://127.0.0.1:8000/health

### Примеры запросов
```bash
# Список книг
curl http://127.0.0.1:8000/books

# Фильтр по категории
curl "http://127.0.0.1:8000/books?category_id=1"

# Создать категорию
curl -X POST http://127.0.0.1:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"title":"Детективы"}'

# Создать книгу
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Шерлок Холмс","price":500.0,"category_id":1}'
```

### Скриншоты работы API
См. папку [`examples/`](examples/).