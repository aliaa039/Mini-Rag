from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List
import os
from pathlib import Path

# Get the src directory (where .env is located)
SRC_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: List[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    class Config:
        env_file = os.path.join(SRC_DIR, ".env")
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()