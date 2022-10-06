import unittest

from src.main.forward_office.consignment_import.controller \
    import FclImportController


class TestFclImportController(unittest.TestCase):
    def setUp(self) -> None:
        self._import_format = {
            'contact_name': 0, 'company_name': 1, 'address_line_1': 2,
            'address_line_2': 3, 'address_line_3': 4, 'town': 5,
            'post_code': 6, 'reference': 7, 'telephone_no': 8,
            'line_1_weight': 9, 'line_1_quantity': 10,
            'line_1_package_type': 11, 'line_1_description': 12,
            'principal_client': 13, 'line_2_weight': 14,
            'line_2_quantity': 15, 'line_2_package_type': 16,
            'line_2_description': 17, 'line_3_weight': 18,
            'line_3_quantity': 19, 'line_3_package_type': 20,
            'line_3_description': 21, 'line_4_weight': 22,
            'line_4_quantity': 23, 'line_4_package_type': 24,
            'line_4_description': 25, 'delivery_instruction_1': 26,
            'delivery_instruction_2': 27, 'booking_time': 28,
            'delivery_date': 29, 'shipper_reference': 30,
            'total_pallets': 31, 'priority_code': 32,
            'tail_lift_required': 33
        }

        self._simple_example = [[
            "Ryan Matfen", "Graylaw Freight Group", "Gillibrands Road",
            "", "", "Skelmersdale",
            "WN8 9TA", "GR221003000", "01695 729101",
            "500", "1", "PALL", "PALLETS N/D",
            "Disneyworld",
            "", "", "", "",
            "", "", "", "",
            "", "", "", "",
            "Tail Lift", "",
            "", "06-Oct-23", "OL1234",
            "1", "02", "Yes"
        ]]

    def test_should_import_one_liner_consignment(self):
        importer = FclImportController(self._import_format)
        report = importer.import_consignments(self._simple_example)

        self.assertEqual(1, len(report.consignments))
        self.assertFalse(report.errors)
        self.assertFalse(report.advisories)


if __name__ == '__main__':
    unittest.main()
