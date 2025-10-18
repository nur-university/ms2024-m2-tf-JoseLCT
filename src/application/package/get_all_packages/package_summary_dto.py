from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class PackageSummaryDto:
    id: UUID
    delivery_date: datetime
    delivery_address: str
