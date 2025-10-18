from src.domain.package.entities import PackageEntity


class PackageMapper:
    @staticmethod
    def to_entity(db_model) -> PackageEntity:
        return PackageEntity(
            id=db_model.id,
            tracking_number=db_model.tracking_number,
            status=db_model.status,
            delivery_date=db_model.delivery_date,
            delivery_address=db_model.delivery_address,
            geographic_point=db_model.geographic_point,
            route_id=db_model.route_id,
        )
