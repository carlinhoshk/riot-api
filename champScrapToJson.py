import requests
import json

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
    # Save champion data to a JSON file
    with open('data/champions.json', 'w') as json_file:
        json.dump(all_champions, json_file, indent=4)
    print("Champion data saved to champions.json.")
else:
    print("Champion data not available.")
