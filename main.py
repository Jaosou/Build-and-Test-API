from fastapi import FastAPI
from routers import item,banking_company,customer,section_data,call_db
import uvicorn


app = FastAPI()

app.include_router(item.router)
app.include_router(banking_company.router)
app.include_router(customer.router)
app.include_router(section_data.router)
app.include_router(call_db.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)