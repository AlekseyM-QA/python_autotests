import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e29e79e579edf865cbbc951b0dca8900'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
P_ID = "289198"

body_create = {
    "name": "Рой",
    "photo_id": 15
}

body_name_change = {
    "pokemon_id": P_ID,
    "name": "Рой2",
    "photo_id": 15
}

body_add_pokeball = {
    "pokemon_id": P_ID
}

# Создание покемона
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

# Смена имени покемона
'''response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)'''

# Поймать покемона в покебол
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

