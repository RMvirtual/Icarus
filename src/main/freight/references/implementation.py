from src.main.freight.references import interface

from src.main.freight.references.consignment.interface \
    import ConsignmentReference as ConsignmentReferenceInterface

from src.main.freight.references.consignment.reference \
    import ConsignmentReference


class References(interface.References):
    def __init__(self, consignment_reference: str):
        self._consignment = ConsignmentReference(consignment_reference)
        self._shipper = []
        self._consignee = []

    @property
    def consignment(self) -> ConsignmentReferenceInterface:
        return self._consignment

    @consignment.setter
    def consignment(self, new_reference: str) -> None:
        self._consignment = ConsignmentReference(new_reference)

    @property
    def shipper(self) -> list[str]:
        return self._shipper

    @property
    def consignee(self) -> list[str]:
        return self._consignee
