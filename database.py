# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
import time


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

client = AsyncIOMotorClient(MONGO_URI)

db = client.rename_bot
users = db.users
leaderboard = db.leaderboard
user_bots = db.bots


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def update_leaderboard(user_id):

    await leaderboard.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "today": 1,
                "weekly": 1,
                "monthly": 1,
                "alltime": 1
            },
            "$set": {
                "user_id": user_id
            }
        },
        upsert=True
    )


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_user(uid):
    return await users.find_one({"_id": uid})

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def set_user(uid, data):
    await users.update_one(
        {"_id": uid},
        {"$set": data},
        upsert=True
    )


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def add_user(uid):
    await users.update_one(
        {"_id": uid},
        {
            "$setOnInsert": {
                "prefix": "",
                "suffix": "",
                "caption": "",
                "thumb": "",
                "banned": False,
                "premium": False
            }
        },
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def is_banned(uid):
    user = await get_user(uid)

    return user.get("banned", False) if user else False

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_all_users():
    return await users.find({}).to_list(length=None)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def get_premium_status(uid):
    user = await get_user(uid)

    if not user:
        return False

    return user.get("premium", False)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

async def setup_database():
    print("Dᴀᴛᴀʙᴀsᴇ Cᴏɴɴᴇᴄᴛᴇᴅ ✅")

# ---------------- USER BOTS SYSTEM ---------------- #

async def get_user_bots(user_id):
    return await user_bots.find_one({"_id": user_id})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def add_user_bot(user_id, username, token):

    await user_bots.update_one(
        {"_id": user_id},
        {
            "$push": {
                "bots": {
                    "username": username,
                    "token": token,
                    "uploads": 0
                }
            },
            "$setOnInsert": {
                "active": 0,
                "last_used": "Never"
            }
        },
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def increase_bot_upload(user_id, bot_index=0):

    await user_bots.update_one(
        {"_id": user_id},
        {
            "$inc": {
                f"bots.{bot_index}.uploads": 1
            },
            "$set": {
                "last_used": "Just now"
            }
        }
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def set_active_bot(user_id, index):

    await user_bots.update_one(
        {"_id": user_id},
        {
            "$set": {
                "active": index
            }
        }
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def delete_all_bots(user_id):

    await user_bots.delete_one({"_id": user_id})
    
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #