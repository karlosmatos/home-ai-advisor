from bson import json_util
from openai import OpenAI
import json

from fastapi import APIRouter, HTTPException
from collections import defaultdict
from pymongo import MongoClient
from api.core.config import settings

router = APIRouter()

client = MongoClient(settings.MONGO_URI)
db = client['realestatecluster']
collection = db['sreality']

@router.get("/real_estate")
async def get_real_estate():
    real_estate = collection.find({}).limit(6)
    return json.loads(json_util.dumps(list(real_estate)))

@router.get("/real_estate/{location}")
async def get_real_estate_by_id(location: str):
    real_estate = collection.find({"seo.locality": location})
    real_estate_list = list(real_estate)
    if not real_estate_list:
        raise HTTPException(status_code=404, detail="Real estate not found")
    return json.loads(json_util.dumps(real_estate_list))

@router.get("/real_estate/search")
async def search_real_estate(query: str):
    real_estate = collection.find({"$text": {"$search": query}})
    return json.loads(json_util.dumps(list(real_estate)))

@router.get("/openai/{prompt}")
async def get_openai_response(prompt: str):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """
         You are a AI home advisor. 
         You are helping a user find a new home. 
         You provide home parameters and recommendations based on the user's input. 
         The output must be in JSON format.
         """},
        {"role": "user", "content": prompt}
    ]
    )

    return json.loads(completion.choices[0].message.content)
