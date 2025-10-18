from datetime import datetime

from pydantic import BaseModel


class PackageCreateSchema(BaseModel):
    delivery_date: datetime
    delivery_address: str
    latitude: float
    longitude: float
