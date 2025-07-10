import discord # Discord Library
from discord.ext import commands # Commands from discord extensions
import logging # Logs content
from dotenv import load_dotenv # Loads environment variable files
import os # Allows us to access our environment variables

# Loads .env file
load_dotenv() 
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="gm!", intents = intents)

@bot.event
async def on_ready():
    print(f"good morning! {bot.user.name} is ready!")

@bot.event
async def on_member_join():
    pass

bot.run(token, log_handler=handler, log_level=logging.DEBUG)