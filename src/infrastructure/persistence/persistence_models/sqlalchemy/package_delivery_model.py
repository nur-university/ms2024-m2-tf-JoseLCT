from datetime import datetime
from uuid import uuid4, UUID

from geoalchemy2 import Geometry, WKBElement
from sqlalchemy import DateTime, Uuid, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.utils import DatetimeUtils
from src.infrastructure.persistence.persistence_models import PersistenceDb


class PackageDeliveryModel(PersistenceDb.Base):
    __tablename__ = "package_deliveries"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, default=uuid4)
    package_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("packages.id", ondelete="CASCADE"), index=True)
    route_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("routes.id", ondelete="SET NULL"), nullable=True, index=True)
    delivery_date: Mapped[datetime] = mapped_column(DateTime)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    geographic_point: Mapped[WKBElement] = mapped_column(Geometry(geometry_type='POINT', srid=4326))

    created_at: Mapped[datetime] = mapped_column(DateTime, default=DatetimeUtils.get_utc_datetime)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=DatetimeUtils.get_utc_datetime,
        onupdate=DatetimeUtils.get_utc_datetime,
    )
