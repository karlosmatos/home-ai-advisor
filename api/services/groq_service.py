from groq import Groq
import json
from api.core.config import settings

async def get_response(life_situation: str, monthly_income_range: str):
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
        model=settings.GROQ_MODEL_NAME,
        temperature=0,
        response_format={"type": "json_object"},
    )

    return json.loads(chat_completion.choices[0].message.content)