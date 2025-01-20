from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
# from src.core.db import search

router = APIRouter(prefix='/auth', tags=['Auth'])

security = HTTPBasic()


@router.post('/autorize_me')
def basic_auth(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    print(credentials.username, credentials.password)
    return f'hello {credentials.username}'
