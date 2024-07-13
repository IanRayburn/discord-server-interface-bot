import os
from discord import Intents, Client, Message, abc, File
import logging

import settings

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

TOKEN = settings.TOKEN
WORLD_LOCATION = settings.WORLD_LOCATION

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Log start up
@client.event
async def on_ready() -> None:
    logging.info("Starting up")


# Check message and preform requested command
@client.event
async def on_message(message: Message) -> None:
    if message.content[:5] == "$get ":
        file_type: str = message.content[5:]
    else:
        return

    match file_type:
        case "world": 
            await message.channel.send("Server World File: ")
            await message.channel.send(file=File(WORLD_LOCATION))
            logging.info(f"Sent World file to {message.author}")
        case "log":
            await message.channel.send("server log file: ")
            logging.info(f"Sent Log file to {message.author}")
        case _:
            await message.channel.send(f"{file_type} is invalid $get command")
            await message.channel.send("Try: '$get world' or '$get log'")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()