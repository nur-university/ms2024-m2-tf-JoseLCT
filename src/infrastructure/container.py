from dependency_injector import containers, providers

from src.infrastructure.persistence.domain_models import DomainDb
from src.infrastructure.persistence.repositories import DeliveryPersonRepository, PackageRepository, RouteRepository, \
    PackageDeliveryRepository
from src.infrastructure.queries.delivery_person import GetAllDeliveryPersonsHandler, GetDeliveryPersonByIdHandler


class InfrastructureContainer(containers.DeclarativeContainer):
    session_provider = providers.Callable(DomainDb.get_session)

    delivery_person_repository = providers.Factory(
        DeliveryPersonRepository,
        session=session_provider,
    )
    package_repository = providers.Factory(
        PackageRepository,
        session=session_provider,
    )
    route_repository = providers.Factory(
        RouteRepository,
        session=session_provider,
    )
    package_delivery_repository = providers.Factory(
        PackageDeliveryRepository,
        session=session_provider,
    )

    get_all_delivery_persons_handler = providers.Factory(
        GetAllDeliveryPersonsHandler,
        session=session_provider,
    )
    get_delivery_person_by_id_handler = providers.Factory(
        GetDeliveryPersonByIdHandler,
        session=session_provider,
    )
