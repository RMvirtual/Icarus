import dataclasses


@dataclasses.dataclass
class AddressParseRequest:
    name: str = ""
    line_1: str = ""
    line_2: str = ""
    line_3: str = ""
    town: str = ""
    post_code: str = ""
    country: str = "GB"
    contact_name: str = ""
    telephone_number: str = ""


@dataclasses.dataclass
class ServiceParseRequest:
    priority_code: str = ""
    tail_lift_requested: bool = False


@dataclasses.dataclass
class CargoEntryParseRequest:
    quantity: int = 0
    package_type: str = ""
    weight: float = 0
    goods_description: str = ""

    def __bool__(self):
        return not (
            not self.quantity and not self.package_type
            and not self.weight and not self.goods_description
        )

    def is_empty(self) -> bool:
        return dataclasses.fields(self) in (0, "")


@dataclasses.dataclass
class CargoParseRequest:
    line_1: CargoEntryParseRequest = CargoEntryParseRequest()
    line_2: CargoEntryParseRequest = CargoEntryParseRequest()
    line_3: CargoEntryParseRequest = CargoEntryParseRequest()
    line_4: CargoEntryParseRequest = CargoEntryParseRequest()

