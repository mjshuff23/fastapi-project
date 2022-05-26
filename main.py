from typing import Union

from fastapi import FastAPI

from models.test import User, external_data

# Initialize Server
app = FastAPI()


# Decorator (does something to the method under it)
@app.get("/")
def root() -> User:
    user = User(**external_data)
    return user.dict()


@app.get("/items/{user_id}")
def read_item(user_id: Union[int, str]) -> dict:
    if isinstance(user_id, int):
        user_id = str(user_id)
    return {"user_id": user_id}
