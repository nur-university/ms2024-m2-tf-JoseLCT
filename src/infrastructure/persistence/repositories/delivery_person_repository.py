from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.delivery_person.entities import DeliveryPersonEntity
from src.domain.delivery_person.repositories import IDeliveryPersonRepository
from src.infrastructure.persistence.domain_models.mappers import DeliveryPersonMapper
from src.infrastructure.persistence.persistence_models.sqlalchemy import DeliveryPersonModel


class DeliveryPersonRepository(IDeliveryPersonRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_async(self) -> list[DeliveryPersonEntity]:
        query = select(DeliveryPersonModel)
        result = await self._session.execute(query)
        delivery_persons = result.scalars().all()
        return [DeliveryPersonMapper.to_entity(dp) for dp in delivery_persons]

    async def get_by_id_async(self, id: UUID) -> Optional[DeliveryPersonEntity]:
        query = select(DeliveryPersonModel).filter(DeliveryPersonModel.id == id)
        result = await self._session.execute(query)
        delivery_person = result.scalar_one_or_none()
        return DeliveryPersonMapper.to_entity(delivery_person) if delivery_person else None

    async def add_async(self, entity: DeliveryPersonEntity) -> None:
        new_delivery_person = DeliveryPersonModel(
            id=entity.id,
            is_active=entity.is_active,
            name=entity.name,
        )
        self._session.add(new_delivery_person)
        await self._session.flush()

    async def update_async(self, entity: DeliveryPersonEntity) -> None:
        query = select(DeliveryPersonModel).filter(DeliveryPersonModel.id == entity.id)
        result = await self._session.execute(query)
        delivery_person = result.scalar_one_or_none()
        if not delivery_person:
            return
        delivery_person.is_active = entity.is_active
        delivery_person.name = entity.name
        await self._session.flush()

    async def delete_async(self, id: UUID) -> None:
        query = select(DeliveryPersonModel).filter(DeliveryPersonModel.id == id)
        result = await self._session.execute(query)
        delivery_person = result.scalar_one_or_none()
        if not delivery_person:
            return
        await self._session.delete(delivery_person)
        await self._session.flush()
