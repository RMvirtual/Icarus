import json
import copy
from typing import Callable

from src.main.file_system import runfiles, system_files
from src.main.freight.service.model import Service


class ServiceCodeMapBuilder:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        self._mappings = {}
        self._parse_mappings()
        self._service = Service()

    def _parse_mappings(self):
        for service_mapping in self._mapping_file_contents():
            self._add(service_mapping)

    def _add(self, service_mapping):
        priority_code = service_mapping["priority_code"]
        self._mappings[priority_code] = self._deserialise(service_mapping)

    def _deserialise(self, service_mapping) -> Service:
        mapping_info = service_mapping["maps_to"]

        self._service = Service()
        self._process_main_service(mapping_info)
        self._process_premium_service(mapping_info)
        self._process_booked_service(mapping_info)
        self._process_saturday_service(mapping_info)

        return copy.copy(self._service)

    def _process_main_service(self, mapping_info):
        self._execute_callback_by_key(
            key=mapping_info["main_service"],
            callbacks={
                "PRIORITY": self._service.priority,
                "ECONOMY": self._service.economy
            }
        )

    def _process_premium_service(self, mapping_info):
        if mapping_info["premium_service"]:
            self._set_premium_service(mapping_info["premium_service"])

    def _set_premium_service(self, service_key: str):
        self._execute_callback_by_key(
            key=service_key,
            callbacks={
                "AM": self._service.am,
                "PRE-10AM": self._service.pre_10am,
                "TIMED": self._service.timed
            }
        )

    def _process_booked_service(self, mapping_info):
        if mapping_info["booked_service"]:
            self._set_booked_service(mapping_info["booked_service"])

    def _set_booked_service(self, service_key: str):
        self._execute_callback_by_key(
            key=service_key,
            callbacks={
                "BOOK-IN": self._service.book_in,
                "BOOKED": self._service.booked
            }
        )

    def _process_saturday_service(self, mapping_info):
        if mapping_info["saturday_service"]:
            self._service.saturday()

    @staticmethod
    def _execute_callback_by_key(
            key: str, callbacks: dict[str, Callable[[], None]]) -> None:
        callbacks[key]()

    def _mapping_file_contents(self):
        with open(self._file_path()) as json_file:
            return json.load(json_file)

    @staticmethod
    def _file_path():
        relative_path = system_files.load_path("FCL_SERVICE_CODE_MAPPINGS")

        return runfiles.load_path(relative_path)

    def mappings(self):
        return copy.copy(self._mappings)


class FclServiceCodeMap:
    def __init__(self):
        self._map = ServiceCodeMapBuilder().mappings()

    def __getitem__(self, priority_code: int or str) -> Service:
        return copy.copy(self._map[self._normalise(priority_code)])

    def contains(self, priority_code: int or str):
        return self._normalise(priority_code) in self._map

    def __contains__(self, priority_code: int or str):
        return self.contains(self._normalise(priority_code))

    @staticmethod
    def _normalise(priority_code: str) -> int:
        if type(priority_code) is str and priority_code.isnumeric():
            return int(priority_code)

        elif type(priority_code) is int or float:
            return priority_code

        else:
            raise TypeError("Invalid priority code:", priority_code)
