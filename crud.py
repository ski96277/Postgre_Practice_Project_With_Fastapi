from sqlalchemy.orm import Session
from models import Book
from schemas import BookSchemas


def get_book(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Book).offset(skip).limit(limit=limit).all()


def get_book_bby_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchemas):
    print(f"hello input books = {book}")
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)

    return _book
