from groq import Groq, BadRequestError
import json
from api.core.config import settings

async def get_response(life_situation: str, monthly_income_range: str, model_name: str):
    client = Groq(api_key=settings.GROQ_API_KEY)

    MAX_ATTEMPTS = 5  # Define the maximum number of attempts

    for attempt in range(MAX_ATTEMPTS):
        try:
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
            break  # If the code above succeeds, break the loop
        except BadRequestError:
            if attempt < MAX_ATTEMPTS - 1:  # i.e. if it's not the last attempt
                continue  # try again
            else:
                raise  # if it's the last attempt, raise the exception

    return json.loads(chat_completion.choices[0].message.content)

async def get_mixtral_response(life_situation: str, monthly_income_range: str):
    return await get_response(life_situation, monthly_income_range, settings.MIXTRAL_MODEL_NAME)

async def get_llama_response(life_situation: str, monthly_income_range: str):
    return await get_response(life_situation, monthly_income_range, settings.LLAMA_MODEL_NAME)