from labyrinth_test_case import LabyrinthTestCase
from lwotai.alignment import ADVERSARY
from lwotai.governance import ISLAMIST_RULE
from lwotai.labyrinth import Labyrinth


class Scenario1Test(LabyrinthTestCase):

    def test_scenario_1_makes_afghanistan_islamist_rule_adversary(self):
        # Set up
        app = Labyrinth(1, 1)
        afghanistan = app.get_country("Afghanistan")

        # Invoke
        alignment = afghanistan.alignment()
        governance = afghanistan.get_governance()

        # Check
        self.assertEqual(ADVERSARY, alignment)
        self.assertEqual(ISLAMIST_RULE, governance)
