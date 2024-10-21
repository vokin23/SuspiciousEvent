from typing import List

from fastapi import APIRouter
from fastapi.params import Query

from app.repositories.suspicious_event import SuspiciousEventRepository

from app.routers.dependencies import DBDep
from app.schemas.suspicious_event import SuspiciousEventCreateSchema, SuspiciousEventBaseSchema, \
    SuspiciousEventPatchSchemas

suspicious_event_crud_router = APIRouter(prefix="/suspicious_event")


# Работа с моделью SuspiciousEvent
@suspicious_event_crud_router.get("/get_suspicious_events", summary="Получение подозрительных событий")
async def get_suspicious_events(db: DBDep) -> List[SuspiciousEventBaseSchema]:
    return await SuspiciousEventRepository(db).get_all()


@suspicious_event_crud_router.get("/get_suspicious_event", summary="Получение подозрительного события")
async def get_suspicious_event(db: DBDep, suspicious_event_id: int = Query(description='ID подозрительного события')) -> SuspiciousEventBaseSchema:
    return await SuspiciousEventRepository(db).get_one_or_none(id=suspicious_event_id)



@suspicious_event_crud_router.post("/create_suspicious_event", summary="Создание подозрительного события")
async def create_suspicious_event(data: SuspiciousEventCreateSchema, db: DBDep):
    return await SuspiciousEventRepository(db).add(data)



@suspicious_event_crud_router.put("/update_suspicious_event", summary="Обновление подозрительного события")
async def update_suspicious_event(data: SuspiciousEventCreateSchema,
                                  db: DBDep,
                                  suspicious_event_id: int = Query(description='ID подозрительного события')) -> SuspiciousEventBaseSchema:
    return await SuspiciousEventRepository(db).update(data, id=suspicious_event_id)


@suspicious_event_crud_router.patch("/patch_suspicious_event", summary="Обновление подозрительного события")
async def patch_suspicious_event(data: SuspiciousEventPatchSchemas,
                                 db: DBDep,
                                 suspicious_event_id: int = Query(description='ID подозрительного события')) -> SuspiciousEventBaseSchema:
    return await SuspiciousEventRepository(db).patch(data, id=suspicious_event_id)


@suspicious_event_crud_router.delete("/delete_suspicious_event", summary="Удаление подозрительного события")
async def delete_suspicious_event(db: DBDep, suspicious_event_: int = Query(description='ID подозрительного события')):
    return await SuspiciousEventRepository(db).delete(id=suspicious_event_)
