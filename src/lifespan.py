from contextlib import asynccontextmanager
from core.db_helper import db_helper
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

    await db_helper.dispose()