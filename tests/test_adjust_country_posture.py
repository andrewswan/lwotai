from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth
from postures.posture import HARD, SOFT


class AdjustCountryPosture(LabyrinthTestCase):
    """Tests the 'adjustCountryPosture' method"""

    def test_accepts_mixed_case_input(self):
        self._assert_adjust_posture("Hard", HARD)

    def test_accepts_lower_case_input(self):
        self._assert_adjust_posture("hard", HARD)

    def test_accepts_upper_case_input(self):
        self._assert_adjust_posture("HARD", HARD)

    def test_set_soft_posture(self):
        self._assert_adjust_posture("soft", SOFT)

    def test_set_untested_posture(self):
        self._assert_adjust_posture("UNTESTED", None)

    def test_set_no_posture(self):
        self._assert_adjust_posture("bad input lalala", None, False)

    def _assert_adjust_posture(self, user_input, expected_posture, expected_successful=True):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario, test_user_input=[user_input])
        country = app.get_country("France")  # Only non-muslim countries have a posture
        self.assertEqual(country.get_posture(), None)  # means "Untested"

        # Invoke
        successful = app.adjust_country_posture(country.name)

        # Check
        self.assertEqual(successful, expected_successful)
        self.assertEqual(country.get_posture(), expected_posture)
