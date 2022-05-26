import os
from typing import Union

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema.index import Author as SchemaAuthor
from schema.index import Book as SchemaBook
from schema.index import User, external_data

from models.models import Author as ModelAuthor
from models.models import Book as ModelBook

load_dotenv(".env")

# Initialize Server
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
def root() -> User:
    user = User(**external_data)
    return user.dict()


@app.post("/book/", response_model=SchemaBook)
async def create_book(book: SchemaBook):
    db_book = ModelBook(**book.dict())
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get("/books/")
async def book():
    book = db.session.query(ModelBook).all()
    return book


@app.post("/author/", response_model=SchemaAuthor)
async def create_author(author: SchemaAuthor):
    db_author = ModelAuthor(**author.dict())
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.get("/author/")
async def author():
    author = db.session.query(ModelAuthor).all()
    return author


@app.get("/items/{user_id}")
def read_item(user_id: Union[int, str]) -> dict:
    if isinstance(user_id, int):
        user_id = str(user_id)
    return {"user_id": user_id}
