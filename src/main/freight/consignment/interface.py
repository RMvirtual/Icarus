from abc import ABC, abstractmethod
from src.main.addresses.interface import Address
from src.main.freight.references.interface import References
from src.main.freight.shipment_dates.interface import ShipmentDatesInterface
from src.main.freight.cargo.container.implementation import Cargo
from src.main.freight.service.container.interface import Services


class Consignment(ABC):
    @property
    @abstractmethod
    def references(self) -> References:
        ...

    @property
    @abstractmethod
    def address(self) -> Address:
        ...

    @property
    @abstractmethod
    def cargo(self) -> Cargo:
        ...

    @property
    @abstractmethod
    def service(self) -> Services:
        ...

    @property
    @abstractmethod
    def delivery_instructions(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def client_name(self) -> str:
        ...

    @property
    @abstractmethod
    def shipment_dates(self) -> ShipmentDatesInterface:
        ...
