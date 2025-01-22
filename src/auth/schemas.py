from pydantic import BaseModel, ConfigDict


class UserLogin(BaseModel):
    username: str
    password: str