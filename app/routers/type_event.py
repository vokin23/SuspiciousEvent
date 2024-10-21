from typing import List
from app.schemas.type_event import TypeEvenCreatSchema, TypeEventSchema, TypeEventPutSchema, TypeEventPatchSchema
from fastapi import APIRouter
from fastapi.params import Query
from app.repositories.type_event import TypeEventRepository
from app.routers.dependencies import DBDep


type_event_crud_router = APIRouter(prefix="/type_event")


@type_event_crud_router.post("/create_type_event", summary="Создание типа события")
async def create_type_event(data: TypeEvenCreatSchema, db: DBDep) -> TypeEventSchema:
    return await TypeEventRepository(db).add(data)


@type_event_crud_router.get("/get_type_events", summary="Получение типов событий")
async def get_type_events(db: DBDep) -> List[TypeEventSchema]:
    return await TypeEventRepository(db).get_all()


@type_event_crud_router.get("/get_type_event", summary="Получение типа события")
async def get_type_event(db: DBDep, type_event_id: int = Query(description='ID типа события')) -> TypeEventSchema:
    return await TypeEventRepository(db).get_one_or_none(id=type_event_id)


@type_event_crud_router.put("/update_type_event", summary="Обновление типа события")
async def update_type_event(data: TypeEventPutSchema, db: DBDep,
                            type_event_id: int = Query(description='ID типа события')) -> TypeEventSchema:
    return await TypeEventRepository(db).update(data, id=type_event_id)


@type_event_crud_router.patch("/patch_type_event", summary="Обновление типа события")
async def patch_type_event(data: TypeEventPatchSchema, db: DBDep,
                           type_event_id: int = Query(description='ID типа события')) -> TypeEventSchema:
    return await TypeEventRepository(db).patch(data, id=type_event_id)


@type_event_crud_router.delete("/delete_type_event", summary="Удаление типа события")
async def delete_type_event(db: DBDep, type_event_id: int = Query(description='ID типа события')) -> TypeEventSchema:
    return await TypeEventRepository(db).delete(id=type_event_id)
