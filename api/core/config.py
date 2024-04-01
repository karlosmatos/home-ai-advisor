from pydantic import AnyHttpUrl
from typing import List, Union
from decouple import config

class Settings():
    PROJECT_NAME: str = "AI Home Advisor"
    MONGO_URI: str = config('MONGO_URI')
    OPENAI_API_KEY: str = config('OPENAI_API_KEY')
    CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000', "https://home-ai-advisor.vercel.app", "https://home-ai-advisor-aanj8jqv7-karlosmatos.vercel.app"]

    class Config:
        env_file = ".env"

settings = Settings()