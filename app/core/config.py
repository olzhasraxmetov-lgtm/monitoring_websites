from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MODE: Literal["TEST", "LOCAL", "DEV", "PROD"]

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    APP_NAME: str = 'Monitoring Websites Project'
    APP_DESCRIPTION: str = 'Monitoring Websites Project'
    APP_VERSION: str = '0.0.1'

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
        env_file_encoding='utf-8',
    )


settings = Settings()  # type: ignore