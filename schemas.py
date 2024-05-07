from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class BookSchemas(BaseModel):
    # id: Optional[int] = None/
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mood = True


# class RequestBook(BaseModel):
#     parameter: BookSchemas = Field(...)


class Response(GenericModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]
