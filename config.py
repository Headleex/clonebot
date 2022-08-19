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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5403229743:AAG8h1K4oaZQyctrmd4kqtCiJ1o41nZR4P8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "15916772"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "c486bad713b20920b073bbbb41c66894")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BADy3uQAjlJq-u6JJW5BxhJNfLvdv9GWnTdEdAIPi7OlEXd1j-D1aBmQVfhh0R4t1zueTuZoB9PbVGENzcuIlFMGQvhm6OiEXrcQK_kN1GNEairvL5GnRFskvSTl9hJ_vVP05uWw3vjFQ4GXkl7vNCcSL46XmqIKRis-NWbRGoWGxE2HdW_T_6utOQw7lbcdcXWO6-BNt04AKeoShB87HPMeAxu6ToSFILIZxMfFCuH0RsGeQub-L9Z3xGayMWYTDsc9frcC5YfFI4rNmHXXex1STxDc3b7hPg7IuTmJmB3LBEVnBCd5cfKz3p3QOZJuHjDjojOH0y4f0QEaV3Fu078qDHUkeAAAAAFEV819AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
