from countries.muslim import MuslimCountry
from countries.non_muslim import NonMuslimCountry
from labyrinth_test_case import LabyrinthTestCase
from lwotai.countries.types import SHIA_MIX
from lwotai.governance import FAIR
from lwotai.labyrinth import Labyrinth


class DisruptTest(LabyrinthTestCase):

    def test_cannot_disrupt_in_neutral_muslim_country_with_no_troops(self):
        # Set up
        country = MuslimCountry(None, "Somewhere", SHIA_MIX, False, 0, False)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 0

        # Invoke & assert
        self.assertFalse(country.can_disrupt())

    def test_cannot_disrupt_in_neutral_muslim_country_with_one_troop(self):
        # Set up
        country = MuslimCountry(None, "Somewhere", SHIA_MIX, False, 0, False)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 1

        # Invoke & assert
        self.assertFalse(country.can_disrupt())

    def test_can_disrupt_in_neutral_muslim_country_with_two_troops(self):
        # Set up
        country = MuslimCountry(None, "Somewhere", SHIA_MIX, False, 0, False)
        country.cadre = 1
        country.make_neutral()
        country.troopCubes = 2

        # Invoke & assert
        self.assertTrue(country.can_disrupt())

    def test_can_disrupt_in_allied_muslim_country_with_no_troops(self):
        # Set up
        country = MuslimCountry(None, "Somewhere", SHIA_MIX, False, 0, False)
        country.cadre = 1
        country.make_ally()
        country.make_fair()
        country.troopCubes = 0

        # Invoke & assert
        self.assertTrue(country.can_disrupt())

    def test_can_disrupt_in_non_muslim_country_with_no_troops(self):
        # Set up
        country = NonMuslimCountry(None, "Somewhere", None, FAIR, False)
        country.cadre = 1
        country.troopCubes = 0

        # Invoke & assert
        self.assertTrue(country.can_disrupt())

    def test_num_disruptable(self):
        # Set up
        app = Labyrinth(1, 1)
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").make_ally()
        app.get_country("Jordan").sleeperCells = 1
        app.get_country("Jordan").troopCubes = 2
        app.get_country("Libya").sleeperCells = 1
        app.get_country("Libya").troopCubes = 1  # Should not be enough

        # Invoke & assert
        self.assertEqual(app.num_disruptable(), 3)
