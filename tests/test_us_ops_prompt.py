from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class UsOpsPromptTest(LabyrinthTestCase):

    def test_should_be_able_to_do_anything_with_three_ops(self):
        # Set up
        app = Labyrinth(1, 1)

        # Invoke
        prompt = app.get_us_prompt_to_spend_ops(82)  # Jihadist Videos

        # Check
        self.assertEqual(prompt, "3 Ops available. Use one of: alert, deploy, disrupt, reassessment, regime_change,"
                                 " reserves, war_of_ideas, withdraw")

    def test_should_have_minimal_choice_with_one_ops(self):
        # Set up
        app = Labyrinth(1, 1)

        # Invoke
        prompt = app.get_us_prompt_to_spend_ops(4)  # Moro talks

        # Check
        self.assertEqual(prompt, "1 Ops available. Use one of: deploy, disrupt, reserves, war_of_ideas")
