from src.domain.package.entities import PackageDeliveryEntity


class PackageDeliveryMapper:
    @staticmethod
    def to_entity(db_model) -> PackageDeliveryEntity:
        return PackageDeliveryEntity(
            id=db_model.id,
            package_id=db_model.package_id,
            delivery_date=db_model.delivery_date,
            image_url=db_model.image_url,
            geographic_point=db_model.geographic_point,
        )
