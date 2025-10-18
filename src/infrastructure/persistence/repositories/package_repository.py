from datetime import datetime
from typing import Optional
from uuid import UUID

from geoalchemy2 import WKBElement
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.package.entities import PackageEntity
from src.domain.package.repositories import IPackageRepository
from src.domain.package.types import PackageStatusType
from src.infrastructure.persistence.domain_models.mappers import PackageMapper
from src.infrastructure.persistence.persistence_models.sqlalchemy import PackageModel


class PackageRepository(IPackageRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_async(self) -> list[PackageEntity]:
        query = select(PackageModel)
        result = await self._session.execute(query)
        packages = result.scalars().all()
        return [PackageMapper.to_entity(pkg) for pkg in packages]

    async def get_by_filters_async(
            self,
            start_index: int,
            max_results: int,
            text: Optional[str] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            states: Optional[list[PackageStatusType]] = None,
    ) -> list[PackageEntity]:
        query = select(PackageModel)

        if text:
            query = query.filter(PackageModel.tracking_number.ilike(f"%{text}%"))
        if start_date:
            query = query.filter(PackageModel.delivery_date >= start_date)
        if end_date:
            query = query.filter(PackageModel.delivery_date <= end_date)
        if states:
            query = query.filter(PackageModel.status.in_(states))

        query = query.offset(start_index).limit(max_results)
        result = await self._session.execute(query)
        packages = result.scalars().all()
        return [PackageMapper.to_entity(pkg) for pkg in packages]

    async def count_by_filters_async(
            self,
            text: Optional[str] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            states: Optional[list[PackageStatusType]] = None
    ) -> int:
        query = select(func.count()).select_from(PackageModel)

        if text:
            query = query.filter(PackageModel.tracking_number.ilike(f"%{text}%"))
        if start_date:
            query = query.filter(PackageModel.delivery_date >= start_date)
        if end_date:
            query = query.filter(PackageModel.delivery_date <= end_date)
        if states:
            query = query.filter(PackageModel.status.in_(states))

        result = await self._session.execute(query)
        return result.scalar_one()

    async def get_by_id_async(self, id: UUID) -> Optional[PackageEntity]:
        pass

    async def get_by_tracking_number_async(self, tracking_number: str) -> Optional[PackageEntity]:
        query = select(PackageModel).filter(PackageModel.tracking_number == tracking_number)
        result = await self._session.execute(query)
        package = result.scalars().first()
        return PackageMapper.to_entity(package) if package else None

    async def exists_by_tracking_number_async(self, tracking_number: str) -> bool:
        query = select(func.count()).select_from(PackageModel).filter(
            PackageModel.tracking_number == tracking_number
        )
        result = await self._session.execute(query)
        count = result.scalar_one()
        return count > 0

    async def add_async(self, entity: PackageEntity) -> None:
        geographic_point = self._create_geographic_point(
            latitude=entity.geographic_point.latitude,
            longitude=entity.geographic_point.longitude,
        )

        new_package = PackageModel(
            id=entity.id,
            route_id=entity.route_id,
            delivery_order=entity.delivery_order,
            tracking_number=entity.tracking_number,
            status=entity.status,
            delivery_date=entity.delivery_date,
            delivery_address=entity.delivery_address,
            geographic_point=geographic_point,
        )

        self._session.add(new_package)
        await self._session.flush()

    async def update_async(self, entity: PackageEntity) -> None:
        query = select(PackageModel).filter(PackageModel.id == entity.id)
        result = await self._session.execute(query)
        package = result.scalars().first()

        if not package:
            return

        geographic_point = self._create_geographic_point(
            latitude=entity.geographic_point.latitude,
            longitude=entity.geographic_point.longitude,
        )

        package.route_id = entity.route_id
        package.delivery_order = entity.delivery_order
        package.tracking_number = entity.tracking_number
        package.status = entity.status
        package.delivery_date = entity.delivery_date
        package.delivery_address = entity.delivery_address
        package.geographic_point = geographic_point

        await self._session.flush()

    async def delete_async(self, id: UUID) -> None:
        query = select(PackageModel).filter(PackageModel.id == id)
        result = await self._session.execute(query)
        package = result.scalars().first()

        if not package:
            return

        await self._session.delete(package)
        await self._session.flush()

    @staticmethod
    def _create_geographic_point(latitude: float, longitude: float) -> WKBElement:
        return WKBElement(f"POINT({longitude} {latitude})", srid=4326)
