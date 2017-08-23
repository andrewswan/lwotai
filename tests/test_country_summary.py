from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class CountrySummary(LabyrinthTestCase):

    def test_non_muslim_country_with_no_markers(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        israel = app.get_country("Israel")

        # Invoke
        summary = israel.summary()

        # Check
        self.assertEqual(summary, "Israel - Posture:Hard\n   Active:0 Sleeper:0 Cadre:0 Plots:0")
