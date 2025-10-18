from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetDeliveryPersonByIdQuery:
    id: UUID
