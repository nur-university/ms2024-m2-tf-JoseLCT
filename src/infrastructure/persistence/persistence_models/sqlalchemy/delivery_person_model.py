from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import String, Boolean, DateTime, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from src.core.utils import DatetimeUtils
from src.infrastructure.persistence.persistence_models import PersistenceDb


class DeliveryPersonModel(PersistenceDb.Base):
    __tablename__ = "delivery_persons"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, default=uuid4)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=DatetimeUtils.get_utc_datetime)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=DatetimeUtils.get_utc_datetime,
        onupdate=DatetimeUtils.get_utc_datetime,
    )
