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

    for key, value in champions_list.items():
        if value['key'] == str(id):
            return value
    return None

# Example
champion_info = getChampionInfo(45)
if champion_info:
    print(champion_info["name"])  # outputs "Veigar"
else:
    print("Champion not found.")
