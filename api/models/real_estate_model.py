from pydantic import BaseModel

class RealEstateFilter(BaseModel):
    is_llama: bool
    life_situation: str
    monthly_income_range: str