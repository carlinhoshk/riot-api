import os
from flask import Flask, request, jsonify
import requests
from urllib.parse import quote
# from dotenv import load_dotenv



app = Flask(__name__)

# load_dotenv()
api_key = os.getenv('RIOT_KEY')
# print(api_key)   ( off: my build-project test)
region = 'br1'

# Função para buscar informações do invocador pelo nome
def GetInfoByName(summoner_name):
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{quote(summoner_name)}'
    headers = {'X-Riot-Token': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        summoner_data = response.json()
        return summoner_data
    else:
        return None
# Função para buscar as informações de champion mastery pelo encryptedSummonerId
def GetUserMasteries(summoner_id):
    url = f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{quote(summoner_id)}'
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


@app.route('/summoner_info', methods=['GET'])
def get_summoner_info():
    summoner_name = request.args.get('summoner_name')
    
    if not summoner_name:
        return jsonify({"error": "Summoner name missing"}), 400

    summoner_info = GetInfoByName(summoner_name)
    if summoner_info:
        return jsonify(summoner_info)
    else:
        return jsonify({"error": "Summoner not found"}), 404

@app.route('/summoner_masteries', methods=['GET'])
def get_champion_masteries():
    encrypted_summoner_id = request.args.get('encrypted_summoner_id')
    
    if not encrypted_summoner_id:
        return jsonify({"error": "Encrypted Summoner ID missing"}), 400

    champion_masteries = GetUserMasteries(encrypted_summoner_id)
    return jsonify(champion_masteries)

if __name__ == '__main__':
    app.run(debug=True)
