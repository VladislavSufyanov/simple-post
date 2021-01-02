from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
