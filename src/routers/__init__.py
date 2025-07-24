from fastapi import APIRouter
from .client_router import router as router_client

global_router = APIRouter(prefix="/api/v1")
global_router.include_router(router_client, prefix="/clients", tags=["clients"])
