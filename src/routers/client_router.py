from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db

router = APIRouter()

@router.get("/")
def get_clients(session: Session = Depends(get_db)):
    pass

@router.get("/{id}")
def get_client_by_id(id: int, session: Session = Depends(get_db)):
    pass

@router.post("/")
def create_client(client: dict, session: Session = Depends(get_db)):
    pass
    
@router.patch("/{id}")
def patch_client_by_id(id: int, client: dict, session: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_client_by_id(id: int, session: Session = Depends(get_db)):
    pass