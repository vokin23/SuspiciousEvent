from datetime import datetime
from sqlalchemy import insert, select

from app.repositories.base import BaseRepository
from app.models.suspicious_event import SuspiciousEvent, TypeEvent
from app.schemas.suspicious_event import CreateSuspiciousEventSchema, TypeEventSchema, TypeEvenCreatSchema, \
    TypeEventPatchSchema


class SuspiciousEventRepository(BaseRepository):
    model = SuspiciousEvent

    async def add(self, data: CreateSuspiciousEventSchema):
        query = select(self.model).values(data.model_dump())
        await self.session.execute(query)
        await self.session.commit()


class TypeEventRepository(BaseRepository):
    model = TypeEvent
    base_schema = TypeEventSchema
    create_schema = TypeEvenCreatSchema
    patch_schema = TypeEventPatchSchema

    async def add(self, data: create_schema):
        add_data_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(add_data_stmt)
        model = result.scalar()
        await self.session.commit()
        return model

    async def get_type_event_by_filter(self, **kwargs) -> TypeEventSchema:
        query = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(query)
        models = result.scalars().all()
        return models
