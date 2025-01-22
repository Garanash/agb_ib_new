from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    database_url: str = 'sqlite+asyncio:///database.db'
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 50
    max_iverflow: int = 10


class SecretSettings(BaseModel):
    secret: str = 'SECRET'


class Discription(BaseSettings):
    app_title: str = 'FastAPI app'
    description: str = 'It was lot of fun'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="AGB_CONFIG__"
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix - ApiPrefix()
    database_config: DatabaseConfig = DatabaseConfig()
    discription: Discription = Discription()
    secret: SecretSettings = SecretSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings(

)
