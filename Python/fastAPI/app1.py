from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = [
    
]

class Item(BaseModel):
    id: int
    name: str
    price: int
    is_offer: Union[bool, None] = None

@app.get("/items/")
def get_all(name:Union[str, None]=None):
    if name:
        try:
            it = [val for val in data if val.name == name]
            return it[0]
        except IndexError:
            return {"Info": "No Data Found"}
    else:
        return {"data":data}

@app.get("/items/{item_id}")
def get(item_id:int, query:Union[str, None] = None):
    try:
        items = [val for val in data if val.id == item_id]
        return items[0]
    except IndexError:
        return {"Info": "No Data Found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, items: Item):
    for index, val in enumerate(data):
        if val.id == item_id:
            data[index]=items
    return {"Message":"Updated"}

@app.post('/items/')
def post_item(items: Item):
    data.append(items)
    return {"item_id":items.id, "item_name":items.name}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    try:
        items = [data.pop(index) for index, val in enumerate(data) if val.id == item_id]
        return {"Message":f"item \'{items[0].name}\' is deleted successfully"}
    except IndexError:
        return {"Info": "No Data Found"}



