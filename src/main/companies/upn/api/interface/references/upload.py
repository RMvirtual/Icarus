from abc import ABC, abstractmethod


class ReferencesUpload(ABC):
    @property
    @abstractmethod
    def consignment_no(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_reference(self) -> str:
        ...
