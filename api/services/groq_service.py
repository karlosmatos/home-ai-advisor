from groq import Groq
import json
from api.core.config import settings

async def get_response(life_situation: str, monthly_income_range: str, model_name: str):
    client = Groq(api_key=settings.GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": settings.AI_MESSAGE_SYSTEM
            },
            {
                "role": "user",
                "content": f"I am a {life_situation} with a monthly income of {monthly_income_range}.",
            }
        ],
        model=model_name,
        temperature=0,
        response_format={"type": "json_object"},
    )

    return json.loads(chat_completion.choices[0].message.content)

async def get_mixtral_response(life_situation: str, monthly_income_range: str):
    return await get_response(life_situation, monthly_income_range, settings.MIXTRAL_MODEL_NAME)

async def get_llama_response(life_situation: str, monthly_income_range: str):
    return await get_response(life_situation, monthly_income_range, settings.LLAMA_MODEL_NAME)