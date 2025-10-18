from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.delivery_person.get_all_delivery_persons import DeliveryPersonSummaryDto, \
    GetAllDeliveryPersonsQuery
from src.infrastructure.persistence.persistence_models.sqlalchemy import DeliveryPersonModel


class GetAllDeliveryPersonsHandler:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def handle(self, query: GetAllDeliveryPersonsQuery):
        sql = select(DeliveryPersonModel)
        result = await self._session.execute(sql)
        delivery_persons = result.scalars().all()
        return [
            DeliveryPersonSummaryDto(
                id=dp.id,
                is_active=dp.is_active,
                name=dp.name,
            )
            for dp in delivery_persons
        ]
