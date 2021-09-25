import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCRBmDo8K6fANCPAYbZNjd2mq0QNjW4s-n98Z0Q4j-k4Ua5FGoIQq0UNDYfz_KMVURhPCJ04fHZmqrIUJcmXAxd-6JYcg0wiTg9CVPjymG5IaYIOs5BbcUQhRIQ8yNGdZ1oym9MabEIzDrNlotNhUnUgExEaWNvKaO1kb5jMjpudq8n5DSDCx-Vo8Bq8ecamgldmKlWR3kAe318mqa6ACYPzpyrQP2bo28tmJsjkFDJyZV6qzteBUztLBMAijyits4ytg62kucVwG1YY5dCitjiBrmEcqEix7Vnb3R4VDfPgg7ZG5CLPsHmlvdL6eq61jaU7fxSKsqJwIeTj3yHxwMoXkcHrAA")
BOT_TOKEN = getenv("BOT_TOKEN","1940261617:AAE-fCJODko9gAuQYI8J2RvDkIF5mo-K3Ho")
BOT_NAME = getenv("BOT_NAME","taskil")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","yahaluwo")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {1581713324}
API_ID = int(getenv("API_ID","8267931"))
API_HASH = getenv("API_HASH","4721285cd3901fde69a387d69954dd7b")
BOT_USERNAME = getenv("BOT_USERNAME","music_player_yahaluwo_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME","@music_player_s")
OWNER_NAME = getenv("OWNER_NAME", "@praveenkawshalya")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "chat_with_friends_sl")
PROJECT_NAME = getenv("PROJECT_NAME","taskilmusicbot")
SOURCE_CODE = getenv("SOURCE_CODE","https://t.me/chat_with_friends_sl")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
ARQ_API_KEY = getenv("ARQ_API_KEY","KWTPVR-QZIHPO-FQRBFT-YMCFPO-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "797768146").split()))
