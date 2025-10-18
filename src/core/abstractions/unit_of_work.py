from abc import ABC, abstractmethod
from asyncio import CancelledError
from typing import Optional


class IUnitOfWork(ABC):
    @abstractmethod
    async def commit_async(self, cancellation_token: Optional[CancelledError] = None) -> None:
        pass
