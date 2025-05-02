
import os
import discord
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send('Hello there! 👋')

client.run(TOKEN)
