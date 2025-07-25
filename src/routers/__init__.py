from fastapi import APIRouter
from .client_router import router as router_client
from .commune_router import router as router_commune 

global_router = APIRouter(prefix="/api/v1")
global_router.include_router(router_client, prefix="/clients", tags=["clients"])
global_router.include_router(router_commune, prefix="/communes", tags=["communes"])
