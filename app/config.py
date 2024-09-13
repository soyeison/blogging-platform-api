import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    debug: bool = False
    database_url: str
    fastapi_env: str

    class Config:
        env_file = ".env"

settings = Settings()

if os.getenv("FASTAPI_ENV") == "production":
    settings.Config.env_file = ".env.production"