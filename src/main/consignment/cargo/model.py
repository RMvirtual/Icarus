from src.main.consignment.cargo.entry import CargoEntry


class Cargo:
    def __init__(self):
        self._entry_lines: list[CargoEntry] = []

    def add(self, cargo_entry: CargoEntry) -> None:
        for entry in self._entry_lines:
            if entry.pallet_type.__class__ is cargo_entry.pallet_type.__class__:
                entry.total_weight += cargo_entry.total_weight
                entry.number_of_pallets += cargo_entry.number_of_pallets

                return

        self._entry_lines.append(cargo_entry)

    def __iter__(self):
        return self._entry_lines.__iter__()

    def __getitem__(self, index: int) -> CargoEntry:
        return self._entry_lines[index]

    def __len__(self) -> int:
        return len(self._entry_lines)
