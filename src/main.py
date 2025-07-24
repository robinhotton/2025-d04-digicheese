from fastapi import FastAPI
from sqlmodel import SQLModel

from .routers import global_router
from .database import engine
from .models import (
    Client,
    Departement,
    Commune
)

app = FastAPI()
app.include_router(global_router)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"response": "Hello World!"}
