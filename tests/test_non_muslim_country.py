from mockito import mock, verify

from labyrinth_test_case import LabyrinthTestCase
from lwotai.countries.non_muslim import NonMuslimCountry
from lwotai.governance import GOOD
from lwotai.labyrinth import Labyrinth
from lwotai.postures.posture import HARD, SOFT


class NonMuslimCountryTest(LabyrinthTestCase):

    def test_disrupt_summary(self):
        # Set up
        country = NonMuslimCountry(None, "Australia", HARD, GOOD, False)

        # Invoke
        disrupt_summary = country.get_disrupt_summary()

        # Check
        self.assertEqual("Australia - 0 Active Cells, 0 Sleeper Cells, 0 Cadre, Ops Reqd 1, Posture Hard",
                         disrupt_summary)

    def test_posture_roll_of_1_sets_to_soft(self):
        self._assert_test_posture(1, SOFT)

    def test_posture_roll_of_4_sets_to_soft(self):
        self._assert_test_posture(4, SOFT)

    def test_posture_roll_of_5_sets_to_hard(self):
        self._assert_test_posture(5, HARD)

    def test_posture_roll_of_6_sets_to_hard(self):
        self._assert_test_posture(6, HARD)

    def _assert_test_posture(self, roll, expected_posture):
        # Set up
        app = mock(Labyrinth, strict=False)
        country = NonMuslimCountry(app, "Australia", None, GOOD, False)

        # Invoke
        country.test(roll)

        # Check
        self.assertEqual(expected_posture, country.get_posture())
        verify(app).output_to_history("Australia tested, posture %s" % expected_posture, False)
