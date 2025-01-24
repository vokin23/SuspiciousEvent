from datetime import datetime
from typing import List

from app.schemas.suspicious_event import PostSuspiciousEventSchema, CreateSuspiciousEventSchema, SuspiciousEventSchema, \
    TypeEventPatchSchema, TypeEvenCreatSchema
from app.services.base import BaseService


class SuspiciousEventService(BaseService):

    async def create_suspicious_event_service(self, data: PostSuspiciousEventSchema):
        user_id = data.user_id
        if data.request and data.right_name:
            type_event = data.right_name.lower()
            bd_type_event = await self.db.type_event.get_type_event_by_filter(name_en=type_event)
            if bd_type_event:
                type_event_id = bd_type_event[0].id
            else:
                type_event_id = (await self.db.type_event.add(
                    TypeEvenCreatSchema(name_en=type_event, name_ru="", description="", status=False))).id
            request = data.request
            was_notified = True
            description_event = None
            deleted_user_id = request.get("path").split('/')[-1]
            if request.get("method") == 'DELETE':
                description_event = f"User {user_id} deleted user: {deleted_user_id}. {type_event} event type."
            elif request.get("method") == 'PATCH':
                description_event = f"System user {user_id} patch user: {deleted_user_id}. {type_event} event type."

            await self.db.suspicious_event.add(CreateSuspiciousEventSchema(type_event=type_event_id,
                                                                           created_at=str(datetime.now()),
                                                                           was_notified=was_notified,
                                                                           description_event=description_event,
                                                                           user_initiated_event=user_id))

    async def get_suspicious_events_service(self) -> List[SuspiciousEventSchema]:
        return await self.db.suspicious_event.get_all()


class TypeEventRepositoryService(BaseService):

    async def create_type_event_service(self, data: TypeEvenCreatSchema):
        return await self.db.type_event.add(data)

    async def get_all_service(self):
        return await self.db.type_event.get_all()

    async def get_one_or_none_service(self, id: int):
        return await self.db.type_event.get_one_or_none(id=id)

    async def patch_service(self, data: TypeEventPatchSchema, id: int):
        return await self.db.type_event.patch(data, id=id)

    async def delete_type_event_service(self, id: int):
        return await self.db.type_event.delete(id=id)
