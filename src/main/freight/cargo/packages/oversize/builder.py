from src.main.freight.cargo.packages.oversize import implementation, interface


class OversizeOptionsBuilder:
    def __init__(self):
        self._current_option = None
        self._default_option = None
        self._options = []

    def add_option(self, name: str, multiplier: float) -> None:
        self._current_option = implementation.OversizeOption(name, multiplier)
        self._options.append(self._current_option)

    def default_to_most_recent(self) -> None:
        self._default_option = self._current_option

    def build(self) -> interface.OversizeOptions:
        if not self._current_option:
            raise ValueError("Must have added at least one option.")

        if not self._default_option:
            self._default_option = self._options[0]

        return implementation.OversizeOptions(
            default=self._default_option, options=self._options)
