from typing import Optional
from uuid import UUID

from geoalchemy2 import WKBElement
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.package.entities import PackageDeliveryEntity
from src.domain.package.repositories import IPackageDeliveryRepository
from src.infrastructure.persistence.domain_models.mappers import PackageDeliveryMapper
from src.infrastructure.persistence.persistence_models.sqlalchemy import PackageDeliveryModel


class PackageDeliveryRepository(IPackageDeliveryRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_async(self) -> list[PackageDeliveryEntity]:
        query = select(PackageDeliveryModel)
        result = await self._session.execute(query)
        records = result.scalars().all()
        return [PackageDeliveryMapper.to_entity(r) for r in records]

    async def get_by_id_async(self, id: UUID) -> Optional[PackageDeliveryEntity]:
        query = select(PackageDeliveryModel).filter(PackageDeliveryModel.id == id)
        result = await self._session.execute(query)
        record = result.scalar_one_or_none()
        return PackageDeliveryMapper.to_entity(record) if record else None

    async def add_async(self, entity: PackageDeliveryEntity) -> None:
        geographic_point = self._create_geographic_point(
            entity.geographic_point.latitude,
            entity.geographic_point.longitude,
        )

        new_record = PackageDeliveryModel(
            id=entity.id,
            package_id=entity.package_id,
            route_id=entity.route_id,
            delivery_date=entity.delivery_date,
            image_url=entity.image_url,
            geographic_point=geographic_point,
        )

        self._session.add(new_record)
        await self._session.flush()

    @staticmethod
    def _create_geographic_point(latitude: float, longitude: float) -> WKBElement:
        return WKBElement(f"POINT({longitude} {latitude})", srid=4326)
