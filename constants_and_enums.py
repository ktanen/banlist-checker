from enum import Enum

BASE_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
class GameFormat(Enum):
    tcg = "tcg"
    ocg = "ocg"
    goat = "goat"
    genesys = "genesys"
    master_duel = "master duel"
    duel_links = "duel links"
    ocg_goat = "ocg goat"