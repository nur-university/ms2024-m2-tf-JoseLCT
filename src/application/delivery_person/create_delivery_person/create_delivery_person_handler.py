from uuid import uuid4

from src.application.delivery_person.create_delivery_person.create_delivery_person_command import \
    CreateDeliveryPersonCommand
from src.core.abstractions import IUnitOfWork
from src.core.results import Result
from src.domain.delivery_person.entities import DeliveryPersonEntity
from src.domain.delivery_person.repositories import IDeliveryPersonRepository


class CreateDeliveryPersonHandler:
    def __init__(
            self,
            unit_of_work: IUnitOfWork,
            repository: IDeliveryPersonRepository,
    ):
        self._unit_of_work = unit_of_work
        self._repository = repository

    async def handle(self, command: CreateDeliveryPersonCommand):
        entity = DeliveryPersonEntity(
            id=uuid4(),
            is_active=command.is_active,
            name=command.name,
        )
        await self._repository.add_async(entity)
        await self._unit_of_work.commit_async()
        return Result.success_value(entity.id)
