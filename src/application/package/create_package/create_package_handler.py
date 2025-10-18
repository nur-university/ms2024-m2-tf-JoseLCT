from uuid import uuid4

from src.application.package.create_package import CreatePackageCommand
from src.core.abstractions import IUnitOfWork
from src.core.results import Result
from src.domain.package.entities import PackageEntity
from src.domain.package.repositories import IPackageRepository
from src.domain.package.types import PackageStatusType
from src.domain.shared.value_objects import GeographicPointValue


class CreatePackageHandler:
    def __init__(
            self,
            unit_of_work: IUnitOfWork,
            repository: IPackageRepository,
    ):
        self._unit_of_work = unit_of_work
        self._repository = repository

    async def handle(self, command: CreatePackageCommand):
        entity = PackageEntity(
            id=uuid4(),
            tracking_number=uuid4().__str__(),
            status=PackageStatusType.PENDING,
            delivery_date=command.delivery_date,
            delivery_address=command.delivery_address,
            geographic_point=GeographicPointValue(
                latitude=command.latitude,
                longitude=command.longitude,
            ),
        )
        await self._repository.add_async(entity)
        await self._unit_of_work.commit_async()
        return Result.success_value(entity.id)
