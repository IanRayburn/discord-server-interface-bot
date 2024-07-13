import os

# .env setup
TOKEN = os.getenv("TOKEN")
WORLDBACKUP_LOCATION = os.get("WORLDBACKUP_LOCATION")
CHANNEL_ID = os.get("CHANNEL_ID")

# Just pass a string to TOKEN & WORLDBACKUP_LOCATION if enter info in this file
# Make sure to pass a number to CHANNEL_ID