import aiohttp

async def get_sreality_listings(region: str, action: str, category: str, bedrooms: int, price_from: int, price_to: int, per_page: int = 8):
    action_to_category_type_cb = {
        "buy": 1,
        "rent": 2,
    }
    
    category_to_main_cb = {
        "apartment": 1,
        "house": 2,
    }

    params = {
        'category_main_cb': str(category_to_main_cb[category]),
        'category_type_cb': str(action_to_category_type_cb[action]),
        'region': region,
        'czk_price_summary_order2': f'{price_from}|{price_to}',
        'per_page': str(per_page),
    }

    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.sreality.cz/api/cs/v2/estates', params=params) as response:
            if response.status != 200:
                return {"error": "Failed to fetch data from Sreality"}
            response_json = await response.json()
            return response_json["_embedded"]["estates"]
