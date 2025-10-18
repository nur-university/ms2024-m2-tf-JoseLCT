from enum import StrEnum


class PackageStatusType(StrEnum):
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
