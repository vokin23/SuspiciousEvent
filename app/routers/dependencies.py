from typing import Annotated

from fastapi import Depends

from app.datebase import async_session_maker
from app.utils.db_manager import DBManager


def get_db_manager():
    return


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]