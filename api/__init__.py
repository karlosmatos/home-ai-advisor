from fastapi import APIRouter
from .endpoints import real_estate

prefix_api = "/api"

router = APIRouter()
router.include_router(real_estate.router, tags=["real_estate"], prefix=prefix_api)