import requests
import json

from constants_and_enums import BASE_URL, GameFormat

def get_card_info(card_name, game_format):
    if game_format is None:
        return "Unsupported format. Choose TCG, OCG, Goat or Genesys."
    parameters = {"name": card_name,
    "misc": "yes",
    "format": game_format.value}
    

    #if game_format == GameFormat.genesys:
        #parameters["format"] = "genesys"

    response = requests.get(BASE_URL, parameters)
    
    
    card_info = json.loads(response.text)
    
    
    if "error" in card_info:
        error_message = card_info["error"]
        return error_message
    
    card_data = card_info["data"][0]
    proper_card_name = card_data["name"]
    card_type = card_data["type"]
    misc = card_data["misc_info"][0]
    formats = misc["formats"]
    
    in_tcg = "TCG" in formats
    in_ocg = "OCG" in formats
    in_goat = "GOAT" in formats
    
    

    if game_format == GameFormat.genesys:
        
        if "Pendulum" in card_type or "Link" in card_type:
                result = f"{proper_card_name} is not legal in the {game_format.value} format."
        else:
        
            point_cost = misc["genesys_points"]
            result = f"{proper_card_name} costs {point_cost} {"point" if point_cost == 1 else "points"} in the {game_format.value} format."

        
            return result
    
    
    match game_format:
        case GameFormat.tcg:
            if not in_tcg:
                banlist_status = "not available"
            elif "banlist_info" in card_data:
                if "ban_tcg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_tcg"]
                else:
                    banlist_status = "Unlimited"
            else:
                banlist_status = "Unlimited"      
        case GameFormat.ocg:
            if not in_tcg:
                banlist_status = "not available"
            elif "banlist_info" in card_data:
                if "ban_ocg" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_ocg"]
                else:
                    banlist_status = "Unlimited"
            else:
                banlist_status = "Unlimited" 
        case GameFormat.goat:
            if not in_goat:
                banlist_status = "not available"
            elif "banlist_info" in card_data:
                if "ban_goat" in card_data["banlist_info"]:
                    banlist_status = card_data["banlist_info"]["ban_goat"]
                else:
                    banlist_status = "Unlimited"
            else:
                banlist_status = "Unlimited"
                
                    

    
    result =  f"{proper_card_name} is {banlist_status} in the {game_format.value} format."
    return result
