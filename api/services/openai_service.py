from openai import OpenAI
import json
from api.core.config import settings

async def get_response(life_situation: str, monthly_income_range: str):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model=settings.OPENAI_MODEL_NAME,
        temperature=0,
        messages=[
            {"role": "system", "content": settings.AI_MESSAGE_SYSTEM},
            {"role": "user", "content": f"I am a {life_situation} with a monthly income of {monthly_income_range}."}
        ]
    )

    return json.loads(completion.choices[0].message.content)