from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from src.core.abstractions import Entity
from src.domain.shared.value_objects import GeographicPointValue


@dataclass
class PackageDeliveryEntity(Entity):
    def __init__(
            self,
            id: UUID,
            package_id: UUID,
            route_id: UUID,
            delivery_date: datetime,
            geographic_point: GeographicPointValue,
            image_url: Optional[str] = None,
    ):
        super().__init__(id)
        self._package_id = package_id
        self._route_id = route_id
        self._delivery_date = delivery_date
        self._geographic_point = geographic_point
        self._image_url = image_url

    @property
    def package_id(self) -> UUID:
        return self._package_id

    @property
    def route_id(self) -> UUID:
        return self._route_id

    @property
    def delivery_date(self) -> datetime:
        return self._delivery_date

    @property
    def geographic_point(self) -> GeographicPointValue:
        return self._geographic_point

    @property
    def image_url(self) -> str:
        return self._image_url

    @image_url.setter
    def image_url(self, value: str):
        self._image_url = value

    def __post_init__(self):
        if self.delivery_date > datetime.now():
            raise ValueError("The delivery date cannot be in the future.")
