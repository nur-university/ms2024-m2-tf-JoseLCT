from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.delivery_person.get_all_delivery_persons import DeliveryPersonSummaryDto
from src.application.delivery_person.get_delivery_person_by_id import GetDeliveryPersonByIdQuery
from src.infrastructure.persistence.persistence_models.sqlalchemy import DeliveryPersonModel


class GetDeliveryPersonByIdHandler:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def handle(self, query: GetDeliveryPersonByIdQuery) -> DeliveryPersonSummaryDto | None:
        sql = select(DeliveryPersonModel).filter(DeliveryPersonModel.id == query.id)
        result = await self._session.execute(query)
        delivery_person = result.scalar_one_or_none()

        if not delivery_person:
            return None

        return DeliveryPersonSummaryDto(
            id=delivery_person.id,
            is_active=delivery_person.is_active,
            name=delivery_person.name,
        )
