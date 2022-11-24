import copy
from src.main.upn.consignment.cargo.package.cust_pallet.interface \
    import CustPallet as CustPalletInterface

from src.main.upn.consignment.cargo.package.cust_pallet.implementation \
    import CustPallet, CustPalletFields


class CustPalletBuilder:
    def __init__(self):
        self._fields = CustPalletFields()

    def set_type(self, type_code: str) -> None:
        self._fields.type = type_code

    def set_size(self, size_code: str) -> None:
        self._fields.size = size_code

    def set_type_constraints(self, types: list) -> None:
        self._fields.types = copy.deepcopy(types)

    def set_size_constraints(self, sizes: list) -> None:
        self._fields.sizes = copy.deepcopy(sizes)

    def set_weight(self, weight: int) -> None:
        self._fields.weight = weight

    def build(self) -> CustPalletInterface:
        return CustPallet(self._fields)
