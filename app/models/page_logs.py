from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from sqlalchemy import DateTime, func, ForeignKey, Integer, Float


class PageLogsORM(Base):
    __tablename__ = 'page_logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id', ondelete='CASCADE'), nullable=False)
    status_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    response_time: Mapped[float | None] = mapped_column(Float, nullable=True)
    checked_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())