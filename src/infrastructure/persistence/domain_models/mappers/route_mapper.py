from src.domain.route.entities import RouteEntity


class RouteMapper:
    @staticmethod
    def to_entity(db_model) -> RouteEntity:
        return RouteEntity(
            id=db_model.id,
            delivery_person_id=db_model.delivery_person_id,
            execution_date=db_model.execution_date,
            status=db_model.status,
        )
