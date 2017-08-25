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

    @staticmethod
    def test_can_check_is_tested():
        # Set up
        iran = Iran(None)

        # Invoke
        iran.check_is_tested()

    def test_major_jihad_is_not_possible(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = Iran(app)
        iran.sleeperCells = 5
        iran.change_troops(-999)

        # Invoke
        major_jihad_possible = iran.is_major_jihad_possible(3, 5, False)

        # Check
        self.assertFalse(major_jihad_possible)

    def test_cannot_be_made_hard(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = Iran(app)

        # Invoke
        try:
            iran.make_hard()
            self.fail("Should have raised an Exception")
        except Exception as e:
            # Check
            self.assertEqual("Not in Iran", e.message)

