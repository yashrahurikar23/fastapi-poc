from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None

@app.get("/")
def get_items():
  return { 
    "data": []
  }

@app.get("/items/{item_id}")
def get_item():
  return { 
    "data": {}
  }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return { 
    "data": {
      "item_name": item.name,
      "item_id": item_id
    }
  }


