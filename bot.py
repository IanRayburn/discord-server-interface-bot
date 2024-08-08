from os import system
from discord import Intents, Client, Message, File, Member
import logging

from responce_methods import get_file
import settings

TOKEN = settings.TOKEN
BOT_LOG_LOCATION = settings.BOT_LOG_LOCATION
SERVER_START_FILE = settings.SERVER_START_FILE
SERVER_START_FILE_ON = settings.SERVER_START_FILE_ON

logging.basicConfig(filename=BOT_LOG_LOCATION, filemode="a", format='%(asctime)s - %(message)s', level=logging.INFO)


intents = Intents.default()
intents.message_content = True
intents.members = True
client = Client(intents=intents)

helper_message = "Get World File: '$get world'\nGet Bot Logs: '$get bot log'"

# Log start up
@client.event
async def on_ready() -> None:
    logging.info("Starting up")

# Introduce commands to new user
@client.event
async def on_member_join(member: Member) -> None:
    logging.info(f"{member.name} joined")
    await member.send(f"Commands:\n{helper_message}")
    await member.send("Send $help to get this message again.")

# Check message and preform requested command
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user : return

    if message.content[:5] == "$get ":
        file_location, file_type = get_file(message.content)
        try:
            logging.info(f"Trying to send file to {message.author}")
            await message.channel.send(f"{file_type}: ")
            await message.channel.send(file=File(file_location))
            logging.info(f"Sent {file_type} to {message.author}")
        except FileNotFoundError:
            logging.info(
                f"Could not send file to {message.author}, Error type: {file_location}"
                         )
            await message.channel.send(file_location)
            await message.channel.send(helper_message)

    elif message.content == "$help":
        await message.channel.send(helper_message)

    elif message.content == "$run":
        if SERVER_START_FILE_ON:
            system(f"./{SERVER_START_FILE}")
            await message.channel.send("Successfully ran server")
            logging.info(f"{message.author} successfully ran server file")
        else:
            await message.channel.send("Running server file is not activated")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()