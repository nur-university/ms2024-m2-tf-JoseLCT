from datetime import datetime
from uuid import uuid4, UUID

from geoalchemy2 import Geometry, WKBElement
from sqlalchemy import DateTime, Uuid, ForeignKey, Enum, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.core.utils import DatetimeUtils
from src.domain.package.types import PackageStatusType
from src.infrastructure.persistence.persistence_models import PersistenceDb


class PackageModel(PersistenceDb.Base):
    __tablename__ = "packages"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, default=uuid4)
    route_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("routes.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    delivery_order: Mapped[int] = mapped_column(Integer, default=0)
    tracking_number: Mapped[str] = mapped_column(String(6), unique=True, index=True)
    status: Mapped[PackageStatusType] = mapped_column(Enum(PackageStatusType), index=True)
    delivery_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    delivery_address: Mapped[str] = mapped_column(String(255))
    geographic_point: Mapped[WKBElement] = mapped_column(Geometry(geometry_type='POINT', srid=4326))

    created_at: Mapped[datetime] = mapped_column(DateTime, default=DatetimeUtils.get_utc_datetime)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=DatetimeUtils.get_utc_datetime,
        onupdate=DatetimeUtils.get_utc_datetime,
    )
