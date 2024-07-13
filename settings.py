import os

# .env setup
TOKEN: str = os.environ.get("TOKEN")
WORLD_LOCATION: str = os.environ.get("WORLD_LOCATION")
SERVER_LOG_LOCATION: str = os.environ.get("SERVER_LOG_LOCATION")

# regular setup
BOT_LOG_LOCATION = "bot_log.txt"
SERVER_LOG_ON = False

# Just pass a string to TOKEN & WORLDBACKUP_LOCATION if enter info in this file