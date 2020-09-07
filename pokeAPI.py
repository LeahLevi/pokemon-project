import requests


def get_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    info = requests.get(url=url, verify=False).json()
    url = f"{info['species']['url']}"
    info = requests.get(url=url, verify=False).json()
    url = f"{info['evolution_chain']['url']}"
    info = requests.get(url=url, verify=False).json()
    return info


def get_base_experience(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    info = requests.get(url=url, verify=False).json()
    return info['base_experience']
