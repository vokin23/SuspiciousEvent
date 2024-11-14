# app/repositories/auth.py
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.schemas.auth import AuthSchema
from app.services.auth import AuthService


class AuthRepository:
    base_schema: BaseModel = AuthSchema
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def auth(self, data):
        login = data.login
        password = data.password

        if login != AuthService().login:
            raise HTTPException(status_code=403, detail="Access forbidden: User login is incorrect")

        if AuthService().verify_password(password, AuthService().hashed_password):
            access_token = AuthService().create_access_token({"login": login})
            return {"access_token_sem": access_token}
        else:
            raise HTTPException(status_code=401, detail="Access forbidden: User is not root")
