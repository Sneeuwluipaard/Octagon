from pydantic import BaseModel, ConfigDict, Field


# ===================== CATEGORY =====================

class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ===================== BOOK =====================

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    price: float = Field(..., ge=0)
    url: str = ""
    category_id: int | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    """Все поля опциональны — частичное обновление."""
    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    price: float | None = Field(None, ge=0)
    url: str | None = None
    category_id: int | None = None


class BookResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    price: float
    url: str | None = None
    # В модели атрибут называется `category`, а в API по заданию — `category_id`.
    # validation_alias читает obj.category при from_attributes=True,
    # а на выходе поле сериализуется как category_id (по имени поля).
    category_id: int | None = Field(default=None, validation_alias="category")

    model_config = ConfigDict(from_attributes=True)