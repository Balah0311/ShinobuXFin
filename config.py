import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", ""))

OWNER_ID = int(getenv("OWNER_ID", "1471469091"))

START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAEL5olmGPWEXFq5JVQtvFpiKqx1mY3F4AACBwgAAssdOVf48RP1cE0UejQE")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Idhaya X Music")

POWERED_BY = getenv("POWERED_BY", "𝐈𝐃𝐇𝐀𝐘𝐀𝐍ᥫ᭡")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Balah0311/ShinobiXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shinobuupdates_2")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/shinobusupport_1")

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "30000"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "300"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))



# Get your pyrogram v2 session from @TBN_StringGeneratorRobot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/c00f7bc800cbe221465ba.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/ceb40a2b642db9aff9a1a.jpg"
)
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://telegra.ph/file/3016c891e6c06ec3d21a5.jpg"
)
STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://telegra.ph/file/6b171c95d37b42aaf6c9e.jpg"
)
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/bd9d9956eb18ad06ef0a2.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/6eedbaf9e81c2d051e60f.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/df35660a5cbb6f3909a9c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7350bd3be7ff08a503f51.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/8737c03dc5a33fb87fbfb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/137a849a5265ca8121717.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/137a849a5265ca8121717.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/3016c891e6c06ec3d21a5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
