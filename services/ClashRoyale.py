import requests
from os import environ

bearer_token = environ.get('CLASH_ROYALE_API_TOKEN')
clash_royale_API_URI = 'https://api.clashroyale.com/v1/players/'

def get_player_info(tag):
    response = requests.get(
        clash_royale_API_URI + tag,
        headers={'authorization': f'Bearer: {bearer_token}'},
    )
    if (response.status_code != 200):
        return
    return response.json()

def get_player_matches(tag):
    response = requests.get(
        f'{clash_royale_API_URI}{tag}/battlelog',
        headers={'authorization': f'Bearer: {bearer_token}'},
    )
    return response.json()