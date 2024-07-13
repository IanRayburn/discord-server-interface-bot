import os
from discord import Intents, Client, Message
import logging

import settings

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

TOKEN = settings.TOKEN
CHANNEL_ID = settings.CHANNEL_ID
WORLDBACKUP_LOCATION = settings.WORLDBACKUP_LOCATION

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()