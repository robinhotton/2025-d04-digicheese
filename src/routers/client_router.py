from http.client import NOT_IMPLEMENTED
from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlmodel import Session
from typing import List
from ..database import get_session
from ..models import ClientPublic, ClientCreate, ClientPatch
from ..services import ClientService as service

router = APIRouter(
    responses={
        404: {"description": "Client not found"},
        422: {"description": "Validation error"},
        500: {"description": "Internal server error"}
    }
)

@router.get(
    "/",
    response_model=List[ClientPublic],
    status_code=status.HTTP_200_OK,
    summary="Get all clients",
    description="Retrieve all clients with optional pagination"
)
def get_clients(
    limit: int = Query(default=5, ge=1, le=100, description="Number of clients to return"),
    session: Session = Depends(get_session)
):
    """Retrieve all clients with pagination."""
    try:
        clients = service.get_all(session=session, limit=limit)
        return clients
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving clients"
        )

@router.get(
    "/{client_id}",
    response_model=ClientPublic,
    status_code=status.HTTP_200_OK,
    summary="Get client by ID",
    description="Retrieve a specific client by their ID"
)
def get_client_by_id(
    client_id: int = Path(..., ge=1, description="Client ID"),
    session: Session = Depends(get_session)
):
    """Retrieve a client by their ID."""
    try:
        client = service.get_by_id(id=client_id, session=session)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with ID {client_id} not found"
            )
        return client
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the client"
        )

@router.post(
    "/",
    response_model=ClientPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Create new client",
    description="Create a new client with the provided information"
)
def create_client(
    client_data: ClientCreate,
    session: Session = Depends(get_session)
):
    """Create a new client."""
    try:
        new_client = service.create(data=client_data, session=session)
        return new_client
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the client"
        )

@router.patch(
    "/{client_id}",
    response_model=ClientPublic,
    status_code=status.HTTP_200_OK,
    summary="Update client",
    description="Update an existing client with partial data"
)
def update_client(
    client_id: int = Path(..., ge=1, description="Client ID to update"),
    client_data: ClientPatch = ...,
    session: Session = Depends(get_session)
):
    """Update an existing client."""
    try:
        updated_client = service.patch(id=client_id, data=client_data, session=session)
        if not updated_client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with ID {client_id} not found"
            )
        return updated_client
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the client"
        )

@router.delete(
    "/{client_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete client",
    description="Delete a client by their ID"
)
def delete_client(
    client_id: int = Path(..., ge=1, description="Client ID to delete"),
    session: Session = Depends(get_session)
):
    """Delete a client by their ID."""
    try:
        result = service.delete(id=client_id, session=session)
        if "not found" in result.get("message", "").lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with ID {client_id} not found"
            )
        # Return 204 No Content (pas de body)
        return None
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the client"
        )

@router.get(
    "/search/by-email",
    response_model=ClientPublic,
    status_code=status.HTTP_200_OK,
    summary="Get client by email",
    description="Retrieve a client by their email address"
)
def get_client_by_email(
    email: str = Query(..., regex=r"^[^@]+@[^@]+\.[^@]+$", description="Client email address"),
    session: Session = Depends(get_session)
):
    """Retrieve a client by their email address."""
    try:
        client = service.get_by_email(email=email, session=session)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with email '{email}' not found"
            )
        return client
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while searching for the client"
        )

@router.get(
    "/newsletter/subscribers",
    response_model=List[ClientPublic],
    status_code=status.HTTP_200_OK,
    summary="Get newsletter subscribers",
    description="Retrieve all clients who subscribed to the newsletter"
)
def get_newsletter_subscribers(session: Session = Depends(get_session)):
    """Retrieve all clients subscribed to the newsletter."""
    try:
        subscribers = service.get_active_clients(session=session)
        return subscribers
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving newsletter subscribers"
        )

# Endpoint de santé pour vérifier que le service fonctionne
@router.get(
    "/info/health",
    status_code=status.HTTP_200_OK,
    summary="Health check",
    description="Check if the clients service is healthy",
    tags=["health"],
    response_model=dict
)
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "clients"}

# Endpoint pour obtenir des statistiques
@router.get(
    "/info/stats",
    status_code=status.HTTP_200_OK,
    summary="Get client statistics",
    description="Get statistics about clients",
    response_model=dict
)
def get_client_stats(session: Session = Depends(get_session)):
    """Get client statistics."""
    try:
        # Cette logique serait implémentée dans le service
        NOT_IMPLEMENTED = "This feature is not yet implemented"
        stats = {
            "total_clients": NOT_IMPLEMENTED,
            "newsletter_subscribers": NOT_IMPLEMENTED,
            "recent_registrations": NOT_IMPLEMENTED
        }
        return stats
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving statistics"
        )
