from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter(
    prefix="/section",
    tags=["Account Section"],
    responses={404: {"message": "Not found"}}
)

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


fake_items_db = [
    {
        "id": 1,
        "name": "Kmutt",
        "description": "Bank Branch kmutt",
        "number": 025468.545,
        "address": "MF2W+GH กรุงเทพมหานคร",
    },
    {
        "id": 2,
        "name": "Kmutnb",
        "description": "Bank Branch Kmutnb",
        "number": 02548465.356,
        "address": "RG97+MP กรุงเทพมหานคร",
    },
    {
        "id": 3,
        "name": "Kmitl",
        "description": "Luxury Gamma item",
        "number": 0265865.324,
        "address": "PQHH+X7 กรุงเทพมหานคร",
    },     
]

@router.get("/")
async def items():
    return fake_items_db

@router.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return fake_items_db[item_id - 1]

@router.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item.dict())
    return item
@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    for index, db_item in enumerate(fake_items_db):
        if db_item["id"] == item_id:
            fake_items_db[index] = item.dict()
            return item
