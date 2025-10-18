from src.domain.delivery_person.entities import DeliveryPersonEntity


class DeliveryPersonMapper:
    @staticmethod
    def to_entity(db_model) -> DeliveryPersonEntity:
        return DeliveryPersonEntity(
            id=db_model.id,
            is_active=db_model.is_active,
            name=db_model.name,
        )
