from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from src.core.config import Environment


class PersistenceDb:
    _environment = Environment()
    _async_engine = create_async_engine(
        _environment.async_database_url,
        echo=False,
        pool_pre_ping=True,
    )
    _AsyncSessionFactory = async_sessionmaker(
        bind=_async_engine,
        expire_on_commit=False,
        autoflush=False,
        class_=AsyncSession,
    )
    Base = declarative_base()

    @classmethod
    async def get_session(cls) -> AsyncGenerator[AsyncSession, None]:
        async with cls._AsyncSessionFactory() as session:
            try:
                yield session
            finally:
                await session.close()
