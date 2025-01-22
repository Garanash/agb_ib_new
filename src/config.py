from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'FastAPI app'
    description: str = 'It was lot of fun'
    database_url: str = 'sqlite+asyncio:///database.db'
    secret: str = 'SECRET'
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 50
    max_iverflow: int = 10

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()