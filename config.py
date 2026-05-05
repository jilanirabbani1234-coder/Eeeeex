import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", ""))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
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
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003549344180"))
