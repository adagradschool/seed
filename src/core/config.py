from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, HttpUrl

load_dotenv(dotenv_path=Path("config/local.env"))


class Settings(BaseSettings):
    TOKEN: str
    PERMISSIONS_INTEGER: int
    AUTH_URL: HttpUrl
    CLIENT_ID: int
