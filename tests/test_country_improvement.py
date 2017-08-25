from labyrinth_test_case import LabyrinthTestCase
from lwotai.countries.muslim import MuslimCountry
from lwotai.countries.types import SUNNI


class CountryImprovementTest(LabyrinthTestCase):

    def test_improve_country_from_fair_to_good(self):
        # Set up
        country = MuslimCountry(None, "Somewhere", SUNNI, False, 0)
        country.set_aid(4)
        country.make_fair()
        country.make_besieged()
        country.make_regime_change()

        # Invoke
        country.improve_governance()

        # Assert
        self.assertTrue(country.is_good())
        self.assertEqual(0, country.get_aid())
        self.assertFalse(country.is_besieged())
        self.assertFalse(country.is_regime_change())
