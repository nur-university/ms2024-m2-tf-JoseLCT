from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.application.container import ApplicationContainer
from src.application.route.create_route import CreateRouteCommand
from src.application.route.get_all_routes import GetAllRoutesQuery
from src.core.patterns import Mediator
from src.web_api.schemas.route import RouteCreateSchema

router = APIRouter(tags=['Route'], prefix='/routes')


@router.get(
    path='/',
    summary='Get all routes',
    description='Retrieve a list of all routes.',
)
@inject
async def get_all_routes(
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    query = GetAllRoutesQuery()
    result = await mediator.send(query)
    return result


@router.post(
    path='/',
    summary='Create a new route',
    description='Create a new route with the provided details.',
)
@inject
async def create_route(
        schema: RouteCreateSchema,
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    command = CreateRouteCommand(
        execution_date=schema.execution_date,
    )
    result = await mediator.send(command)
    return result
