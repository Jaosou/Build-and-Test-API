from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

class customer(BaseModel):
        id_customer: str
        name: str
        lastname : str
        email : str
        address : str
        phone_number : str

app = FastAPI()

router = APIRouter(
    prefix="/customers",
    tags=["Customer Data"],
    responses={404: {"message": "Not found"}}
)

data_customer = [
    {
        "id_customer" : "0123456",
        "name" : "eye",
        "lastname" : "eiei",
        "email" : "eye@gmail.com",
        "address" : "lopburi",
        "phone_number" : "0954145299",
    },
    {
        "id_customer" : "7891234",
        "name" : "ohm",
        "lastname" : "auanmak",
        "email" : "ohm@gmail.com",
        "address" : "singburi",
        "phone_number" : "0852361059",
    }
]

@router.get("/")
async def personal_data():
    return data_customer


@router.get("/items/{item_id}")
async def get_personal_data_by_id(item_id: int): # Path parameters with types
    return data_customer[item_id - 1]


@router.post("/items/")
async def create_personal_data(item: customer):
    data_customer.append(item.model_dump())
    return item


@router.delete("/items/{item_id}")
async def delete_personal_data(id_customer: str):
    for index, item in enumerate(data_customer):
        if item["id_customer"] == id_customer:
            deleted_item = data_customer.pop(index)
        return {"message": "Item deleted", "item": deleted_item}
    return {"error": "Item not found"}