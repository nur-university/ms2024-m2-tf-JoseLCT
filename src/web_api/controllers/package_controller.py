from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.application.container import ApplicationContainer
from src.application.package.create_package import CreatePackageCommand
from src.application.package.get_all_packages import GetAllPackagesQuery
from src.core.patterns import Mediator
from src.web_api.schemas.package import PackageCreateSchema

router = APIRouter(tags=['Package'], prefix='/packages')


@router.get(
    path='/',
    summary='Get all packages',
    description='Retrieve a list of all packages.',
)
@inject
async def get_all_packages(
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    query = GetAllPackagesQuery()
    result = await mediator.send(query)
    return result


@router.post(
    path='/',
    summary='Create a new package',
    description='Create a new package with the provided details.',
)
@inject
async def create_package(
        schema: PackageCreateSchema,
        mediator: Mediator = Depends(Provide[ApplicationContainer.mediator]),
):
    command = CreatePackageCommand(
        delivery_address=schema.delivery_address,
        delivery_date=schema.delivery_date,
        latitude=schema.latitude,
        longitude=schema.longitude,
    )
    result = await mediator.send(command)
    return result
