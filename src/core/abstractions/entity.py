from abc import ABC
from uuid import UUID, uuid4

from src.core.abstractions import DomainEvent


class Entity(ABC):
    def __init__(self, id: UUID = None):
        self._id = id or uuid4()

        if self._id.int == 0:
            raise ValueError("Id cannot be empty")

        self._domain_events: list[DomainEvent] = []

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def domain_events(self) -> list[DomainEvent]:
        return self._domain_events

    def add_domain_event(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)

    def clear_domain_events(self) -> None:
        self._domain_events.clear()
