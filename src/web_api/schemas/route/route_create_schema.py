from datetime import datetime

from pydantic import BaseModel


class RouteCreateSchema(BaseModel):
    execution_date: datetime
