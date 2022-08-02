#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5435688482:AAHvBLhG-IpDlAVVimCWQe2iwnBiUQuNoI8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "2573266"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "6969659cf50a9b0bb20ec8d06b61c27b")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AgAnQ9IAY1nu_L8j2-RMLMWIb-0nGybytvpyDQ0DU6zdkMbuo3MfFdvhQx3I--KB7cIGtT9yhxujMy8Nk0DqTdgQ9BoDs0Zi-Tqgbf_Mj6FIo9WDJQmhOhd7Le0K6tNuLFH6_Z4f61O0Dv3Kto6T-FdZ_Ma2pjxPwIF7HPJxyyg9eNuVYz9WanBc2NxKpEu5Y6KCJ5O-y1ZPfUGxlFSRFn-v2dZNIcFgr_QToj30F3mfXKOGtNj2NEpkmllT4ZrNyMg04jme7sRcR7AVybP9W5aT3cFmEWde_CLcZlrCK1AKYH2HLplBb7WjTRW2kUFXFgfFQICHngw_esSy__quF5B5v0FKswAAAAAaLxdBAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
