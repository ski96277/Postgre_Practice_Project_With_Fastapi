from sqlalchemy import Column, Integer, String

from config import Base


class Book(Base):
    __tablename__ = 'Book'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    description = Column(String)
