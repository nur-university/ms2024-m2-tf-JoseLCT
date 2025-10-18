from dataclasses import dataclass


@dataclass
class CreateDeliveryPersonCommand:
    name: str
    is_active: bool = True
