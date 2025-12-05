# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    coingecko_api_key: str
    internal_api_key: str = "mysecret" 
    
    # NEW: JWT Settings
    JWT_SECRET_KEY: str # Must be set in .env
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Token lifespan

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

settings = Settings()