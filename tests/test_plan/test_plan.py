import requests
import pytest 

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '0741fa1d74f3e1d1798544edd9465d19'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 2715

def test_status_code() :
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response() : 
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Miller'