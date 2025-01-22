from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool, echo_pool: str, pool_size: int = 5, max_overflow: int = 10):
        self.engine = create_async_engine(url=url,
                                          echo=echo,
                                          echo_pool=echo_pool,
                                          pool_size=pool_size,
                                          max_owerflow=max_overflow,
                                          )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.engine,
                                                                                    autoflush=False,
                                                                                    autocommit=False,
                                                                                    expire_on_commit=False,
                                                                                    )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(settings.database_url,
                           settings.echo,
                           settings.echo_pool,
                           settings.pool_size,
                           settings.max_iverflow
                           )
