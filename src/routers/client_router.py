from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_session
from ..repositories import ClientRepository as repository
from ..models import Client, ClientPost, ClientPatch

router = APIRouter()

@router.get("/")
def get_clients(limit: int = 5, session: Session = Depends(get_session)):
    return repository.get_all(session=session, limit=limit)

@router.get("/{id}")
def get_client_by_id(id: int, session: Session = Depends(get_session)):
    return repository.get_by_id(id=id, session=session)

@router.post("/")
def create_client(client_data: ClientPost, session: Session = Depends(get_session)):
    return repository.create(client_data=client_data, session=session)

@router.patch("/{id}")
def patch_client_by_id(id: int, client_data: ClientPatch, session: Session = Depends(get_session)):
    return repository.patch(id=id, client_data=client_data, session=session)

@router.delete("/{id}")
def delete_client_by_id(id: int, session: Session = Depends(get_session)):
    return repository.delete(id=id, session=session)