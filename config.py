import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("23028479"))
API_HASH = getenv("c1e6a93b04c0810a5c282d8d8d44ea6f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7892211587:AAGrn0aYADE75zX9pJOrofw0iaTbTwv1bPk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002252184024))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7038202445))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Mrcutex1/Riyuu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Shorekeeper_updates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Group_India_Chat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING2 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING3 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING4 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)
STRING5 = getenv("BQGWS8YAcExf2Cp-m9-Z388GFSKeUyXsv-rauB0jNKp6BQRnlxZoflKYQJsUDpk0ii2VAAmduJZ79ncqyuejJyckRijhrWkWzQdbFiz-eH95xLciXrPprMBVDDup95_s81jAjIWJ2zO0_Vvg7RMNIY0weyX36A66oL9KS9GlkZb0tGOFrXJZG1qeio5LsvP1j8adtmGhcA_P6l8CXB8mMU-L_P21bFOIsgqlUTfYuhNPbsjZx-oTKNsr1Mf51XR7pGiYbdUIf9t9dCIsyAg_jKEyoBeTAvfn8UDCp2mnVMgiR8nYRmOZh3sRwrXcrFArpcZD-v49NFm-pUfsj1xZk6L2D77zIwAAAAG-IuuuAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://envs.sh/AJT.jpg"]
    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/AJ_.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/AJA.jpg"
STATS_IMG_URL = "https://telegra.ph/file/edd388a42dd2c499fd868.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
STREAM_IMG_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
