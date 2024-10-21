from datetime import datetime

from sqlalchemy import insert

from app.repositories.base import BaseRepository
from app.models.suspicious_event import SuspiciousEvent
from app.schemas.suspicious_event import SuspiciousEventBaseSchema, SuspiciousEventCreateSchema


class SuspiciousEventRepository(BaseRepository):
    model = SuspiciousEvent
    base_schema = SuspiciousEventBaseSchema
    create_schema = SuspiciousEventCreateSchema


    async def add(self, data: create_schema) -> base_schema:
        add_data_stmt = insert(self.model).values(
            name_target_model=data.name_target_model,
            type_event=data.type_event,
            created_at=str(datetime.now()),
            was_notified=data.was_notified,
            description_event=data.description_event,
            user_initiated_event=data.user_initiated_event
        ).returning(self.model)
        result = await self.session.execute(add_data_stmt)
        model = result.scalar()
        await self.session.commit()
        return model