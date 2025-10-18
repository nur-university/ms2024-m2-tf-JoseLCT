from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeliveryPersonDetailDto:
    id: UUID
    is_active: bool
    name: str
