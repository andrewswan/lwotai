from labyrinth_test_case import LabyrinthTestCase
from lwotai.countries.country import Country
from lwotai.countries.types import SUNNI
from lwotai.governance import FAIR


class CountryImprovementTest(LabyrinthTestCase):

    def test_improve_country_from_fair_to_good(self):
        # Set up
        country = Country(None, "Somewhere", SUNNI, FAIR, False, 0, False, 2)
        country.aid = 4
        country.make_besieged()
        country.make_regime_change()

        # Invoke
        country.improve_governance()

        # Assert
        self.assertTrue(country.is_good())
        self.assertEqual(0, country.aid)
        self.assertFalse(country.is_besieged())
        self.assertFalse(country.is_regime_change())
