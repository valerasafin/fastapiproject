import requests
from fastapi import FastAPI, APIRouter
import uvicorn
import json

app = FastAPI()


URL = 'http://127.0.0.1:8000/library'


class Book(object):
    title: str
    author: str
    description: str
    in_stock: bool

    def __init__(self, id, title, author, description, in_stock):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.in_stock = in_stock

    def __str__(self):
        return self.title+' '+self.author+' '+self.description


@app.get('/')
async def get_book():
    r = requests.get(URL)
    k = r.text
    j = json.loads(k)
    list = []
    for i in j:
        list.append(str(Book(**i)))
    return list

uvicorn.run(app, host='127.0.0.1', port=8033)

