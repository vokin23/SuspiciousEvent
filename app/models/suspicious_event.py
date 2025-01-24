from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class TypeEvent(Base):
    __tablename__ = 'type_event'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_en: Mapped[str] = mapped_column(String(100), unique=True)
    name_ru: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255), nullable=True, default=None)
    status: Mapped[bool] = mapped_column(default=False)


class SuspiciousEvent(Base):
    __tablename__ = 'suspicious_event'

    id: Mapped[int] = mapped_column(primary_key=True)
    type_event: Mapped[int] = mapped_column(ForeignKey('type_event.id'))
    created_at: Mapped[str] = mapped_column(String(255), default=None, nullable=True)
    was_notified: Mapped[bool] = mapped_column(default=False)
    description_event: Mapped[str] = mapped_column(String(255), default=None, nullable=True)
    user_initiated_event: Mapped[int] = mapped_column()
