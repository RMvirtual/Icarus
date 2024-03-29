from src.main.companies.upn.api.interface.cargo.pallets.upload \
    import UploadPallet
from src.main.companies.upn.model.implementation.cargo.pallets.abstract \
    .abstract import AbstractUPNPallet, UPNPalletFields


class CustPalletFields(UPNPalletFields):
    weight: int = 0


class CustPallet(AbstractUPNPallet, UploadPallet):
    def __init__(self, pallet_fields: CustPalletFields) -> None:
        super().__init__(pallet_fields)
        self._weight = pallet_fields.weight

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, new_weight: int) -> None:
        self._weight = new_weight
