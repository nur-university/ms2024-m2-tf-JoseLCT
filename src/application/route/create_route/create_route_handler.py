from uuid import uuid4

from src.application.route.create_route import CreateRouteCommand
from src.core.abstractions import IUnitOfWork
from src.core.results import Result
from src.domain.route.entities import RouteEntity
from src.domain.route.repositories import IRouteRepository
from src.domain.route.types import RouteStatusType


class CreateRouteHandler:
    def __init__(
            self,
            unit_of_work: IUnitOfWork,
            repository: IRouteRepository,
    ):
        self._unit_of_work = unit_of_work
        self._repository = repository

    async def handle(self, command: CreateRouteCommand):
        entity = RouteEntity(
            id=uuid4(),
            execution_date=command.execution_date,
            status=RouteStatusType.PENDING,
        )
        await self._repository.add_async(entity)
        await self._unit_of_work.commit_async()
        return Result.success_value(entity.id)
