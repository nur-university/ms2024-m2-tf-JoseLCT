from abc import ABC, abstractmethod

from src.core.abstractions import IRepository
from src.domain.route.entities import RouteEntity


class IRouteRepository(IRepository[RouteEntity], ABC):
    @abstractmethod
    async def get_all_async(self) -> list[RouteEntity]:
        pass

    @abstractmethod
    async def update_async(self, entity: RouteEntity) -> None:
        pass

    @abstractmethod
    async def delete_async(self, id) -> None:
        pass
