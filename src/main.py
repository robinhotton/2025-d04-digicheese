from fastapi import FastAPI
from sqlmodel import SQLModel

from .routers import router
from .database import engine
from .models import (
    Departement,
    Commune,
    Client,
    Commande,
    Conditionnement,
    Objet,
    ObjetCond,
    Detail,
    DetailObjet,
    Enseigne,
    Poids,
    Role,
    Utilisateur,
    RoleUtilisateur
)

from .routers import router

app = FastAPI()
app.include_router(router)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"response": "Hello World!"}
