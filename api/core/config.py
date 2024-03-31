from pydantic import AnyHttpUrl
from typing import List, Union
from decouple import config
import os

class Settings():
    PROJECT_NAME: str = "AI Home Advisor"
    SUPABASE_URL: str = config("SUPABASE_URL")
    SUPABASE_KEY: str = config("SUPABASE_KEY")
    CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000', "https://home-ai-advisor.vercel.app/"]

    class Config:
        env_file = ".env.local"

settings = Settings()