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

# Check message and preform requested command
@client.event
async def on_message(message: Message) -> None:
    if message.content[:5] == "$get ":
        user_message: str = message.content[5:]
    else:
        return

    if user_message == "world":
        await message.channel.send("Server World File: ")
    elif user_message == "log":
        await message.channel.send("Server Log File: ")
    else: 
        await message.channel.send(f"{user_message} is invalid $get command")
        await message.channel.send("Try: '$get world' or '$get log'")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()