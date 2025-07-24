from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_session
from ..repositories import ClientRepository as repository
from ..models import ClientPublic, ClientPost, ClientPatch


router = APIRouter()


@router.get("/", response_model=list[ClientPublic])
def get_clients(limit: int = 5, session: Session = Depends(get_session)):
    return repository.get_all(session=session, limit=limit)


@router.get("/{id}", response_model=ClientPublic)
def get_client_by_id(id: int, session: Session = Depends(get_session)):
    return repository.get_by_id(id=id, session=session)


@router.post("/", response_model=ClientPublic)
def create_client(client_data: ClientPost, session: Session = Depends(get_session)):
    return repository.create(data=client_data, session=session)


@router.patch("/{id}", response_model=ClientPublic)
def patch_client_by_id(id: int, client_data: ClientPatch, session: Session = Depends(get_session)):
    return repository.patch(id=id, data=client_data, session=session)


@router.delete("/{id}", response_model=dict)
def delete_client_by_id(id: int, session: Session = Depends(get_session)):
    return repository.delete(id=id, session=session)