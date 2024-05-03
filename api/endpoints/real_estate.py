from fastapi import APIRouter, Depends
from pymongo.collection import Collection

from api.core.config import settings
from api.models.real_estate_model import RealEstateFilter
from api.services import real_estate_service
from api.db import get_db

router = APIRouter()

# Dependency to get the MongoDB collection
async def get_collection(db=Depends(get_db)) -> Collection:
    return db[settings.MONGO_COLLECTION]

@router.get("/", response_model=dict)
async def root():
    return {"message": "Hello World"}

@router.get("/real_estate")
async def get_real_estate(collection: Collection = Depends(get_collection)):
    return await real_estate_service.get_real_estate(collection)

@router.post("/real_estate_recommendation/real_time")
async def get_real_estate_by_location_price_size_real_time(
    filter: RealEstateFilter
):
    return await real_estate_service.get_real_estate_by_filter_real_time(filter)
