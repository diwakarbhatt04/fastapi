from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum


app = FastAPI()

class Items(BaseModel):
    name : str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/postapi")
def get_json(item: Items):
    return item.name

handler = Mangum(app)