from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import DateTime, Uuid, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.core.utils import DatetimeUtils
from src.domain.route.types import RouteStatusType
from src.infrastructure.persistence.persistence_models import PersistenceDb


class RouteModel(PersistenceDb.Base):
    __tablename__ = "routes"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, default=uuid4)
    delivery_person_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("delivery_persons.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    execution_date: Mapped[datetime] = mapped_column(DateTime, index=True)
    status: Mapped[RouteStatusType] = mapped_column(Enum(RouteStatusType), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=DatetimeUtils.get_utc_datetime)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=DatetimeUtils.get_utc_datetime,
        onupdate=DatetimeUtils.get_utc_datetime,
    )
