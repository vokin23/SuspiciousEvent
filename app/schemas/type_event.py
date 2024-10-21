from datetime import datetime

from pydantic import BaseModel


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