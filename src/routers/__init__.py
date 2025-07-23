from fastapi import APIRouter
from .client_router import router as router_client

router = APIRouter()
router.include_router(router_client, prefix="/clients", tags=["clients"])
