from src.main.companies.upn.api.implementation_1.api.cargo.container \
    import UPNCargo

from src.main.companies.upn.api.implementation_1.api.pallets.download.builder \
    import NetworkPalletBuilder


def single_entry_upn_cargo() -> UPNCargo:
    result = UPNCargo()
    result.total_weight = 3000
    builder = NetworkPalletBuilder()
    builder.set_size_constraints(["N"])
    builder.set_type_constraints(["FULL"])
    builder.set_barcode("W123456789")
    builder.set_consignment_barcode("W987654321")
    builder.set_size("N")
    builder.set_type("FULL")

    for i in range(3):
        result.pallets.append(builder.build())

    return result
