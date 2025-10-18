from pydantic import BaseModel


class DeliveryPersonCreateSchema(BaseModel):
    name: str
