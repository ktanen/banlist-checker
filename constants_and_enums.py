from enum import Enum

BASE_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
GameFormat = Enum('GameFormat',['tcg', 'ocg', 'goat'])