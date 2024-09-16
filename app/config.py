import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    debug: bool = False
    database_url: str = "postgresql://postgres:qwerty@localhost:5432/postgres"
    fastapi_env: str

    class Config:
        env_file = ".env"

settings = Settings()