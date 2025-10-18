from uuid import UUID

from src.core.abstractions import Entity


class AggregateRoot(Entity):
    def __init__(self, id: UUID = None):
        super().__init__(id)
