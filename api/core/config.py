from pydantic import AnyHttpUrl
from typing import List, Union
from decouple import config

class Settings():
    PROJECT_NAME: str = 'AI Home Advisor'

    MONGO_URI: str = config('MONGO_URI')
    MONGO_DB: str = config('MONGO_DB')
    MONGO_COLLECTION: str = config('MONGO_COLLECTION')

    GROQ_API_KEY: str = config('GROQ_API_KEY')
    MIXTRAL_MODEL_NAME: str = "mixtral-8x7b-32768"
    LLAMA_MODEL_NAME: str = "llama3-70b-8192"

    AI_MESSAGE_SYSTEM: str = """You are a AI home advisor.
    You are helping a user find a new home.
    You provide home parameters and recommendations based on the user's input.
    Prague = praha
    The output must be in JSON format.
    Here is the example output:
    {
        "apartment_or_house": "apartment",
        "location": "praha-holesovice",
        "buy_rent": "buy",
        "price_from": 10000,
        "price_to": 20000,
        "bedrooms": 3,
        "my_advise": "Based on your current situation and preferences, I recommend you to buy a 3 bedroom apartment in Prague 4 - Chodov. The price range is between 10,000 and 20,000 CZK. This location is close to the city center and has good public transportation connections. The area is safe and has good schools and parks. I hope this helps you find your new home!"
    }"""
    
    NEXT_PUBLIC_API_BASE_URL: str = config('NEXT_PUBLIC_API_BASE_URL')
    CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000', NEXT_PUBLIC_API_BASE_URL]

    class Config:
        env_file = '.env'

settings = Settings()