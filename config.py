import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("API_ID","16743442")
API_HASH = os.getenv("API_HASH","12bbd720f4097ba7713c5e40a11dfd2a")
BOT_TOKEN = os.getenv("BOT_TOKEN","6065321925:AAEWc4Y5PDWTcE4jUBYIAL6s1OzlnuaWWmU")
MONGO_DB_URI = os.getenv("MONGO_DB_URI","mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
STATUS_MSG_ID = os.getenv("STATUS_MSG_ID","3")
SCHEDULE_MSG_ID = os.getenv("SCHEDULE_MSG_ID","2")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "@Index_AC")
INDEX_CHANNEL_USERNAME = os.getenv("INDEX_CHANNEL_USERNAME","Index_AC")
UPLOADS_CHANNEL_USERNAME = os.getenv("UPLOADS_CHANNEL_USERNAME","Upload_AC")
TECHZ_API_KEY = os.getenv("TECHZ_API_KEY","RFKVZE")
COMMENTS_GROUP_LINK = os.getenv("COMMENTS_GROUP_LINK", "https://t.me/MissCamelliaSupport")
SLEEP_TIME = os.getenv("SLEEP_TIME", 60)

for k, v in {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "STATUS_MSG_ID": STATUS_MSG_ID,
    "SCHEDULE_MSG_ID": SCHEDULE_MSG_ID,
    "INDEX_CHANNEL_USERNAME": INDEX_CHANNEL_USERNAME,
    "UPLOADS_CHANNEL_USERNAME": UPLOADS_CHANNEL_USERNAME,
    "TECHZ_API_KEY": TECHZ_API_KEY,
    "COMMENTS_GROUP_LINK": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use AutoAnimeBot")
