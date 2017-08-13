from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class NamesOfCountriesMatchingPredicateTest(LabyrinthTestCase):

    def test_schengen_countries(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)

        # Invoke
        schengen_countries = app.names_of_countries(lambda c: c.schengen)

        # Check
        expected_names = ['France', 'Scandinavia', 'Benelux', 'Italy', 'Germany', 'Spain', 'Eastern Europe']
        self.assertEqual(len(expected_names), len(schengen_countries))
        for expected_name in expected_names:
            self.assertTrue(expected_name in schengen_countries, "Could not find '%s'" % expected_name)
