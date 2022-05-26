from fastapi import FastAPI
from typing import Union

# Initialize Server
app = FastAPI()

# Decorator (does something to the method under it)
@app.get("/")
def root():
    return {"message": "Hello, world!"}

@app.get("/items/{user_id}")
def read_item(user_id: Union[int, str]):
    if isinstance(user_id, int):
        user_id = str(user_id)
    return {"user_id": user_id}