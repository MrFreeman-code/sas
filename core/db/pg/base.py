from pytest_asyncio.plugin import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession)

from core.config import settings


class DBSessionManager:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10
        ):
            """ Create async engine for connect in DB"""
            self.engine: AsyncEngine = create_async_engine(
                url=url,
                echo=echo,
                echo_pool=echo_pool,
                pool_size=pool_size,
                max_overflow=max_overflow
            )
            """ Create a session factory to get an AsyncSession for database operations"""
            self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
                bind=self.engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False
            )
    async def dispose(self) -> None:
        """ Close engine and connections"""
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        """ Create and close async session"""
        async with self.session_factory() as session:
            yield session


db_session_manager = DBSessionManager(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow
)