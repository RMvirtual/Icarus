from src.main.file_system.file_readers import runfiles


def network_consignment_keys():
    return _api_file_contents("consignments/network/keys.json")


def network_consignment_constraints():
    return _api_file_contents("consignments/network/constraints.json")


def network_pallet_keys():
    return _api_file_contents("pallets/network/keys.json")


def network_pallet_constraints():
    return _api_file_contents("pallets/network/constraints.json")


def primitives():
    return _api_file_contents("data_types/primitives.json")


def _api_file_contents(file_name: str):
    return runfiles.load_json_file(_api_file_path(file_name))


def _api_file_path(file_name: str) -> str:
    return "resources/companies/upn/api/" + file_name
