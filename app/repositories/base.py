from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select, delete
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.sync import update


class BaseRepository:
    model = None
    base_schema: BaseModel = None
    create_schema: BaseModel = None
    patch_schema: BaseModel = None
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, *args, **kwargs):
        query = select(self.model)
        result = await self.session.execute(query)
        models = result.scalars().all()
        return models

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalar()
        if model is None:
            return None
        return model

    async def add(self, data: create_schema):
        add_data_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(add_data_stmt)
        model = result.scalar()
        await self.session.commit()
        return model


    async def delete(self, **filter_by):
        delete_stmt = delete(self.model).filter_by(**filter_by)
        if not await self.get_one_or_none(**filter_by):
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} not found")
        delete_obj = await self.session.execute(delete_stmt)
        await self.session.commit()
        return delete_obj.scalar()

    async def update(self, data: create_schema, **filter_by):
        obj_to_update = await self.get_one_or_none(**filter_by)
        if obj_to_update is None:
            return None
        for key, value in data.dict().items():
            setattr(obj_to_update, key, value)
        await self.session.commit()
        return obj_to_update

    async def patch(self, data: create_schema, **filter_by):
        obj_to_update = await self.get_one_or_none(**filter_by)
        if obj_to_update is None:
            return None
        for key, value in data.dict().items():
            if value is not None:
                setattr(obj_to_update, key, value)
        await self.session.commit()
        return obj_to_update