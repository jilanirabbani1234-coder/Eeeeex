import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "29426008"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "fedd630ba4bd77044ee4e5a00e5300e6")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8683411777:AAFAmPQHFVAxPep-e9QPixiwcUK17QS_XvQ")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Eeeexbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1717411093"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "1717411093"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003549344180"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1717411093").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003549344180"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Bot_user:gfZcDelYJBwPda9A@cluster0.thbvcoa.mongodb.net/?appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003549344180"))
