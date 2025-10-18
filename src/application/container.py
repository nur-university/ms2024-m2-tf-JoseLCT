from dependency_injector import containers, providers

from src.application.delivery_person.get_all_delivery_persons import GetAllDeliveryPersonsQuery
from src.application.delivery_person.get_delivery_person_by_id import GetDeliveryPersonByIdQuery
from src.core.patterns import Mediator


class ApplicationContainer(containers.DeclarativeContainer):
    infrastructure = providers.DependenciesContainer()

    mediator = providers.Singleton(
        Mediator,
        handlers={
            GetAllDeliveryPersonsQuery: infrastructure.get_all_delivery_persons_handler,
            GetDeliveryPersonByIdQuery: infrastructure.get_delivery_person_by_id_handler,
        },
    )
