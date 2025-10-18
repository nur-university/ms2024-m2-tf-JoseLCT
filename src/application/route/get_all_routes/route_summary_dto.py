from dataclasses import dataclass
from datetime import datetime

from src.domain.route.types import RouteStatusType


@dataclass
class RouteSummaryDto:
    id: str
    execution_date: datetime
    status: RouteStatusType
