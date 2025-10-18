from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from uuid import UUID

from src.core.abstractions import IRepository
from src.domain.package.entities import PackageEntity
from src.domain.package.types import PackageStatusType


class IPackageRepository(IRepository[PackageEntity], ABC):
    @abstractmethod
    async def get_all_async(self) -> list[PackageEntity]:
        pass

    @abstractmethod
    async def get_by_filters_async(
            self,
            start_index: int,
            max_results: int,
            text: Optional[str] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            states: Optional[list[PackageStatusType]] = None,
    ) -> list[PackageEntity]:
        pass

    @abstractmethod
    async def count_by_filters_async(
            self,
            text: Optional[str] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            states: Optional[list[PackageStatusType]] = None,
    ) -> int:
        pass

    @abstractmethod
    async def get_by_tracking_number_async(self, tracking_number: str) -> Optional[PackageEntity]:
        pass

    @abstractmethod
    async def exists_by_tracking_number_async(self, tracking_number: str) -> bool:
        pass

    @abstractmethod
    async def update_async(self, entity: PackageEntity) -> None:
        pass

    @abstractmethod
    async def delete_async(self, id: UUID) -> None:
        pass
