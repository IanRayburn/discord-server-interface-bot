import os

# .env setup
TOKEN: str = os.environ.get("TOKEN")
WORLD_LOCATION: str = os.environ.get("WORLD_LOCATION")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
SERVER_LOG_LOCATION: str = os.environ.get("SERVER_LOG_LOCATION")

# regular setup
BOT_LOG_LOCATION = "bot_log"

# Just pass a string to TOKEN & WORLDBACKUP_LOCATION if enter info in this file
# Make sure to pass a number to CHANNEL_ID