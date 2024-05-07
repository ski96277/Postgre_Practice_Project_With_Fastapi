from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy import null

from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchemas, Response

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: BookSchemas, db: Session = Depends(get_db)):
    crud.create_book(db=db, book=request)

    return Response(code=200,
                    status="ok",
                    message="Book created successfully",
                    result = null
                    ).dict(exclude_none=True)


@router.get('/')
async def get(db: Session = Depends(get_db)):
    _book = crud.get_book(db=db, skip=0, limit=100)
    return Response(code=200,
                    status="ok",
                    message="Successfully fetch all data",
                    result=_book
                    ).dict(exclude_none=True)
