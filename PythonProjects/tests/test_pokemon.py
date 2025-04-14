import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e29e79e579edf865cbbc951b0dca8900'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


# Запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

# В ответе приходит строчка с именем твоего тренера
def test_name_trainer():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '32142'})
    assert response.json()["data"][0]["trainer_name"] == 'Грогу'