from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional
from uuid import UUID

from src.core.abstractions import AggregateRoot

TEntity = TypeVar("TEntity", bound=AggregateRoot)


class IRepository(ABC, Generic[TEntity]):
    @abstractmethod
    async def get_by_id_async(self, id: UUID) -> Optional[TEntity]:
        pass

    @abstractmethod
    async def add_async(self, entity: TEntity) -> None:
        pass
