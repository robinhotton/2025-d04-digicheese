from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..repositories import ClientRepository
from ..models import Client, ClientPost, ClientPatch

router = APIRouter()

@router.get("/")
def get_clients(db: Session = Depends(get_db)):
    return ClientRepository(db).get_all()

@router.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    return ClientRepository(db)

@router.post("/")
def create_client(client: ClientPost, db: Session = Depends(get_db)):
    return ClientRepository(db)
    
@router.patch("/{id}")
def patch_client_by_id(id: int, client: ClientPatch, db: Session = Depends(get_db)):
    return ClientRepository(db)

@router.delete("/{id}")
def delete_client_by_id(id: int, db: Session = Depends(get_db)):
    return ClientRepository(db)