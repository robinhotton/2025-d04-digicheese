from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlmodel import Session
from typing import List
from ..database import get_session
from ..models import CommunePublic, CommuneCreate, CommunePatch
from ..services import CommuneService as service

router = APIRouter(
    responses={
        404: {"description": "Commune not found"},
        422: {"description": "Validation error"},
        500: {"description": "Internal server error"}
    }
)

@router.get(
    "/",
    response_model=List[CommunePublic],
    status_code=status.HTTP_200_OK,
    summary="Get all communes",
    description="Retrieve all communes with optional pagination"
)
def get_communes(
    limit: int = Query(default=10, ge=1, le=100, description="Number of communes to return"),
    session: Session = Depends(get_session)
):
    """Retrieve all communes with pagination."""
    try:
        communes = service.get_all(session=session, limit=limit)
        return communes
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving communes"
        )

@router.get(
    "/{commune_id}",
    response_model=CommunePublic,
    status_code=status.HTTP_200_OK,
    summary="Get commune by ID",
    description="Retrieve a specific commune by its ID"
)
def get_commune_by_id(
    commune_id: int = Path(..., ge=1, description="Commune ID"),
    session: Session = Depends(get_session)
):
    """Retrieve a commune by its ID."""
    try:
        commune = service.get_by_id(id=commune_id, session=session)
        if not commune:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Commune with ID {commune_id} not found"
            )
        return commune
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the commune"
        )

@router.post(
    "/",
    response_model=CommunePublic,
    status_code=status.HTTP_201_CREATED,
    summary="Create new commune",
    description="Create a new commune with the provided information"
)
def create_commune(
    commune_data: CommuneCreate,
    session: Session = Depends(get_session)
):
    """Create a new commune."""
    try:
        new_commune = service.create(data=commune_data, session=session)
        return new_commune
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the commune"
        )

@router.patch(
    "/{commune_id}",
    response_model=CommunePublic,
    status_code=status.HTTP_200_OK,
    summary="Update commune",
    description="Update an existing commune with partial data"
)
def update_commune(
    commune_data: CommunePatch,
    commune_id: int = Path(..., ge=1, description="Commune ID to update"),
    session: Session = Depends(get_session)
):
    """Update an existing commune."""
    try:
        updated_commune = service.patch(id=commune_id, data=commune_data, session=session)
        if not updated_commune:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Commune with ID {commune_id} not found"
            )
        return updated_commune
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
            detail="An error occurred while updating the commune"
        )

@router.delete(
    "/{commune_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete commune",
    description="Delete a commune by its ID"
)
def delete_commune(
    commune_id: int = Path(..., ge=1, description="Commune ID to delete"),
    session: Session = Depends(get_session)
):
    """Delete a commune by its ID."""
    try:
        result = service.delete(id=commune_id, session=session)
        if "not found" in result.get("message", "").lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Commune with ID {commune_id} not found"
            )
        return None
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the commune"
        )

# Endpoints de recherche spécifiques
@router.get(
    "/search/by-postal-code/{postal_code}",
    response_model=List[CommunePublic],
    status_code=status.HTTP_200_OK,
    summary="Get communes by postal code",
    description="Retrieve all communes with a specific postal code"
)
def get_communes_by_postal_code(
    postal_code: str = Path(..., min_length=5, max_length=5, description="Postal code (5 digits)"),
    session: Session = Depends(get_session)
):
    """Retrieve communes by postal code."""
    try:
        communes = service.get_by_postal_code(postal_code=postal_code, session=session)
        return communes
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while searching communes by postal code"
        )

@router.get(
    "/search/by-department/{department_code}",
    response_model=List[CommunePublic],
    status_code=status.HTTP_200_OK,
    summary="Get communes by department",
    description="Retrieve all communes in a specific department"
)
def get_communes_by_department(
    department_code: str = Path(..., min_length=2, max_length=3, description="Department code"),
    session: Session = Depends(get_session)
):
    """Retrieve communes by department code."""
    try:
        communes = service.get_by_department_code(department_code=department_code, session=session)
        return communes
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while searching communes by department"
        )

@router.get(
    "/search/by-name",
    response_model=List[CommunePublic],
    status_code=status.HTTP_200_OK,
    summary="Search communes by name",
    description="Search communes by name pattern (partial match)"
)
def search_communes_by_name(
    name: str = Query(..., min_length=2, description="Name pattern to search"),
    session: Session = Depends(get_session)
):
    """Search communes by name pattern."""
    try:
        communes = service.search_by_name(name_pattern=name, session=session)
        return communes
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while searching communes by name"
        )

@router.post(
    "/validate-postal-department",
    status_code=status.HTTP_200_OK,
    summary="Validate postal code and department",
    description="Validate that a postal code corresponds to a department"
)
def validate_postal_department(
    postal_code: str = Query(..., min_length=5, max_length=5, description="Postal code"),
    department_code: str = Query(..., min_length=2, max_length=3, description="Department code"),
    session: Session = Depends(get_session)
):
    """Validate postal code and department correspondence."""
    try:
        is_valid = service.validate_postal_code_department(postal_code, department_code)
        return {
            "postal_code": postal_code,
            "department_code": department_code,
            "is_valid": is_valid
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while validating postal code and department"
        )

# Endpoint de santé
@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health check",
    description="Check if the communes service is healthy",
    tags=["health"]
)
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "communes"}