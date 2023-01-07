import datetime

from pydantic import BaseModel


class MessageBase(BaseModel):
    channel_id: str
    author_nick: str
    raw_content: str
    created_at: datetime.datetime = datetime.datetime.utcnow()


class SeedMessage(MessageBase):
    ...


class FetchMessage(MessageBase):
    ...
