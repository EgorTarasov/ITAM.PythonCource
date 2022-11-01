"""
создание виртуального окружения

python3 -m venv <dir>

dir - путь по которому будет создано виртуальное окружение


активация виртуального окружения
linux / mac
- source <dir>/bin/activate

windows 
- .\venv\Scripts\activate

подробнее про виртуальное окружение можно почитать тут:
https://docs.python.org/3/library/venv.html

утановка fastApi
- pip install fastapi 
- pip install uvicorn

официальная документация:
https://fastapi.tiangolo.com

"""

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Book(BaseModel):
    id: int
    name: str


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.post("/")
def save_book(book: Book):
    print(book)
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(f)
    data[book.id] = book.name
    with open("data.json", "w", endcoding="utf-8") as file:
        json.dump(data, file)
    return "saved"


@app.get("/{book_id}")
def get_book(book_id: int):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(f)

    return {book_id: data[book_id]}


import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
