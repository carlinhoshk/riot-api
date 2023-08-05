import requests
from decouple import config
def get_champion_id(api_key, region, summoner_id):
    url = f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}'
    headers = {
        'X-Riot-Token': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        champion_data = response.json()
        champion_ids = [champion['championId'] for champion in champion_data]
        return champion_ids
    else:
        print('Erro na solicitação:', response.status_code)
        return None


api_key = config('RIOT_KEY')
region = 'br1'
summoner_id = '30'

champion_ids = get_champion_id(api_key, region, summoner_id)
if champion_ids:
    for champion_id in champion_ids:
        print(f"Champion ID: {champion_id}")




