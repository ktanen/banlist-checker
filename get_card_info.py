import requests
import json

from constants_and_enums import BASE_URL, GameFormat

def get_card_info(card_name, game_format):
    parameters = {"name": card_name}
    
    response = requests.get(BASE_URL, parameters)
    response.raise_for_status()
    card_info = json.loads(response.text)
    
    
    if "error" in card_info:
        raise ValueError("Invalid card name")
    
    card_data = card_info["data"][0]

    if "banlist_info" not in card_data:
        banlist_status = "not banned"
    else:
        match game_format:
            case GameFormat.tcg:
                if "ban_tcg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_tcg"]
                else:
                    banlist_status = "not available"
            case GameFormat.ocg:
                if "ban_ocg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_ocg"]
                else:
                    banlist_status = "not available"
            case GameFormat.goat:
                if "ban_goat" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_goat"]
                else:
                    banlist_status = "not available"

    
    result =  f"{card_name} is {banlist_status} in the {game_format.value} format."
    return result
