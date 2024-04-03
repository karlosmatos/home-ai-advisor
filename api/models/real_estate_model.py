from pydantic import BaseModel

class RealEstateFilter(BaseModel):
    is_gpt: bool
    life_situation: str
    monthly_income_range: str