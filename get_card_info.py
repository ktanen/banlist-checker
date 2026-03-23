import requests
import json

from constants_and_enums import BASE_URL, GameFormat

def get_card_info(card_name, game_format):
    parameters = {"name": card_name,}

    response = requests.get(BASE_URL, parameters)
    response.raise_for_status()
    card_info_json = response.json()
    card_info = json.loads(card_info_json)
    return card_info



