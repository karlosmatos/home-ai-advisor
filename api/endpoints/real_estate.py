from bson import json_util
import json
from fastapi import APIRouter, HTTPException, Depends
from pymongo import MongoClient

from api.core.config import settings
from api.models.real_estate_model import RealEstateFilter
from api.services import groq_service, openai_service
from api.db import get_db

router = APIRouter()

def get_collection():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]
    collection = db[settings.MONGO_COLLECTION]
    return collection

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/real_estate/")
async def get_real_estate(collection=Depends(get_collection)):
    real_estate = collection.find({}).limit(6)
    return json.loads(json_util.dumps(list(real_estate)))

@router.post("/real_estate_recommendation/")
async def get_real_estate_by_location_price_size(
    filter: RealEstateFilter, 
    collection=Depends(get_collection)
):
    if filter.is_gpt:
        ai_response = await openai_service.get_response(filter.life_situation, filter.monthly_income_range)
    else:
        ai_response = await groq_service.get_response(filter.life_situation, filter.monthly_income_range)
    print(ai_response)
    if real_estate_list := list(
        collection.find(
            {
                "seo.locality": {
                    "$regex": f".*{ai_response['location']}.*",
                    "$options": "i",
                },
                "price": {
                    "$gte": ai_response["price_from"],
                    "$lte": ai_response["price_to"],
                },
            }
        ).limit(6)
    ):
        return {
            "ai_response": ai_response["my_advise"],
            "real_estate_list": json.loads(json_util.dumps(real_estate_list))
        }
    else:
        raise HTTPException(status_code=404, detail="Real estate not found")