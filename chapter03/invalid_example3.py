from typing import List


ITALY_CITIES: List = []
GERMANY_CITIES: List = []
US_CITIES: List = []


def get_restaurant_name(city: str) -> str:
    if city in ITALY_CITIES:
        return "Trattoria Viafore"
    if city in GERMANY_CITIES:
        return "Pat's Kantine"
    if city in US_CITIES:
        return "Pat's Place"
    return None


if get_restaurant_name('Boston'):
    print("Location Found")