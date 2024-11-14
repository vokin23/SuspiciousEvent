from pydantic import BaseModel


class AuthSchema(BaseModel):
    login: str
    password: str

class AuthResponseSchema(BaseModel):
    access_token_sem: str