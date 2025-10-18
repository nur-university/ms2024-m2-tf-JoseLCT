from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from src.core.abstractions import AggregateRoot
from src.domain.package.entities import PackageDeliveryEntity
from src.domain.package.events import PackageDeliveredEvent
from src.domain.package.types import PackageStatusType
from src.domain.shared.value_objects import GeographicPointValue


class PackageEntity(AggregateRoot):
    def __init__(
            self,
            id: UUID,
            tracking_number: str,
            status: PackageStatusType,
            delivery_date: datetime,
            delivery_address: str,
            geographic_point: GeographicPointValue,
            route_id: Optional[UUID] = None,
            delivery_order: Optional[int] = None,
    ):
        super().__init__(id)
        self._tracking_number = tracking_number
        self._status = status
        self._delivery_date = delivery_date
        self._delivery_address = delivery_address
        self._geographic_point = geographic_point
        self._route_id = route_id
        self._delivery_order = delivery_order

    @property
    def tracking_number(self) -> str:
        return self._tracking_number

    @property
    def status(self) -> PackageStatusType:
        return self._status

    @property
    def delivery_date(self) -> datetime:
        return self._delivery_date

    @property
    def delivery_address(self) -> str:
        return self._delivery_address

    @property
    def geographic_point(self) -> GeographicPointValue:
        return self._geographic_point

    @property
    def route_id(self) -> Optional[UUID]:
        return self._route_id

    @property
    def delivery_order(self) -> Optional[int]:
        return self._delivery_order

    def deliver(self, delivery_date: datetime, image_url: str, geographic_point: GeographicPointValue):
        if self._status == PackageStatusType.DELIVERED:
            raise ValueError("Package has already been delivered.")
        if delivery_date > datetime.now():
            raise ValueError("The delivery date cannot be in the future.")
        if not image_url.strip():
            raise ValueError("Image URL cannot be empty.")

        self._status = PackageStatusType.DELIVERED
        self._delivery_date = delivery_date
        self._geographic_point = geographic_point

        domain_event = PackageDeliveredEvent(
            package_id=self.id,
            route_id=self.route_id,
            delivery_date=delivery_date,
            geographic_point=geographic_point,
            image_url=image_url,
        )
        self.add_domain_event(domain_event)

        return PackageDeliveryEntity(
            id=uuid4(),
            package_id=self.id,
            route_id=self.route_id,
            delivery_date=delivery_date,
            geographic_point=geographic_point,
            image_url=image_url,
        )
