from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.route.entities import RouteEntity
from src.domain.route.repositories import IRouteRepository
from src.infrastructure.persistence.domain_models.mappers import RouteMapper
from src.infrastructure.persistence.persistence_models.sqlalchemy import RouteModel


class RouteRepository(IRouteRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_async(self) -> list[RouteEntity]:
        query = select(RouteModel)
        result = await self._session.execute(query)
        routes = result.scalars().all()
        return [RouteMapper.to_entity(r) for r in routes]

    async def get_by_id_async(self, id: UUID) -> Optional[RouteEntity]:
        query = select(RouteModel).where(RouteModel.id == id)
        result = await self._session.execute(query)
        route = result.scalar_one_or_none()
        return RouteMapper.to_entity(route) if route else None

    async def add_async(self, entity: RouteEntity) -> None:
        new_route = RouteModel(
            id=entity.id,
            delivery_person_id=entity.delivery_person_id,
            execution_date=entity.execution_date,
            status=entity.status,
        )
        self._session.add(new_route)
        await self._session.flush()

    async def update_async(self, entity: RouteEntity) -> None:
        query = select(RouteModel).where(RouteModel.id == entity.id)
        result = await self._session.execute(query)
        route = result.scalar_one_or_none()
        if not route:
            return
        route.delivery_person_id = entity.delivery_person_id
        route.execution_date = entity.execution_date
        route.status = entity.status
        await self._session.flush()

    async def delete_async(self, id) -> None:
        query = select(RouteModel).where(RouteModel.id == id)
        result = await self._session.execute(query)
        route = result.scalar_one_or_none()
        if not route:
            return
        await self._session.delete(route)
        await self._session.flush()
