from unittest import TestCase

from lwotai.countries.non_muslim import NonMuslimCountry

from lwotai.countries.muslim import MuslimCountry
from lwotai.countries.types import SUNNI
from lwotai.governance import FAIR, GOOD


class SetGovernanceTest(TestCase):

    def test_muslim_country_can_be_set_to_fair(self):
        # Set up
        lebanon = MuslimCountry(None, "Somewhere", SUNNI, False, 0)

        # Invoke
        lebanon.set_governance(FAIR)

        # Check
        self.assertEqual(FAIR, lebanon.get_governance())

    def test_governance_of_non_muslim_country_cannot_be_changed(self):
        # Set up
        country = NonMuslimCountry(None, "Aussie", None, None, False)

        # Invoke and check
        with self.assertRaises(Exception):
            country.set_governance(GOOD)
