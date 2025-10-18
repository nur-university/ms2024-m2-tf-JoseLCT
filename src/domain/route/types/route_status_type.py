from enum import StrEnum


class RouteStatusType(StrEnum):
    PENDING = "Pending"
    READY_FOR_DELIVERY = "Ready for Delivery"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
