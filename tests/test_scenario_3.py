from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class Scenario3Test(LabyrinthTestCase):

    def test_scenario_3_places_5_sleeper_cells(self):
        app = Labyrinth(3, 1)
        sleeper_cells = sum([country.sleeperCells for country in app.get_countries()])
        self.assertEqual(5, sleeper_cells)
