from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from src.core.db_users import search_user_by_username,search_user_by_id
from authx import AuthX, AuthXConfig
from schemas import UserLogin

router = APIRouter(prefix='/auth', tags=['Auth'])

config = AuthXConfig()
config.JWT_SECRET_KEY = 'AGB_ib'
config.JWT_ACCESS_COOKIE_NAME = 'my_access_token'
config.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config)


@router.post('/autorize_me')
def basic_auth(
        credentials: UserLogin,
        response: Response
):
    user = search_user_by_username(credentials.username)
    """
    ДОПИСАТЬ АВТОРИЗАЦИЮ
    """
    ...
    response.set_cookie()
    return f'hello {credentials.username}'
