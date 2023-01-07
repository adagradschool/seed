import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path('config/local.env'))
from core.config import Settings
settings = Settings()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(settings.TOKEN)