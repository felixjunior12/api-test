from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from db.db import init_db_pool, close_db_pool
from routers import person_router

app = FastAPI()
app.include_router(person_router.router)

@app.on_event("startup")
async def startup():
    await init_db_pool(app)

@app.on_event("shutdown")
async def shutdown():
    await close_db_pool()

@app.get("/")
def index():
    return "Hello, World1!"


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class DB_manager:
    def __init__(self) -> None:
        self.data = {}

    def get(self, id: int):
        return self.data[id]
    
    def create(self, id: int, data: dict):
        self.data[id] = data
        return self.data[id]
    
    def update(self, id: int, data: dict):
        self.data[id] = data
        return self.data[id]
    
    def delete(self, id: int) -> None:
        del self.data[id]
    

db = DB_manager()
@app.get("/api/v1/item/{id}")
def get_item(id: int, q: Union[str, None] = None):
    return db.get(id)
#this is a comment 

@app.post("/api/v1/item")
def create_item(item: Item):
    db.create(item.id, item)
    return item

@app.put("/api/v1/item/{id}")
def update_item(id: int, item: Item):
    db.create(id, item)
    return db.get(id)

@app.delete("/api/v1/item/{id}")
def delete_item(id: int):
    db.delete(id)
    return {"message": "Item deleted"}