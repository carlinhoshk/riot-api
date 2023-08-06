import requests
import os
#from decouple import config ( old build, new give a virtualenv with path variables )


name = input('Nome do Jogador: ')
url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
api_key = os.getenv('RIOT_KEY')
params = {'api_key': api_key}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    summoner_data = response.json()
    print(summoner_data)
except requests.exceptions.RequestException as e:
    print('Erro na solicitação:', e)