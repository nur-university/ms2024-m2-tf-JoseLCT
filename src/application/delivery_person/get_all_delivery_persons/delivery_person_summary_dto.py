from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeliveryPersonSummaryDto:
    id: UUID
    is_active: bool
    name: str
