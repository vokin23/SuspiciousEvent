from typing import List
from datetime import datetime
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
            # Check if a TypeEvent with the same name_en already exists
            existing_type_event_stmt = select(TypeEvent).filter_by(name_en=data.name_target_model)
            existing_type_event = await self.session.execute(existing_type_event_stmt)
            existing_type_event = existing_type_event.scalar()

            if existing_type_event is None:
                new_type_event_stmt = insert(TypeEvent).values(
                    name_en=data.name_target_model,
                    name_ru='',
                    description='',
                    status=False
                ).returning(TypeEvent)
                await self.session.execute(new_type_event_stmt)
                await self.session.commit()
                type_event = await self.session.execute(type_event_stmt)
                type_event = type_event.scalar()
            else:
                type_event = existing_type_event

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