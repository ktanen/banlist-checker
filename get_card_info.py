import requests
import json

from constants_and_enums import BASE_URL, GameFormat

def get_card_info(card_name, game_format):
    parameters = {"name": card_name,
    "misc": "yes",
    "format": game_format.value}
    
    response = requests.get(BASE_URL, parameters)
    response.raise_for_status()
    card_info = json.loads(response.text)
    
    
    if "error" in card_info:
        error_message = card_info["error"]
        raise ValueError(error_message)
    
    card_data = card_info["data"][0]
    card_type = card_data["type"]
    if game_format == GameFormat.genesys:
        
        if "Pendulum" in card_type or "Link" in card_type:
                result = f"{card_name} is not legal in the {game_format.value} format."
        else:
            misc = card_data["misc_info"][0]
            point_cost = misc["genesys_points"]
            result = f"{card_name} costs {point_cost} {"point" if point_cost == 1 else "points"} in the {game_format.value} format."

        
        return result
    if "banlist_info" not in card_data:
        banlist_status = "not banned"
    else:
        match game_format:
            case GameFormat.tcg:
                if "ban_tcg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_tcg"]
                else:
                    banlist_status = "not banned or not available"
            case GameFormat.ocg:
                if "ban_ocg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_ocg"]
                else:
                    banlist_status = "not banned or not available"
            case GameFormat.goat:
                if "ban_goat" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_goat"]
                else:
                    banlist_status = "not banned or not available"

    
    result =  f"{card_name} is {banlist_status} in the {game_format.value} format."
    return result
