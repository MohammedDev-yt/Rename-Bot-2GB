# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #

import os

class Config:

    # ---------------- BOT CORE ----------------
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    OWNER_ID = int(os.getenv("OWNER_ID"))

    # ---------------- DATABASE ----------------
    MONGO_URI = os.getenv("MONGO_URI")

    # ---------------- CHANNELS ----------------
    _raw_update = os.getenv("UPDATE_CHANNEL", "https://t.me/Anime_UpdatesAU")

    if _raw_update.startswith("@"):
        UPDATE_CHANNEL = "https://t.me/" + _raw_update[1:]
    elif not _raw_update.startswith("http"):
        UPDATE_CHANNEL = "https://t.me/Anime_UpdatesAU"
    else:
        UPDATE_CHANNEL = _raw_update

    LOG_CHANNEL = os.getenv("LOG_CHANNEL")


# ---------------- EXPORT VARIABLES ----------------

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
OWNER_ID = Config.OWNER_ID
MONGO_URI = Config.MONGO_URI
LOG_CHANNEL = Config.LOG_CHANNEL
UPDATE_CHANNEL = Config.UPDATE_CHANNEL

# ------------------------- #
# Don't Remove Credit
# Ask Doubt @AU_Bot_Discussion
# Owner @Mr_Mohammed_29
# ------------------------- #