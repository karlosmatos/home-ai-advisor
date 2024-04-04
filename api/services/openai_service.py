from openai import OpenAI
import json
from api.core.config import settings

async def get_response(life_situation: str, monthly_income_range: str):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": """
             You are a AI home advisor. 
             You are helping a user find a new home. 
             You provide home parameters and recommendations based on the user's input.
             Prague = praha
             The output must be in JSON format.
             Here is the example output:
                {
                    "location": "praha-holesovice",
                    "buy_rent": "buy",
                    "price_from": 100000,
                    "price_to": 200000,
                    "bedrooms": 3,
                    "my_advise": "Based on your current situation and preferences, I recommend you to buy a 3 bedroom apartment in Prague 4 - Chodov. The price range is between 100,000 and 200,000 CZK. This location is close to the city center and has good public transportation connections. The area is safe and has good schools and parks. I hope this helps you find your new home!"
                }
             """
            },
            {"role": "user", "content": f"I am a {life_situation} with a monthly income of {monthly_income_range}."}
        ]
    )

    return json.loads(completion.choices[0].message.content)