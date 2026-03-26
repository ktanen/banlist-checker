from enum import Enum

BASE_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
class GameFormat(Enum):
    tcg = "TCG"
    ocg = "OCG"
    goat = "Goat"
    genesys = "Genesys"
    master_duel = "Master Duel"
    duel_links = "Duel Links"
    ocg_goat = "OCG GOAT"