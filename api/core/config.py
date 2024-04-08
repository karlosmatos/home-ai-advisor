from pydantic import AnyHttpUrl
from typing import List, Union
from decouple import config

class Settings():
    PROJECT_NAME: str = 'AI Home Advisor'

    MONGO_URI: str = config('MONGO_URI')
    MONGO_DB: str = config('MONGO_DB')
    MONGO_COLLECTION: str = config('MONGO_COLLECTION')

    OPENAI_API_KEY: str = config('OPENAI_API_KEY')
    GROQ_API_KEY: str = config('GROQ_API_KEY')
    
    NEXT_PUBLIC_API_BASE_URL: str = config('NEXT_PUBLIC_API_BASE_URL')
    CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000', NEXT_PUBLIC_API_BASE_URL]

    class Config:
        env_file = '.env'

settings = Settings()