from typing import List

from fastapi import APIRouter

from app.routers.dependencies import DBDep
from app.schemas.suspicious_event import PostSuspiciousEventSchema, SuspiciousEventSchema, TypeEvenCreatSchema, \
    TypeEventSchema, TypeEventPatchSchema
from app.services.suspicious_event import SuspiciousEventService, TypeEventRepositoryService

suspicious_event_crud_router = APIRouter(prefix="/suspicious_event")


@suspicious_event_crud_router.post("", summary="Создание подозрительного события")
async def create_suspicious_event(data: PostSuspiciousEventSchema, db: DBDep):
    return await SuspiciousEventService(db).create_suspicious_event_service(data)


@suspicious_event_crud_router.get("", summary="Получение списка подозрительных событий")
async def get_suspicious_events(db: DBDep) -> List[SuspiciousEventSchema]:
    return await SuspiciousEventService(db).get_suspicious_events_service()


type_event_crud_router = APIRouter(prefix="/type_event")


@type_event_crud_router.post("", summary="Создание типа события")
async def create_type_event(data: TypeEvenCreatSchema, db: DBDep) -> TypeEventSchema:
    return await TypeEventRepositoryService(db).create_type_event_service(data)


@type_event_crud_router.get("", summary="Получение типов событий")
async def get_type_events(db: DBDep) -> List[TypeEventSchema]:
    return await TypeEventRepositoryService(db).get_all_service()


@type_event_crud_router.get("/{type_event_id}", summary="Получение типа события")
async def get_type_event(db: DBDep, type_event_id: int) -> TypeEventSchema:
    return await TypeEventRepositoryService(db).get_one_or_none_service(id=type_event_id)


@type_event_crud_router.patch("/{type_event_id}", summary="Обновление типа события")
async def patch_type_event(data: TypeEventPatchSchema, db: DBDep,
                           type_event_id: int) -> TypeEventSchema:
    return await TypeEventRepositoryService(db).patch_service(data, id=type_event_id)


@type_event_crud_router.delete("/{type_event_id}", summary="Удаление типа события")
async def delete_type_event(db: DBDep, type_event_id: int) -> TypeEventSchema:
    return await TypeEventRepositoryService(db).delete_type_event_service(id=type_event_id)
