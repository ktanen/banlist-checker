import sys
from constants_and_enums import GameFormat
from get_card_info import get_card_info
from requests import exceptions
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <card name> <format>")
        sys.exit(1)
    
    card_name = sys.argv[1]
    game_format_string = sys.argv[2].lower()
    game_format = None
    match game_format_string:
        case "tcg":
            game_format = GameFormat.tcg
        case "ocg":
            game_format = GameFormat.ocg
        case "goat":
            game_format = GameFormat.goat
        case _:
            raise ValueError("Unsupported format name: Choose tcg, ocg, or goat")
    try:
        banlist_status = get_card_info(card_name, game_format)
        print(banlist_status)
    except exceptions.HTTPError as e:
        print("Invalid card name")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
