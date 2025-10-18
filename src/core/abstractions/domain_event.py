from abc import ABC
from datetime import datetime
from uuid import UUID, uuid4


class DomainEvent(ABC):
    def __init__(self):
        self._id = uuid4()
        self._occured_on = datetime.now()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def occured_on(self) -> datetime:
        return self._occured_on
