from datetime import datetime
from typing import Optional
from uuid import UUID

from src.core.abstractions import AggregateRoot
from src.domain.package.entities import PackageEntity
from src.domain.route.types import RouteStatusType


class RouteEntity(AggregateRoot):
    def __init__(
            self,
            id: UUID,
            execution_date: datetime,
            status: RouteStatusType,
            delivery_person_id: UUID | None = None,
            packages: Optional[list[PackageEntity]] = None,
    ):
        super().__init__(id)
        self._execution_date = execution_date
        self._status = status
        self._delivery_person_id = delivery_person_id
        self._packages = packages or []

    @property
    def execution_date(self) -> datetime:
        return self._execution_date

    @property
    def status(self) -> RouteStatusType:
        return self._status

    @property
    def delivery_person_id(self) -> UUID:
        return self._delivery_person_id

    @property
    def packages(self) -> list[PackageEntity]:
        return self._packages

    def get_package(self, package_id: UUID) -> Optional[PackageEntity]:
        return next((p for p in self._packages if p.id == package_id), None)

    def assign_packages(self, ordered_packages: list[PackageEntity]):
        if self._status != RouteStatusType.PENDING:
            raise ValueError(f"Cannot add packages to a route with status {self._status}.")

        orders = [p.delivery_order for p in ordered_packages]
        if len(orders) != len(set(orders)):
            raise ValueError("There are packages with duplicate delivery orders.")

        self._packages = sorted(ordered_packages, key=lambda p: p.delivery_order)

    def add_package(self, package: PackageEntity):
        if self._status != RouteStatusType.PENDING:
            raise ValueError(f"Cannot add packages to a route with status {self._status}.")
        if any(p.delivery_order == package.delivery_order for p in self._packages):
            raise ValueError(f"A package with delivery order {package.delivery_order} already exists.")
        self._packages.append(package)
        self._packages.sort(key=lambda p: p.delivery_order)

    def remove_package(self, package_id: UUID):
        if self._status != RouteStatusType.PENDING:
            raise ValueError(f"Cannot remove packages from a route with status {self._status}.")
        package = self.get_package(package_id)
        if not package:
            raise ValueError(f"Package with ID {package_id} not found in the route.")
        self._packages = [p for p in self._packages if p.id != package_id]

    def start_route(self):
        if self._status != RouteStatusType.PENDING:
            raise ValueError("Can only start a pending route.")
        if not self._packages:
            raise ValueError("Cannot start a route without packages.")
        self._status = RouteStatusType.IN_PROGRESS

    def complete_route(self):
        if self._status != RouteStatusType.IN_PROGRESS:
            raise ValueError("Can only complete a route that is in progress.")
        self._status = RouteStatusType.COMPLETED
