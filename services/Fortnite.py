import requests
from os import environ

token = environ.get('FORNITE_API_TOKEN')
fortnite_API_URI = 'https://fortniteapi.io/v1'

def get_player_info(username):
    res_find_player = requests.get(
        f'{fortnite_API_URI}/lookup',
        headers={'Authorization': token},
        params={'username': username}
    )
    player = res_find_player.json()
    if (not player['result']):
        return
    player_id = player['account_id']
    res_player_stats = requests.get(
        f'{fortnite_API_URI}/stats',
        headers={'Authorization': token},
        params={'account': player_id}
    )
    player_stats = res_player_stats.json()
    return {**player_stats, 'id': player_id}

def get_player_matches(id):
    res_player_matches = requests.get(
        f'{fortnite_API_URI}/matches',
        headers={'Authorization': token},
        params={'account': id}
    )
    return res_player_matches.json()