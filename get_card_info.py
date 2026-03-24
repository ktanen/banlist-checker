import requests
import json

from constants_and_enums import BASE_URL, GameFormat

def get_card_info(card_name, game_format):
    parameters = {"name": card_name,}

    response = requests.get(BASE_URL, parameters)
    response.raise_for_status()
    card_info_json = response.json()
    card_info = json.loads(card_info_json)
    
    if "error" in card_info:
        raise ValueError("Invalid card name")
    
    card_data = card_info["data"]

    if "banlist_info" not in card_data:
        banlist_status = "not banned"
    else:
        match game_format:
            case GameFormat.tcg:
                banlist_status = card_data["banlist_info"]["ban_tcg"]
            case GameFormat.ocg:
                banlist_status = card_data["banlist_info"]["ban_ocg"]
            case GameFormat.goat:
                banlist_status = card_data["banlist_info"]["ban_goat"]
            case _:
                raise ValueError("Unsupported format name: Choose tcg, ocg, or goat")
    
    result =  f"{card_name} is {banlist_status} in the {game_format} format."
    return result
