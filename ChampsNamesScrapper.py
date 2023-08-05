import requests

def getChampionInfo(id):
    versions_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
    versions_response = requests.get(versions_url)
    versions = versions_response.json()
    latest = versions[0]

    champions_url = f'https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json'
    champions_response = requests.get(champions_url)
    champions_data = champions_response.json()
    champions_list = champions_data['data']

    if id is None:
        return champions_list
    else:
        for key, value in champions_list.items():
            if value['key'] == str(id):
                return value
        return None

# Get all champions and their names
all_champions = getChampionInfo(None)
if all_champions:
    for champion in all_champions.values():
        print(f"ID: {champion['key']}, Name: {champion['name']}")
else:
    print("Champion data not available.")
