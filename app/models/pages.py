from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from sqlalchemy import String, DateTime, func


class PagesORM(Base):
    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())