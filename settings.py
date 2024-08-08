import os

TOKEN: str = os.environ.get("TOKEN")

WORLD_LOCATION: str = os.environ.get("WORLD_LOCATION")
SERVER_LOG_LOCATION: str = os.environ.get("SERVER_LOG_LOCATION")
SERVER_START_FILE: str = os.environ.get("SERVER_START_FILE") # Has to be a bash script
BOT_LOG_LOCATION = "bot_log.txt"

SERVER_LOG_ON = False
SERVER_START_FILE_ON = True