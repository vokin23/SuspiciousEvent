from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy import insert, select

from app.repositories.base import BaseRepository
from app.models.suspicious_event import SuspiciousEvent, TypeEvent
from app.schemas.suspicious_event import SuspiciousEventBaseSchema, SuspiciousEventCreateSchema


class SuspiciousEventRepository(BaseRepository):
    model = SuspiciousEvent
    base_schema = SuspiciousEventBaseSchema
    create_schema = SuspiciousEventCreateSchema

    async def add(self, data: SuspiciousEventCreateSchema):
        type_event_stmt = select(TypeEvent).filter_by(name_en=data.name_target_model, status=True)
        type_event = await self.session.execute(type_event_stmt)
        type_event = type_event.scalar()
        if type_event is None:
            raise HTTPException(status_code=404, detail=f"TypeEvent with name en {data.name_target_model} not found")
        add_data_stmt = insert(self.model).values(
            type_event=type_event.id,
            created_at=str(datetime.now()),
            was_notified=data.was_notified,
            description_event=data.description_event,
            user_initiated_event=data.user_initiated_event
        )
        await self.session.execute(add_data_stmt)
        await self.session.commit()

    async def get_all(self, *args, **kwargs) -> List[SuspiciousEventBaseSchema]:
        query = select(self.model)
        result = await self.session.execute(query)
        models = result.scalars().all()
        return models