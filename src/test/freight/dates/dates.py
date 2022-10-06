import unittest
from src.main.freight.dates.model import ShipmentDates, Date


class TestShipmentDates(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_dates_can_be_compared(self):
        date_1 = Date("06/10/2022")
        date_2 = Date("07/10/2022")

        self.assertTrue(date_1 < date_2)
        self.assertTrue(date_1 <= date_2)
        self.assertFalse(date_1 == date_2)
        self.assertFalse(date_1 > date_2)
        self.assertFalse(date_1 >= date_2)


if __name__ == '__main__':
    unittest.main()