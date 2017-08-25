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

    def test_is_not_schengen(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = Iran(app)

        # Invoke
        schengen = iran.schengen

        # Check
        self.assertFalse(schengen)

    def test_can_check_is_tested(self):
        # Set up
        iran = Iran(None)

        # Invoke
        iran.check_is_tested()
