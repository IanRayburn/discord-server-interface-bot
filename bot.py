import os
from discord import Intents, Client, Message, File, Member
import logging

from responce_methods import get_file
import settings

TOKEN = settings.TOKEN
BOT_LOG_LOCATION = settings.BOT_LOG_LOCATION

logging.basicConfig(filename=BOT_LOG_LOCATION, filemode="a", format='%(asctime)s - %(message)s', level=logging.INFO)


intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

helper_message = "Get World File: '$get world'\nGet Bot Logs: '$get bot log'"

# Log start up
@client.event
async def on_ready() -> None:
    logging.info("Starting up")

# Introduce commands to new user
@client.event
async def on_member_join(member: Member):
    logging.info(f"{member.name} joined")
    member.send(helper_message) 

# Check message and preform requested command
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user : return

    if message.content[:5] == "$get ":
        file_location, file_type = get_file(message.content)
        match file_type:
            case "Unkown File Type":
                await message.channel.send(file_location)
                await message.channel.send(helper_message)
            case "Server log off":
                await message.channel.send(file_location)
                await message.channel.send(helper_message)
            case _:
                await message.channel.send(f"{file_type} File: ")
                await message.channel.send(file=File(file_location))
    elif message.content == "$help":
        await message.channel.send(helper_message)
    

'''
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
            if SERVER_LOG_ON:
                logging.info(f"Send Server Log file to {message.author}")
                await message.channel.send("Server Log File: ")
                await message.channel.send(file=File(SERVER_LOG_LOCATION))
            else:
                await message.channel.send("Server log access is not activated")

        case "help":
            await message.channel.send(helper_message)
        
        case _:
            await message.channel.send(f"{file_type} is invalid $get command")
            await message.channel.send(helper_message)
'''

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()