import unittest
from src.main.freight.cargo.packages.package_types import load


class TestPackageTypesJsonReader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_get_base_type_from_full_pallet(self):
        package_type = load("full")
        self.assertEqual(package_type.base_type, "pallet")

    def test_should_get_oversize_options_after_amendment(self):
        package_type = load("half")
        package_type.oversize_option = "double"

        self.assertEqual("double", package_type.oversize_option)
        self.assertEqual(2, package_type.oversize_multiplier)

    def test_should_error_when_setting_invalid_oversize_option(self):
        package_type = load("quarter")

        with self.assertRaises(ValueError):
            package_type.oversize_option = "quadruple"

    def test_should_show_identical_normal_package_types_as_equal(self):
        package_1 = load("full")
        package_2 = load("full")

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_identical_oversize_package_types_as_equal(self):
        package_1 = load("full")
        package_1.oversize_option = "double"

        package_2 = load("full")
        package_2.oversize_option = "double"

        self.assertTrue(package_1 == package_2)
        self.assertFalse(package_1 != package_2)

    def test_should_show_different_normal_package_types_as_inequal(self):
        package_1 = load("full")
        package_2 = load("half")

        self.assertTrue(package_1 != package_2)
        self.assertFalse(package_1 == package_2)

    def test_should_show_different_oversize_package_types_as_inequal(self):
        package_1 = load("full")
        package_1.oversize_option = "double"

        package_2 = load("full")
        package_2.oversize_option = "triple"

        self.assertTrue(package_1 != package_2)
        self.assertFalse(package_1 == package_2)


if __name__ == '__main__':
    unittest.main()
