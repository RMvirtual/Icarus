import dataclasses
from src.main.file_system.upn.api import structures


@dataclasses.dataclass
class MappingValues:
    type: str = ""
    mapping: str = ""
    values: list = None


def fields():
    return _network_consignment_fields(structures.network_consignment())


def _network_consignment_fields(contents: dict[str, dict]):
    return map(json_entry_to_field_values, contents.items())


def json_entry_to_field_values(field) -> list[str, any, MappingValues]:
    key, value = field

    return [key, MappingValues, _to_mapping_values(value)]


def _to_mapping_values(values: dict[str, str or list[str]]) -> MappingValues:
    result = MappingValues()
    result.type = values["type"]
    result.mapping = values["mapping"]
    result.values = values["values"] if "values" in values else []

    return result


NetworkConsignmentStructure = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=fields()
)
