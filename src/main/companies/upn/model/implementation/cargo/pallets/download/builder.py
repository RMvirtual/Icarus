import copy
from src.main.companies.upn.api.interface.cargo.pallets.download \
    import DownloadPallet
from src.main.companies.upn.model.implementation.cargo.pallets.download \
    .implementation import NetworkPallet, NetworkPalletFields


class NetworkPalletBuilder:
    def __init__(self):
        self._fields = NetworkPalletFields()

    def set_barcode(self, barcode: str) -> None:
        self._fields.barcode = barcode

    def set_consignment_barcode(self, barcode: str) -> None:
        self._fields.consignment_barcode = barcode

    def set_type(self, type_code: str) -> None:
        self._fields.type = type_code

    def set_size(self, size_code: str) -> None:
        self._fields.size = size_code

    def set_type_constraints(self, types: list[str]) -> None:
        self._fields.type_constraints = copy.deepcopy(types)

    def set_size_constraints(self, sizes: list[str]) -> None:
        self._fields.size_constraints = copy.deepcopy(sizes)

    def build(self) -> DownloadPallet:
        return NetworkPallet(self._fields)
