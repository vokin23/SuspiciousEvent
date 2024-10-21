from alembic.util import status
from fastapi import HTTPException
from sqlalchemy import insert
from datetime import datetime

from app.models.suspicious_event import TypeEvent
from app.repositories.base import BaseRepository
from app.schemas.type_event import TypeEventSchema, TypeEvenCreatSchema, TypeEventPatchSchema


class TypeEventRepository(BaseRepository):
    model = TypeEvent
    base_schema = TypeEventSchema
    create_schema = TypeEvenCreatSchema
    patch_schema = TypeEventPatchSchema

    async def add(self, data: create_schema):
        if await self.get_one_or_none(name_en=data.name_en) is not None:
            raise HTTPException(status_code=400, detail=f"TypeEvent with name en {data.name_en} already exists")
        elif await self.get_one_or_none(name_ru=data.name_ru) is not None:
            raise HTTPException(status_code=400, detail=f"TypeEvent with name ru {data.name_ru} already exists")
        add_data_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(add_data_stmt)
        model = result.scalar()
        await self.session.commit()
        return model