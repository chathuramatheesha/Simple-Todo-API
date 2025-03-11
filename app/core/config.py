from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite+aiosqlite:///test.db"
    SECRET_KEY: str = "fastapi-secret-key-placeholder"
    ALGORITHM: str = "HS256"
    HOST: str = "127.0.0.1"
    PORT: int = 3000

    class Config:
        env_file = ".env"


settings = Settings()
