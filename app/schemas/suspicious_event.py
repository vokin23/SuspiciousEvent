from pydantic import BaseModel


class PostSuspiciousEventSchema(BaseModel):
    request: dict | None
    right_name: str | None
    user_id: int | None


class CreateSuspiciousEventSchema(BaseModel):
    type_event: int
    created_at: str
    was_notified: bool
    description_event: str
    user_initiated_event: int


class SuspiciousEventSchema(BaseModel):
    id: int
    type_event: int
    created_at: str | None
    was_notified: bool | None
    description_event: str | None
    user_initiated_event: int | None


class TypeEvenCreatSchema(BaseModel):
    name_en: str
    name_ru: str
    description: str | None
    status: bool


class TypeEventSchema(TypeEvenCreatSchema):
    id: int


class TypeEventPutSchema(BaseModel):
    name_en: str
    name_ru: str
    description: str
    status: bool


class TypeEventPatchSchema(BaseModel):
    name_en: str | None = None
    name_ru: str | None = None
    description: str | None = None
    status: bool | None = None
