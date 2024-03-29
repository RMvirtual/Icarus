from src.main.companies.upn.database.interface.consignment.network\
    .constraints import NetworkConsignmentConstraintsList
from src.main.companies.upn.model.implementation.constraints.implementation \
    import DataConstraint
from src.main.file_system.companies.upn.api.consignments.network \
    import NetworkConsignmentFiles


class NetworkConsignmentConstraints(NetworkConsignmentConstraintsList):
    def __init__(self):
        file = NetworkConsignmentFiles()
        self._key_mappings = file.keys
        self._constraints = file.constraints

    def _constraint(self, key: str) -> DataConstraint:
        dictionary = self._map_key_to_constraint(key)

        return DataConstraint(
            const_type=dictionary["type"],
            const_values=(
                dictionary["values"] if "values" in dictionary else None)
        )

    def _map_key_to_constraint(self, key: str) -> dict[str, any]:
        return self._constraints[self._key_mappings[key]]

    @property
    def consignment_no(self) -> DataConstraint:
        return self._constraint("consignment_no")

    @property
    def barcode(self) -> DataConstraint:
        return self._constraint("barcode")

    @property
    def customer_reference(self) -> DataConstraint:
        return self._constraint("customer_reference")

    @property
    def depot_no(self) -> DataConstraint:
        return self._constraint("depot_no")

    @property
    def despatch_date(self) -> DataConstraint:
        return self._constraint("despatch_date")

    @property
    def delivery_datetime(self) -> DataConstraint:
        return self._constraint("delivery_datetime")

    @property
    def delivery_name(self) -> DataConstraint:
        return self._constraint("delivery_name")

    @property
    def delivery_address_1(self) -> DataConstraint:
        return self._constraint("delivery_address_1")

    @property
    def delivery_address_2(self) -> DataConstraint:
        return self._constraint("delivery_address_2")

    @property
    def delivery_town(self) -> DataConstraint:
        return self._constraint("delivery_town")

    @property
    def delivery_county(self) -> DataConstraint:
        return self._constraint("delivery_county")

    @property
    def delivery_post_code(self) -> DataConstraint:
        return self._constraint("delivery_post_code")

    @property
    def delivery_country(self) -> DataConstraint:
        return self._constraint("delivery_country")

    @property
    def delivery_contact_name(self) -> DataConstraint:
        return self._constraint("delivery_contact_name")

    @property
    def delivery_telephone_no(self) -> DataConstraint:
        return self._constraint("delivery_telephone_no")

    @property
    def total_weight(self) -> DataConstraint:
        return self._constraint("total_weight")

    @property
    def special_instructions(self) -> DataConstraint:
        return self._constraint("special_instructions")

    @property
    def customer_id(self) -> DataConstraint:
        return self._constraint("customer_id")

    @property
    def customer_name(self) -> DataConstraint:
        return self._constraint("customer_name")

    @property
    def customer_paperwork_pages(self) -> DataConstraint:
        return self._constraint("customer_paperwork_pages")

    @property
    def main_service(self) -> DataConstraint:
        return self._constraint("main_service")

    @property
    def premium_service(self) -> DataConstraint:
        return self._constraint("premium_service")

    @property
    def tail_lift_required(self) -> DataConstraint:
        return self._constraint("tail_lift_required")

    @property
    def additional_service(self) -> DataConstraint:
        return self._constraint("additional_service")

    @property
    def pallets(self) -> DataConstraint:
        return self._constraint("pallets")
