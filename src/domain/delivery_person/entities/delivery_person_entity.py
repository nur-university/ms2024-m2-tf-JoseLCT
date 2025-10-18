from typing import Optional
from uuid import UUID

from src.core.abstractions import AggregateRoot
from src.domain.route.entities import RouteEntity


class DeliveryPersonEntity(AggregateRoot):
    def __init__(
            self,
            id: UUID,
            is_active: bool,
            name: str,
            routes: Optional[list[RouteEntity]] = None,
    ):
        super().__init__(id)
        self._is_active = is_active
        self._name = name
        self._routes = routes or []

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def name(self) -> str:
        return self._name

    @property
    def routes(self) -> list:
        return self._routes

    def get_route(self, route_id: UUID) -> Optional[RouteEntity]:
        return next((r for r in self._routes if r.id == route_id), None)

    def add_route(self, route: RouteEntity):
        if any(r.id == route.id for r in self._routes):
            raise ValueError(f"Route with id {route.id} already exists for this delivery person.")
        self._routes.append(route)

    def remove_route(self, route_id: UUID):
        route = self.get_route(route_id)
        if not route:
            raise ValueError(f"Route with id {route_id} does not exist for this delivery person.")
        self._routes.remove(route)

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False
        self._routes.clear()
