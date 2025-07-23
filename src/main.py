from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, select, Session

from .database import get_db, engine
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

from .routers import router_client, router_objet

app = FastAPI()
app.include_router(router_client)
app.include_router(router_objet)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"response": "Hello World!"}
