from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.datebase import Base


class SuspiciousEvent(Base):
    __tablename__ = 'suspicious_event'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_target_model: Mapped[str] = mapped_column(String(100))
    type_event: Mapped[str] = mapped_column(String(100))
    event_created_at: Mapped[datetime] = mapped_column(DateTime)
    was_notified: Mapped[bool] = mapped_column(default=False)
    description_event: Mapped[str] = mapped_column(String(255))
    user_initiated_event: Mapped[int] = mapped_column()
