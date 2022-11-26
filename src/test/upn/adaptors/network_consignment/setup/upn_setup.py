import datetime
from src.main.upn.consignments.network_consignment.implementation \
    import NetworkConsignment

from src.main.upn.freight.references.references import UPNReferences
from src.main.upn.freight.customer.customer import UPNCustomer
from src.main.upn.freight.cargo.container.container import UPNCargo
from src.main.upn.freight.services.services import UPNServices
from src.main.upn.freight.dates.dates import UPNDates
from src.main.upn.freight.address.address import UPNAddress
from src.main.upn.packages.network_pallet import factory as pallet_factory
from src.main.upn.api.interfaces.pallets.network_pallet \
    import NetworkPalletInterface


def dummy_network_consignment() -> NetworkConsignment:
    result = NetworkConsignment()
    result.references = _references()
    result.depot_no = 75
    result.customer_paperwork_pages = 0
    result.customer = _customer()
    result.delivery_address = _delivery_address()
    result.cargo = _cargo()
    result.dates = _dates()
    result.special_instructions = "Don't smash up this adaptors."
    result.services = _services()

    return result


def _references() -> UPNReferences:
    result = UPNReferences()

    result.consignment_no = "GR221004388"
    result.customer_reference = "49632"
    result.barcode = "W213359799C"

    return result


def _delivery_address() -> UPNAddress:
    result = UPNAddress()
    result.name = "GRAYLAW FREIGHT GROUP"
    result.line_1 = "GRAYLAW FREIGHT TERMINAL"
    result.line_2 = "GILLBRANDS ROAD"
    result.town = "SKELMERSDALE"
    result.county = "LANCS"
    result.post_code = "WN8  9TA"
    result.country = "UNITED KINGDOM"
    result.contact_name = "Katherine   01695 729101"
    result.telephone_no = "0"

    return result


def _services() -> UPNServices:
    result = UPNServices()
    result.main_service = "P"
    result.premium_service = None
    result.tail_lift_required = None
    result.additional_service = None

    return result


def _cargo() -> UPNCargo:
    result = UPNCargo()
    result.total_weight = 1100
    result.pallets = _pallets()

    return result


def _customer() -> UPNCustomer:
    result = UPNCustomer()
    result.name = "GRAYLAW"
    result.id = 4236

    return result


def _dates() -> UPNDates:
    result = UPNDates()
    result.despatch = datetime.datetime(2022, 10, 18, 0, 0)
    result.delivery = datetime.datetime(2022, 10, 18, 16, 30)

    return result


def _pallets() -> list[NetworkPalletInterface]:
    return [_network_pallet("W213359800P"), _network_pallet("W213359801P")]


def _network_pallet(barcode_no: str) -> NetworkPalletInterface:
    result = pallet_factory.network_pallet(size_name="N", type_name="FULL")
    result.consignment_barcode = "W213359799C"
    result.barcode = barcode_no

    return result
