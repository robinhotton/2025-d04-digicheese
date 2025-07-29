from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session

from ..database import get_session
from ..models import ClientPublic, ClientPost, ClientPatch
from ..services import ClientService as service


router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[ClientPublic])
def get_clients(
    limit: int = Query(default=10, ge=1, le=100, description="Number of clients to return"),
    offset: int = Query(default=0, ge=0, description="Number of clients to skip"),
    session: Session = Depends(get_session)
):
    """Retrieve all clients with pagination."""
    return service.get_all(limit=limit, offset=offset, session=session)


@router.get("/{client_id}", response_model=ClientPublic)
def get_client_by_id(client_id: int, session: Session = Depends(get_session)):
    """Retrieve a specific client by ID."""
    client = service.get_by_id(id=client_id, session=session)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Client with ID {client_id} not found"
        )
    return client


@router.post("/", response_model=ClientPublic, status_code=status.HTTP_201_CREATED)
def create_client(data: ClientPost, session: Session = Depends(get_session)):
    """Create a new client."""
    try:
        client = service.create(data=data, session=session)
        return client
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Failed to create client"
        )


@router.patch("/{client_id}", response_model=ClientPublic)
def update_client(
    client_id: int, 
    client_data: ClientPatch, 
    session: Session = Depends(get_session)
):
    """Update an existing client partially."""
    try:
        client = service.patch(id=client_id, data=client_data, session=session)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Client with ID {client_id} not found"
            )
        return client
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, session: Session = Depends(get_session)):
    """Delete a client by ID."""
    success = service.delete(id=client_id, session=session)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Client with ID {client_id} not found"
        )
    # HTTP 204 No Content - pas de body à retourner