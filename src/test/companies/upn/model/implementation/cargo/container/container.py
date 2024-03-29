import unittest
from src.main.companies.upn.model.implementation.cargo.container.container \
    import UPNCargo

from src.main.companies.upn.model.implementation.cargo.pallets.download \
    import factory


class TestUPNCargo(unittest.TestCase):
    def setUp(self):
        self._cargo = UPNCargo()

    def test_should_add_pallet(self) -> None:
        pallet = factory.network_pallet("FULL", "NORMAL")
        self._cargo.add(pallet, 1000)

        self.assertEqual(1000, self._cargo.total_weight)
        self.assertEqual("FULL", self._cargo.pallets[0].type)
        self.assertEqual("NORMAL", self._cargo.pallets[0].size)


if __name__ == '__main__':
    unittest.main()
