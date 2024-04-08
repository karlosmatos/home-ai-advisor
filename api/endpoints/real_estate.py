from bson import json_util
import json
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient

from api.core.config import settings
from api.models.real_estate_model import RealEstateFilter
from api.services import groq_service, openai_service

router = APIRouter()

client = MongoClient(settings.MONGO_URI)
db = client['realestatecluster']
collection = db['sreality']

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/real_estate")
async def get_real_estate():
    real_estate = collection.find({}).limit(6)
    return json.loads(json_util.dumps(list(real_estate)))

@router.get("/real_estate_1")
async def get_real_estate_1():
    return {"message": "Hello World"}

@router.post("/real_estate_recommendation")
async def get_real_estate_by_location_price_size(filter: RealEstateFilter):
    if filter.is_gpt:
        ai_response = await openai_service.get_response(filter.life_situation, filter.monthly_income_range)

    else:
        ai_response = await groq_service.get_response(filter.life_situation, filter.monthly_income_range)
    print(ai_response)
    real_estate_list = list(collection.find(
        {
            "seo.locality": {"$regex": f".*{ai_response['location']}.*", "$options": "i"},
            "price": {"$gte": ai_response["price_from"], "$lte": ai_response["price_to"]},
        }
    ).limit(6))
    if not real_estate_list:
        raise HTTPException(status_code=404, detail="Real estate not found")
    return {
        "ai_response": ai_response["my_advise"],
        "real_estate_list": json.loads(json_util.dumps(real_estate_list))
    }