from bson import json_util
from openai import OpenAI
import json
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient

from api.core.config import settings
from api.models.real_estate_model import RealEstateFilter

router = APIRouter()

client = MongoClient(settings.MONGO_URI)
db = client['realestatecluster']
collection = db['sreality']

@router.get("/real_estate")
async def get_real_estate():
    real_estate = collection.find({}).limit(6)
    return json.loads(json_util.dumps(list(real_estate)))

@router.get("/real_estate/{location}")
async def get_real_estate_by_location(location: str):
    # Use a case-insensitive regular expression to match the location
    regex = {"$regex": f".*{location}.*", "$options" :"i"}
    real_estate = collection.find({"seo.locality": regex})
    real_estate_list = list(real_estate)
    if not real_estate_list:
        raise HTTPException(status_code=404, detail="Real estate not found")
    return json.loads(json_util.dumps(real_estate_list))

@router.get("/openai/{prompt}")
async def get_openai_response(life_situation: str, monthly_income_range: str):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """
         You are a AI home advisor. 
         You are helping a user find a new home. 
         You provide home parameters and recommendations based on the user's input.
         Prague = praha
         The output must be in JSON format.
         Here is the example output:
            {
                "location": "praha-chodov",
                "buy_rent": "buy",
                "price_from": 100000,
                "price_to": 200000,
                "bedrooms": 3,
                "my_advise": "Based on your current situation and preferences, I recommend you to buy a 3 bedroom apartment in Prague 4 - Chodov. The price range is between 100,000 and 200,000 CZK. This location is close to the city center and has good public transportation connections. The area is safe and has good schools and parks. I hope this helps you find your new home!"
            }
         """},
        {"role": "user", "content": f"I am a {life_situation} with a monthly income of {monthly_income_range}."}
    ]
    )

    return json.loads(completion.choices[0].message.content)

@router.get("/real_estate_recommendation/")
async def get_real_estate_by_location_price_size(filter: RealEstateFilter):
    openai_response = await get_openai_response(filter.life_situation, filter.monthly_income_range)
    print(openai_response)
    regex = {"$regex": f".*{openai_response['location']}.*", "$options": "i"}
    real_estate = collection.find(
        {
            "seo.locality": regex,
            "price": {"$gte": openai_response["price_from"], "$lte": openai_response["price_to"]},
        }
    ).limit(6)
    real_estate_list = list(real_estate)
    if not real_estate_list:
        raise HTTPException(status_code=404, detail="Real estate not found")
    return {
        "openai_response": openai_response["my_advise"],
        "real_estate_list": json.loads(json_util.dumps(real_estate_list))
    }