import discord
from discord.ext import commands

from core.config import Settings
from core.exceptions import InvalidChannelException
from schemas import SeedMessage
from service.message import (
    handle_empty_fetch,
    respond_to_fetch_message,
    respond_to_seed_message,
)
from service.storage import fetch_message, store_message

settings = Settings()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.content.startswith("!seedfetch"):
        try:
            fetched_message = fetch_message(str(message.channel.id))
            await message.channel.send(respond_to_fetch_message(fetched_message))
        except InvalidChannelException as e:
            await message.channel.send(handle_empty_fetch(e))

    elif message.content.startswith("!seed"):
        seed_message = SeedMessage(
            author_nick=message.author.display_name,
            raw_content=message.content,
            channel_id=message.channel.id,
        )
        store_message(seed_message)
        await message.channel.send(respond_to_seed_message(seed_message))


client.run(settings.TOKEN)
