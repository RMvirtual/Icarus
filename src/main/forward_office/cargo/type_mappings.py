import dataclasses
import json
import copy

from src.main.file_system import runfiles, system_files
from src.main.freight.cargo.types import load_package_type, PackageType


class Loader:
    def __init__(self):
        self._load()

    def _load(self):
        cargo_type_mappings_file = system_files.load_path(
            "FCL_CARGO_TYPE_MAPPINGS")

        full_path = runfiles.load_path(cargo_type_mappings_file)

        with open(full_path) as json_file:
            contents = json.load(json_file)

        short_codes_to_package_types = {}

        for package_type in contents:
            short_code = package_type["short_code"]
            mapping_info = package_type["maps_to"]

            the_type = load_package_type(mapping_info["name"])
            the_type.oversize_option = mapping_info["oversize_option"]

            short_codes_to_package_types[short_code] = the_type

        self._field_interpretation = []

        for short_code in short_codes_to_package_types:
            package_type = short_codes_to_package_types[short_code]

            self._field_interpretation.append([
                short_code,
                PackageType,
                dataclasses.field(default=package_type)
            ])

    def all(self):
        return copy.copy(self._field_interpretation)


FclCargoTypeMap = dataclasses.make_dataclass(
    cls_name="FclCargoTypeMap",
    fields=Loader().all()
)
