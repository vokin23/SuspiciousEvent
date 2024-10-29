from pydantic import BaseModel


class AuthSchema(BaseModel):
    user_id: int

class AuthResponseSchema(BaseModel):
    access_token_sem: str