from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True)

    # Связь с таблицей книг (обратная ссылка)
    books = relationship("Book", back_populates="category_rel", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category(id={self.id}, title='{self.title}')>"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    url = Column(String(500), nullable=True, default="")
    
    # Внешний ключ, ссылающийся на таблицу categories
    category = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)

    # Связь с объектом категории
    category_rel = relationship("Category", back_populates="books")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', price={self.price})>"
