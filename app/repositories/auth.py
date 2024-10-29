from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import AuthSchema
from app.services.auth import AuthService


class AuthRepository:
    base_schema: BaseModel = AuthSchema
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def auth(self, data: base_schema):
        user_id = data.user_id

        result = await self.session.execute(
            text("""
                    SELECT ur.name
                    FROM UserSettings us
                    JOIN UserRole ur ON us.user_role_id = ur.id
                    WHERE us.user_id = :user_id
                """), {"user_id": user_id}
        )
        user_role = result.scalar()

        if user_role == "root_role":
            access_token = AuthService().create_access_token({"user_id": user_id})
            return {"access_token_sem": access_token}
        else:
            raise HTTPException(status_code=401, detail="Access forbidden: User is not root")