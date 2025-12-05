# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    coingecko_api_key: str
    internal_api_key: str = "mysecret"   # change in .env for production

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

settings = Settings()
