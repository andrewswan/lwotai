from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class Map(LabyrinthTestCase):

    def testDeck(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        for country in app.get_countries():
            for link in country.links:
                self.assertTrue(country in link.links)
