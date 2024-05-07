from fastapi import FastAPI

import models
from config import engine

from router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Postgre Practice")

app.include_router(router, prefix='/book', tags=['Book'])


@app.get("/")
def get_all_notes():
    return {"Notes": [{'title': 'test notes'}]}
