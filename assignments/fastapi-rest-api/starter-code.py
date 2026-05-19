from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items: List[Item] = [
    Item(id=1, name="Notebook", description="A ruled notebook", price=4.99),
    Item(id=2, name="Pen", description="Blue ink pen", price=1.50),
]

@app.get("/items", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# TODO: Add POST, PUT, and DELETE endpoints below to complete the REST API.
# Example:
# @app.post("/items", response_model=Item)
# def create_item(item: Item):
#     ...

# Run this app with: uvicorn starter-code:app --reload
