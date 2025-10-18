from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreatePackageCommand:
    delivery_date: datetime
    delivery_address: str
    latitude: float
    longitude: float
