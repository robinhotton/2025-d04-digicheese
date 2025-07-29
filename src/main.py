from fastapi import FastAPI
from sqlmodel import SQLModel

from .routers import global_router
from .database import engine
from .models import (
    Client,
    Commune,
    Order,
    OrderItem,
    Product,
    ProductCategory,
    ShippingRate,
    Role,
    User,
    UserRole
)

app = FastAPI()
SQLModel.metadata.drop_all(bind=engine)
SQLModel.metadata.create_all(bind=engine)
app.include_router(global_router)

@app.get("/")
def home():
    return {"response": "Hello World!"}
