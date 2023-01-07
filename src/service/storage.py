import random
import typing as t

from core.exceptions import InvalidChannelException
from schemas import SeedMessage

DB: t.Dict[str, t.List[SeedMessage]] = {}


def store_message(message: SeedMessage):
    if message.channel_id in DB:
        DB[message.channel_id].append(message)
    else:
        DB[message.channel_id] = [message]


def fetch_message(channel_id: str) -> SeedMessage:
    if channel_id not in DB:
        raise InvalidChannelException(f"No messages saved for {channel_id}")
    return random.choice(DB[channel_id])
