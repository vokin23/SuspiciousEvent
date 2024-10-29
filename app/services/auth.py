from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext
import jwt
from app.config import settings


class AuthService:
    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    def decode_access_token(self, data: dict) -> str | None:
        try:
            return jwt.decode(data, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        except:
            return None

    