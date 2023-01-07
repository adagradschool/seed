from core.exceptions import InvalidChannelException
from schemas import SeedMessage


def respond_to_seed_message(message: SeedMessage) -> str:
    return f"Ah, nice! I see you're a person of culture, {message.author_nick}."


def respond_to_fetch_message(message: SeedMessage) -> str:
    stripped_content = message.raw_content.lstrip("!seed ")
    return f"I remember {message.author_nick} recommended this!\n{stripped_content}\n Happy Watching! 🍿"


def handle_empty_fetch(e: InvalidChannelException) -> str:
    return str(e)
