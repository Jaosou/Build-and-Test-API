from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

app = FastAPI()

router = APIRouter(
    prefix="/account_book",
    tags=["Account Book bank"],
    responses={404: {"message": "Not found"}}
)

class account_bank(BaseModel):
    id_account_bank: str
    name: str
    lname : str
    address : str
    amount : int

""" @app.get("/")
async def root():
    return {"message": "Hello World"} """

data_ac_bk = [
    {
        "id_account_bank" : "2456",
        "name" : "Aticha",
        "lname" : "Meetun",
        "address" : "135 moo 10 Nakhon Nayok",
        "amount" : 0
    },
    {
        "id_account_bank" : "0001",
        "name" : "Ati",
        "lname" : "Mun",
        "address" : "135 moo 10 Nakhon ",
        "amount" : 100000000
    },
    {
        "id_account_bank" : "0002",
        "name" : "Hello",
        "lname" : "World",
        "address" : "Moon",
        "amount" : 200
    }]

@router.get("/")
async def account_banking():
    return data_ac_bk

@router.get("/items/{item_id}")
async def get_account_banking_by_id(item_id: int): # Path parameters with types
    return data_ac_bk[item_id - 1]

@router.post("/items/")
async def create_account_banking(item: account_bank):
    data_ac_bk.append(item.model_dump())
    return item

@router.patch("/items/{item_id}")
async def update_amount(
    id_account_bank: str,
    amount : Optional[int],

):
    for item in data_ac_bk:
        if item["id_account_bank"] == id_account_bank:
            if amount is not None:
                item["amount"] = amount
        return item
    return {"error": "Item not found"}

@router.delete("/items/{item_id}")
async def delete_account_banking(id_account_bank: str):
    for index, item in enumerate(data_ac_bk):
        if item["id_account_bank"] == id_account_bank:
            deleted_item = data_ac_bk.pop(index)
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "Item not found"}

""" @app.put("/items/{item_id}")
async def update_amount_account_banking(item_id: int, updated_item: account_bank):
    for index, item in enumerate(data_ac_bk):
        if item["id_account_bank"] == item_id:
            data_ac_bk[index] = updated_item.model_dump()
            return updated_item
    return {"error": "Item not found"} """

""" fake_items_db = [
    {
        "id": 1,
    "name": "Alpha",
    "description": "High-quality Alpha product",
    "price": 19000.0,
    "tax": 0.3,
    },
    {
    "id": 2,
    "name": "Beta",
    "description": "Durable Beta item",
    "price": 29300.93,
    "tax": 0.5,
    },
    {
    "id": 3,
    "name": "Gamma",
    "description": "Luxury Gamma item",
    "price": 74569.506,
    "tax": 0.7,
    },
    {
    "id": 4,
    "name": "Delta",
    "description": "Affordable Delta item",
    "price": 15000.0,
    "tax": 0.2,
    },
    {
    "id": 5,
    "name": "Epsilon",
    "description": "Premium Epsilon product",
    "price": 87000.25,
    "tax": 0.6,
    },
] """


""" @app.get("/")
async def items():
    return fake_items_db """

""" @app.get("/items/{item_id}")
async def get_item_by_id(item_id: int): # Path parameters with types
    return fake_items_db[item_id - 1]




@app.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item.model_dump())
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(fake_items_db):
        if item["id"] == item_id:
            fake_items_db[index] = updated_item.model_dump()
            return updated_item
    return {"error": "Item not found"}


@app.patch("/items/{item_id}")
async def partially_update_item(
    item_id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[float] = None,
    tax: Optional[float] = None,
):
    for item in fake_items_db:
        if item["id"] == item_id:
            if name is not None:
                item["name"] = name
            if description is not None:
                item["description"] = description
            if price is not None:
                item["price"] = price
            if tax is not None:
                item["tax"] = tax
        return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(fake_items_db):
        if item["id"] == item_id:
            deleted_item = fake_items_db.pop(index)
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "Item not found"} """
