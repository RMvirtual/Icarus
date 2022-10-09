from src.main.freight.consignment.model import Consignment

from src.main.forward_office.consignment_import.parser.requests.types \
    import ConsignmentParseRequest

from src.main.forward_office.consignment_import.parser import address
from src.main.forward_office.consignment_import.parser import dates
from src.main.forward_office.consignment_import.parser.cargo import CargoParser
from src.main.forward_office.consignment_import.parser.service \
    import ServiceParser


class ConsignmentParser:
    def __init__(self):
        pass

    def parse(self, request: ConsignmentParseRequest) -> Consignment:
        consignment = Consignment()

        consignment.client_name = request.principal_client
        consignment.reference = request.reference
        consignment.cargo = CargoParser().parse(request.cargo)
        consignment.delivery_instructions = request.delivery_instructions
        consignment.shipment_dates = dates.parse(request.shipment_dates)
        consignment.address = address.parse(request.address)
        consignment.service = ServiceParser().parse(request.service)

        return consignment