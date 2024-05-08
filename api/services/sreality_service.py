import aiohttp
from typing import Union, Dict, Any

ACTION_TO_CATEGORY_TYPE_CB = {
    "buy": 1,
    "rent": 2,
}

CATEGORY_TO_MAIN_CB = {
    "apartment": 1,
    "house": 2,
}

BEDROOMS_TO_CATEGORY_SUB_CB = {
    1: '3|2',
    2: '4|5',
    3: '6|7',
    4: '8|9',
    5: '10|11',
    6: '12',
}

SREALITY_API_URL = 'https://www.sreality.cz/api/cs/v2/estates'

async def get_sreality_listings(region: str, action: str, category: str, bedrooms: int, price_from: int, price_to: int, per_page: int = 8) -> Union[Dict[str, Any], str]:
    """
    Fetches real estate listings from Sreality API.

    Parameters:
    region (str): The region for the listings.
    action (str): The action (buy or rent).
    category (str): The category (apartment or house).
    bedrooms (int): The number of bedrooms.
    price_from (int): The minimum price.
    price_to (int): The maximum price.
    per_page (int): The number of listings per page.

    Returns:
    dict: A dictionary containing the listings if successful, or an error message if not.
    """
    try:
        params = {
            'category_main_cb': str(CATEGORY_TO_MAIN_CB[category]),
            'category_type_cb': str(ACTION_TO_CATEGORY_TYPE_CB[action]),
            'category_sub_cb': BEDROOMS_TO_CATEGORY_SUB_CB[bedrooms],
            'region': region,
            'czk_price_summary_order2': f'{price_from}|{price_to}',
            'per_page': str(per_page),
        }
    except KeyError as e:
        return f"Invalid parameter: {e}"

    async with aiohttp.ClientSession() as session:
        async with session.get(SREALITY_API_URL, params=params) as response:
            if response.status != 200:
                return {"error": "Failed to fetch data from Sreality"}
            response_json = await response.json()
            return response_json["_embedded"]["estates"]