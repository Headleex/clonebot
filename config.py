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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BADy3uQAwDR5JKezYCTkqjxlYJtCDAfMinBjug7wuojel7ramYUaPcBkIH7KQWxxAMs7WJmESW0u_KK92yQkPiPss79S3o6iC0wZOcah4CRUhleyofnb0f6WfEFU5jTAdqVIXaIuGkOpZx6rHcMVjMb3BYUhVCQZdbx6F0I2XssBbYj-kjo4_wznsIMdH4P9v-eSALHPKKE0PjbBPLVmJAV9NGoeJ9kCLvgTfoeP_KrbEf4y1j5n0l5s8rmJF6qfNOHdoaeOulwAC7pktJdkmbaWiwe-a3QS3l-ilM-wmUrDwhOlYCI7s3rxY8bIDoP14ySJBIlEUyVQodqWdldHXXx5HVI1BAAAAAFEV819AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
