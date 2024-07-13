import os
from discord import Intents, Client, Message, abc, File
import logging

import settings

TOKEN = settings.TOKEN
WORLD_LOCATION = settings.WORLD_LOCATION
BOT_LOG_LOCATION = settings.BOT_LOG_LOCATION
SERVER_LOG_LOCATION = settings.SERVER_LOG_LOCATION

logging.basicConfig(filename=BOT_LOG_LOCATION, filemode="a", format='%(asctime)s - %(message)s', level=logging.INFO)


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
        case "bot log":
            logging.info(f"Sent Bot Log file to {message.author}")
            await message.channel.send("Bot Log File: ")
            await message.channel.send(file=File(BOT_LOG_LOCATION))
        case "server log":
            logging.info(f"Send Server Log file to {message.author}")
            await message.channel.send("Server Log File: ")
            await message.channel.send(file=File(SERVER_LOG_LOCATIONj))
        case _:
            await message.channel.send(f"{file_type} is invalid $get command")
            await message.channel.send("Try: '$get world' or '$get log'")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()