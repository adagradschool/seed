from pydantic import BaseSettings, HttpUrl

class Settings(BaseSettings):
    TOKEN: str
    PERMISSIONS_INTEGER: int
    AUTH_URL: HttpUrl
    CLIENT_ID: int