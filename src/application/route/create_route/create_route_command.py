from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateRouteCommand:
    execution_date: datetime
