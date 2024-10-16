from pydantic import BaseModel


class SuspiciousEventCreateSchema(BaseModel):
    name_target_model: str
    type_event: str
    event_created_at: str
    was_notified: bool
    description_event: str
    user_initiated_event: int


class SuspiciousEventBaseSchema(SuspiciousEventCreateSchema):
    id: int


class SuspiciousEventUpdateSchema(SuspiciousEventCreateSchema):
    pass


class SuspiciousEventPatchSchemas(BaseModel):
    name_target_model: str | None = None
    type_event: str | None = None
    event_created_at: str | None = None
    was_notified: bool | None = None
    description_event: str | None = None
    user_initiated_event: int | None = None
