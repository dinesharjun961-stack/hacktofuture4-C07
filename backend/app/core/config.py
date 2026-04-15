from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RedBlueAI"
    DEBUG: bool = True
    DATABASE_URL: str
    REDIS_URL: str
    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
