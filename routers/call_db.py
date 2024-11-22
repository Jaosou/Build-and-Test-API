from fastapi import APIRouter
from pydantic import BaseModel
import mysql.connector as mysql
# Connect Database

router = APIRouter(
    prefix="/mysql_db",
    tags=["Call in my databade"],
    responses={404: {"message": "Not found"}}
)

mydb = mysql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="________________",
    database="________________"
)
mycursor = mydb.cursor()


# GET All items.
@router.get("/")
async def get_items():
    mycursor.execute("SELECT * FROM account_book_bank")
    myresult = mycursor.fetchall()
    list_item = []
    for i in myresult:
        item = {}
        item['id'] = i[0]
        item['name'] = i[1]
        item['lname'] = i[2]
        list_item.append(item)
    return list_item

# GET items by id.
@router.get("/{item_id}")
async def get_item_byID(item_id: int):
    sql = "SELECT * FROM account_book_bank WHERE idaccount_book_bank = %s"
    mycursor.execute(sql,(item_id,))
    myresult = mycursor.fetchall()
    list_item = []
    for i in myresult:
        item = {}
        item['id'] = i[0]
        item['name'] = i[1]
        item['price'] = i[2]
        list_item.append(item)
    return list_item

# Create Model Item.
class Item(BaseModel):
    id: int
    name: str
    lname: str
# Create Item.
@router.post("/")
async def create_item(item: Item):
    sql = """
    INSERT INTO account_book_bank (idaccount_book_bank,account_book_bank_name,account_book_bank_lname)
    VALUE(%s ,%s ,%s)
    """
    mycursor.execute(sql)
    mydb.commit()
    max_id = """ SELECT * FROM account_book_bank. WHERE id = (SELECT MAX(id) FROM store.item); """
    mycursor.execute(max_id)
    myresult = mycursor.fetchall()
    for i in myresult:
        item = {}
        item['id'] = i[0]
        item['name'] = i[1]
        item['lname'] = i[2]
    return item
