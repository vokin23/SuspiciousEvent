from app.repositories.base import BaseRepository
from app.models.suspicious_event import SuspiciousEvent
from app.schemas.suspicious_event import SuspiciousEventBaseSchema, SuspiciousEventCreateSchema


class SuspiciousEventRepository(BaseRepository):
    model = SuspiciousEvent
    base_schema = SuspiciousEventBaseSchema
    create_schema = SuspiciousEventCreateSchema


