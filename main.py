import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '0741fa1d74f3e1d1798544edd9465d19'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
'''body_confirmation = {
    "trainer_token": TOKEN
    }
body_create = { 
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/012.png"
    }
body_put = {
    "pokemon_id": "28007",
    "name": "Pikaa",
    "photo": "https://dolnikov.ru/pokemons/albums/014.png"
}'''
body_post = {
    "pokemon_id": "28007"
}
'''response_confirmation = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_confirmation)'''
'''response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create)
print(response_create.json)
response_put = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_put)
print(response_put.text)'''
response_post = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_post)
print(response_post.json)