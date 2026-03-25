import sys
import argparse
from constants_and_enums import GameFormat
from get_card_info import get_card_info
from requests import exceptions

def parse_arguments():
    parser = argparse.ArgumentParser(description="""A tool to get the banlist status/point cost of a
    Yu-Gi-Oh! card in the TCG< OCG, Goat, or Genesys format""")
    parser.add_argument("card name", type=str, help="""The name of the card.
    Case-insensitive, but must match the name exactly otherwise.
    Must be in double-quotes if the card name is more than one word long.""")
    parser.add_argument("format",help="""The format you are looking for.
    Can be any of TCG, OCG, Goat, or Genesys.
    Case-insensitive.""")
    args = parser.parse_args()
    return args

def main(args):

    
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
        case "genesys":
            game_format = GameFormat.genesys
        case _:
            raise ValueError("Unsupported format name: Choose tcg, ocg, goat, or genesys")
    try:
        banlist_status = get_card_info(card_name, game_format)
        print(banlist_status)
    except exceptions.HTTPError as e:
        print(e)
    except ValueError as e:
        print(e)



if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
