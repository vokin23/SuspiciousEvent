from fastapi import APIRouter, HTTPException, Response
from app.repositories.auth import AuthRepository
from app.routers.dependencies import DBDep
from app.schemas.auth import AuthSchema, AuthResponseSchema

auth_router = APIRouter(prefix="/auth")
ping_router = APIRouter(prefix="/ping", tags=["Проверка доступности"])


@ping_router.get("/ping")
async def ping():
    return {"status": "OK"}


@auth_router.post("/login")
async def login(
        data: AuthSchema,
        response: Response,
        db: DBDep
) -> AuthResponseSchema:
    access_token_data = await AuthRepository(db).auth(data)
    access_token_sem = access_token_data["access_token_sem"]
    if access_token_sem is None:
        raise HTTPException(status_code=401, detail="Access forbidden: User is not root")
    else:
        response.set_cookie("access_token_sem", access_token_sem)
        print(AuthResponseSchema(access_token_sem=access_token_sem))
        return AuthResponseSchema(access_token_sem=access_token_sem)