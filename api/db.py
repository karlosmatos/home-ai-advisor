from pymongo import MongoClient
from api.core.config import settings

def get_db():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]
    return db

def get_collection(db):
    collection = db[settings.MONGO_COLLECTION]
    return collection