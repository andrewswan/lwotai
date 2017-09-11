from lwotai.labyrinth import Labyrinth
from labyrinth_test_case import LabyrinthTestCase


class ReservesTest(LabyrinthTestCase):
    """Tests the "reserves" command"""

    def test_adding_three_ops_only_sets_to_two(self):
        # Set up
        app = Labyrinth(1, 1, LabyrinthTestCase.set_up_blank_test_scenario)
        assert app.us_reserves == 0
        app.play_us_card(116)  # 3 ops

        # Invoke
        app.deploy_reserves()

        # Check
        self.assertEqual(2, app.us_reserves)
