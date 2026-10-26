# Juan Cardenas
# 10/25/2026
# Module 7.2 Assignment
# Purpose: To test the city_country function and verify that it returns the expected city and country format.

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Verify the function returns the correct city and country."""
        formatted_city = city_country("Berlin", "Germany")
        self.assertEqual(formatted_city, "Berlin, Germany")


if __name__ == "__main__":
    unittest.main()
