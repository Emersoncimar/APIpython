from requests import get

BASE_URL = "https://pokeapi.co"
ALL_JSON = "/api/v2/"

def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response

def get_pokemons():
    response = get(get_links()['pokemon']).json()
    return response

def chose_pokemon(name):
    response = get(get_links()['pokemon'] + name.lower()).json()
    return response

def pokemon_sprites(name):
    response = get(get_links()['pokemon'] + name.lower()).json()
    return response['sprites']['front_default']

print(pokemon_sprites('caterpie'))