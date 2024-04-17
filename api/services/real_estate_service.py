from typing import List
from pymongo.collection import Collection
from api.models.real_estate_model import RealEstateFilter
from api.services import openai_service, groq_service, sreality_service
from bson import json_util
import json

from fastapi import HTTPException

async def fetch_ai_response(filter: RealEstateFilter):
    """
    Fetch AI response based on the filter using either OpenAI or GROQ service.
    """
    if filter.is_gpt:
        return await openai_service.get_response(filter.life_situation, filter.monthly_income_range)
    else:
        return await groq_service.get_response(filter.life_situation, filter.monthly_income_range)

async def get_real_estate(collection: Collection):
    """
    Fetch a list of real estate data from the database.
    """
    real_estate_cursor = collection.find({}).limit(6)
    real_estate_list = await real_estate_cursor.to_list(length=6)
    return json.loads(json_util.dumps(real_estate_list))

async def get_real_estate_by_filter(filter: RealEstateFilter, collection: Collection):
    """
    Fetch real estate data based on a filter and AI response.
    """
    ai_response = await fetch_ai_response(filter)
    query = {
        "seo.locality": {"$regex": f".*{ai_response['location']}.*", "$options": "i"},
        "price": {"$gte": ai_response["price_from"], "$lte": ai_response["price_to"]},
    }
    real_estate_cursor = collection.find(query).limit(6)
    real_estate_list = await real_estate_cursor.to_list(length=6)
    if real_estate_list:
        return {
            "ai_response": ai_response["my_advise"],
            "real_estate_list": json.loads(json_util.dumps(real_estate_list))
        }
    else:
        raise HTTPException(status_code=404, detail="Real estate not found")

async def get_real_estate_by_filter_real_time(filter: RealEstateFilter, collection: Collection):
    """
    Fetch real estate data based on a filter and AI response, querying in real-time from an external service.
    """
    ai_response = await fetch_ai_response(filter)
    if ai_response:
        real_estate_list = await sreality_service.get_sreality_listings(
            region=ai_response["location"],
            action=ai_response["buy_rent"],
            category=ai_response["apartment_or_house"],
            bedrooms=ai_response["bedrooms"],
            price_from=ai_response["price_from"],
            price_to=ai_response["price_to"]
        )
        return {
            "ai_response": ai_response["my_advise"],
            "real_estate_list": json.loads(json_util.dumps(real_estate_list))
        }
    else:
        raise HTTPException(status_code=404, detail="Real estate not found")
