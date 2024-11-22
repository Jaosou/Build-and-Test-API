from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

app = FastAPI()

router = APIRouter(
    prefix="/banking_company",
    tags=["Banking Company"],
    responses={404: {"message": "Not found"}}
)

class banking_company(BaseModel):
    id_banking_company : str
    name_banking_company : str
    description : str | None
    address : str
    c_phone_number : str

banking_company_account = [
    {
        "id_banking_company" : "00001",
        "name_banking_company" : "Kasikong",
        "description" : "Green",
        "address" : "I my heart",
        "c_phone_number" : "09825631"
    },
    {
        "id_banking_company" : "00002",
        "name_banking_company" : "Kungkai",
        "description" : "SkyBlue",
        "address" : "In my heart",
        "c_phone_number" : "09825632"
    },
    {
        "id_banking_company" : "00003",
        "name_banking_company" : "oamsi",
        "description" : "Orange",
        "address" : "Out my heart",
        "c_phone_number" : "09825634"
    },
]

@router.get("/")
async def banking_company_data():
    return banking_company_account


@router.get("/items/{item_id}")
async def get_banking_company_account_by_id(item_id: int): # Path parameters with types
    return banking_company_account[item_id - 1]


@router.post("/items/")
async def create_banking_company_account(item: banking_company):
    banking_company_account.append(item.model_dump())
    return item