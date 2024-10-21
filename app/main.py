import uvicorn
from contextlib import asynccontextmanager

from app.init import redis_manager
from fastapi import FastAPI, APIRouter
from fastapi.openapi.docs import get_swagger_ui_html

from app.routers.crud import suspicious_event_crud_router


@asynccontextmanager
async def lifespan(add: FastAPI):
    await redis_manager.redis_connect()
    print("Connecting to Redis")
    yield
    await redis_manager.redis_close()
    print("Disconnecting from Redis")


main_router = APIRouter(prefix='/v1')

main_router.include_router(suspicious_event_crud_router)
app = FastAPI(lifespan=lifespan)
app.include_router(main_router, tags=["CRUD"])



@main_router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)