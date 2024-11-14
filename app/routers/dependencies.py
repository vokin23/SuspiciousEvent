from typing import Annotated

from fastapi import Depends, HTTPException, Request
from app.services.auth import AuthService
from app.database import async_session_maker
from app.utils.db_manager import DBManager


def get_db_manager():
    return


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]

async def get_current_user(request: Request):
    token = request.cookies.get("access_token_sem") or request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=403, detail="Not authenticated")

    user_data = AuthService().decode_token(token)
    if user_data is None:
        raise HTTPException(status_code=403, detail="Invalid token")

    return user_data