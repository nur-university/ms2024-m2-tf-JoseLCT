from abc import ABC, abstractmethod
from uuid import UUID

from src.core.abstractions import IRepository
from src.domain.delivery_person.entities import DeliveryPersonEntity


class IDeliveryPersonRepository(IRepository[DeliveryPersonEntity], ABC):
    @abstractmethod
    async def get_all_async(self) -> list[DeliveryPersonEntity]:
        pass

    @abstractmethod
    async def update_async(self, entity: DeliveryPersonEntity) -> None:
        pass

    @abstractmethod
    async def delete_async(self, id: UUID) -> None:
        pass
