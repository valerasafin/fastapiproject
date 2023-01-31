# FastAPI
from fastapi import FastAPI, Depends
from fastapi.routing import APIRouter
from app import schemas, models, db
from app.db import engine, session_local
# Uvicorn
import uvicorn
# SQL Alchemy
from sqlalchemy.orm import session


# create instance for the app
app = FastAPI()

# create instance for the router
main_api_router = APIRouter()
app.include_router(main_api_router)

# create database models
models.Base.metadata.create_all(engine)


# create db_connect
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


# create function for manual book creation in FastAPI/docs
@app.post('/library')
async def create_book(request: schemas.Book, db: session = Depends(get_db)):
    new_book = models.Library(
        title=request.title,
        author=request.author,
        description=request.description,
        in_stock=request.in_stock)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get('/')
async def get_book(db: session = Depends(get_db)):
    books = db.query(models.Library).all()
    return books, "hello"


if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host='127.0.0.1', port=8000)

