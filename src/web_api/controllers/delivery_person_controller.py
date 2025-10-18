from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.application.container import ApplicationContainer
from src.application.delivery_person.create_delivery_person import CreateDeliveryPersonCommand
from src.application.delivery_person.get_all_delivery_persons import GetAllDeliveryPersonsQuery
from src.application.delivery_person.get_delivery_person_by_id import GetDeliveryPersonByIdQuery
from src.core.patterns import Mediator
from src.web_api.schemas.delivery_person import DeliveryPersonCreateSchema

router = APIRouter(tags=['Delivery Person'], prefix='/delivery-persons')


@router.get(
    path='/',
    summary='Get all delivery persons',
    description='Retrieve a list of all delivery persons.',
)
@inject
async def get_all_delivery_persons(
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    query = GetAllDeliveryPersonsQuery()
    result = await mediator.send(query)
    return result


@router.get(
    path='/{delivery_person_id}/',
    summary='Get delivery person by ID',
    description='Retrieve a delivery person by their unique ID.',
)
@inject
async def get_delivery_person_by_id(
        delivery_person_id: UUID,
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    query = GetDeliveryPersonByIdQuery(id=delivery_person_id)
    result = await mediator.send(query)
    return result


@router.post(
    path='/',
    summary='Create a new delivery person',
    description='Create a new delivery person with the provided details.',
)
@inject
async def create_delivery_person(
        schema: DeliveryPersonCreateSchema,
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    command = CreateDeliveryPersonCommand(
        is_active=schema.is_active,
        name=schema.name,
    )
    result = await mediator.send(command)
    return result
