from lwotai.governance import GOOD

from lwotai.postures.posture import HARD

from lwotai.countries.non_muslim import NonMuslimCountry

from labyrinth_test_case import LabyrinthTestCase


class NonMuslimCountryTest(LabyrinthTestCase):

    def test_disrupt_summary(self):
        # Set up
        country = NonMuslimCountry(None, "Australia", HARD, GOOD, False)

        # Invoke
        disrupt_summary = country.get_disrupt_summary()

        # Check
        self.assertEqual("Australia - 0 Active Cells, 0 Sleeper Cells, 0 Cadre, Ops Reqd 1, Posture Hard",
                         disrupt_summary)
