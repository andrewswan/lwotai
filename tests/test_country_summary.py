from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class CountrySummary(LabyrinthTestCase):

    def test_non_muslim_country_with_no_markers(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        israel = app.get_country("Israel")
        israel.plots = 2

        # Invoke
        summary = israel.summary()

        # Check
        self.assertEqual(summary, "Israel - Posture: Hard\n    Plots: 2")

    def test_iran_with_nothing_in_it(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = app.get_country("Iran")

        # Invoke
        summary = iran.summary()

        # Check
        self.assertEqual(summary, "Iran, Fair")

    def test_iran_with_things_in_it(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = app.get_country("Iran")
        iran.plots = 3
        iran.activeCells = 4

        # Invoke
        summary = iran.summary()

        # Check
        self.assertEqual(summary, "Iran, Fair\n    Active: 4, Plots: 3")
