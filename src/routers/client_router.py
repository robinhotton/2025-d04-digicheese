from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from ..database import get_session
from ..models import ClientPublic, ClientPost, ClientPatch
from ..services import ClientService as service


router = APIRouter()


@router.get("/", response_model=list[ClientPublic])
def get_clients(limit: int = 5, session: Session = Depends(get_session)):
    return service.get_all(session=session, limit=limit)


@router.get("/{id}", response_model=ClientPublic)
def get_client_by_id(id: int, session: Session = Depends(get_session)):
    client = service.get_by_id(id=id, session=session)
    if not client:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail=f"Client {id} not found")
    return client


@router.post("/", response_model=ClientPublic, status_code=status.HTTP_201_CREATED)
def create_client(data: ClientPost, session: Session = Depends(get_session)):
    return service.create(data=data, session=session)


@router.patch("/{id}", response_model=ClientPublic)
def patch_client_by_id(id: int, client_data: ClientPatch, session: Session = Depends(get_session)):
    return service.patch(id=id, data=client_data, session=session)


@router.delete("/{id}", response_model=dict)
def delete_client_by_id(id: int, session: Session = Depends(get_session)):
    return service.delete(id=id, session=session)