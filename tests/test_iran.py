from countries.iran import Iran
from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class IranTest(LabyrinthTestCase):
    """Tests the special-case country of Iran"""

    def test_is_fair(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = Iran(app)

        # Invoke
        result = iran.is_fair()

        # Check
        self.assertTrue(result)

    def test_is_not_good(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = Iran(app)

        # Invoke
        result = iran.is_good()

        # Check
        self.assertFalse(result)
