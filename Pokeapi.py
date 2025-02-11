from requests import get

BASE_URL = "https://pokeapi.co"
ALL_JSON = "/api/v2/"

def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response

print(get_links())