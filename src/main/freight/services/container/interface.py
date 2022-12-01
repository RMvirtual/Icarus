from __future__ import annotations
from abc import ABC, abstractmethod
from src.main.freight.services.types.interface.main import MainService
from src.main.freight.services.types.interface.premium import PremiumService
from src.main.freight.services.types.interface.booked import BookedService
from src.main.freight.services.types.interface.tail_lift import TailLiftService


class Services(ABC):
    @abstractmethod
    def main(self) -> MainService:
        ...

    @abstractmethod
    def premium(self) -> PremiumService:
        ...

    @abstractmethod
    def booked(self) -> BookedService:
        ...

    @abstractmethod
    def tail_lift(self) -> TailLiftService:
        ...

    @abstractmethod
    def __eq__(self, other: Services) -> bool:
        ...
