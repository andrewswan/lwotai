from unittest import TestCase
from lwotai.labyrinth import Labyrinth


class TestFindCountries(TestCase):
    """Tests the 'find countries' function"""

    game = Labyrinth(1, 1)

    def test_no_such_country(self):
        countries_with_negative_plots = self.game._find_countries(lambda c: c.plots < 0)
        self.assertEqual([], countries_with_negative_plots)

    def test_count_muslim_countries(self):
        muslim_countries = self.game._find_countries(lambda c: c.is_muslim())
        self.assertEqual(len(muslim_countries), 18)

    def test_count_irans(self):
        irans = self.game._find_countries(lambda c: c.name == "Iran")
        self.assertEqual(len(irans), 1)
