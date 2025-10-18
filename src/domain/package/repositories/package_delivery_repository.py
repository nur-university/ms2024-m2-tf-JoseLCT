from abc import ABC, abstractmethod

from src.core.abstractions import IRepository
from src.domain.package.entities import PackageDeliveryEntity


class IPackageDeliveryRepository(IRepository[PackageDeliveryEntity], ABC):
    @abstractmethod
    async def get_all_async(self) -> list[PackageDeliveryEntity]:
        pass
