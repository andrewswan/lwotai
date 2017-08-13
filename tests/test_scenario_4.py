from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class Scenario4Test(LabyrinthTestCase):

    def test_scenario_4(self):
        app = Labyrinth(4, 1)
        for country in app.get_countries():
            if country.schengen:
                self.assertTrue(country.posture)
