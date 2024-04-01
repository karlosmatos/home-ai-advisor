from pydantic import BaseModel

class RealEstateFilter(BaseModel):
    life_situation: str
    monthly_income_range: str