from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from sqlalchemy import NullPool

DATABASE_URL = settings.db_url
engine = create_async_engine(DATABASE_URL, future=True) # Базовый асинк engine для работы с бд
engine_null_pool = create_async_engine(DATABASE_URL, poolclass=NullPool) # null_pool асинк engine для работы с бд в селари или в тестах
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
async_session_maker_null_pool = async_sessionmaker(bind=engine_null_pool, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
