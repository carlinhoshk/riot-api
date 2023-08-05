import requests, os
from decouple import config



api_key = config('RIOT_KEY')

summoner_name = input('Nome do Jogador: ')

url = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
headers = {'X-Riot-Token': api_key}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    summoner_data = response.json()
    print(summoner_data)
else:
    print('Erro na solicitação:', response.status_code)
