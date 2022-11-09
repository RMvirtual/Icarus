import dataclasses
import datetime

from src.main.upn.api.structures.network_consignment.mapping \
    import NetworkConsignmentStructure

from src.main.upn.api.structures.network_pallet.structure \
    import NetworkPallet

from src.main.upn.api.structures.primitives import base_types
from src.main.upn.api.structures.primitives import arrays


def network_consignment_fields():
    structure = NetworkConsignmentStructure()
    field_names = dataclasses.fields(structure)

    new_fields = []

    for field in field_names:
        mapping_values = getattr(structure, field.name)
        field_type = get_field_type(mapping_values.type)
        field_instance = get_field_instance(field_type)

        new_fields.append([field.name, field_type, field_instance])

    return new_fields


def get_field_type(mapping_type_name: str) -> type:
    if base_types.is_primitive(mapping_type_name):
        return base_types.get_primitive(mapping_type_name)

    elif mapping_type_name == "network_pallet":
        return NetworkPallet

    elif arrays.is_array(mapping_type_name):
        nested_type_name = arrays.extract_array_object_name(mapping_type_name)
        nested_type = get_field_type(nested_type_name)

        return list[nested_type]

    else:
        raise ValueError(
            "Mapping type of " + mapping_type_name + " not found.")


def get_field_instance(field_type: type):
    if field_type == list[NetworkPallet]:
        return dataclasses.field(default_factory=list[NetworkPallet])

    elif field_type is datetime.datetime:
        return None

    else:
        return field_type()


NetworkConsignment = dataclasses.make_dataclass(
    cls_name="NetworkConsignment",
    fields=network_consignment_fields()
)