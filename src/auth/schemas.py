from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    id: int
    username: str
    mail : str
    role : str
    firstname : str
    lastname
    TEXT
    NULL,
    isactive
    BOOL
    DEFAULT
    FALSE,
    superuser
    BOOL
    DEFAULT
    FALSE,