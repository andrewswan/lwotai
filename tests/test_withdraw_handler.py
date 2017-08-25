from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth
from postures.posture import SOFT


class WithdrawHandlerTest(LabyrinthTestCase):
    """Test Withdraw"""

    def test_withdraw(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario_2)
        app.set_posture("United States", SOFT)
        self.assertTrue(app.get_country("Afghanistan").is_good())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").get_aid(), 1)
        self.assertEqual(app.get_country("Afghanistan").is_besieged(), False)
        self.assertEqual(app.get_country("Saudi Arabia").troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestige_rolls = (5, 2, 5)
        app.handle_withdraw("Afghanistan", "Saudi Arabia", 4, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_good())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 2)
        self.assertEqual(app.get_country("Afghanistan").get_aid(), 0)
        self.assertEqual(app.get_country("Afghanistan").is_besieged(), True)
        self.assertEqual(app.get_country("Saudi Arabia").troops(), 6)
        self.assertEqual(app.prestige, 9)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario_2)
        app.set_posture("United States", SOFT)
        self.assertTrue(app.get_country("Afghanistan").is_good())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").get_aid(), 1)
        self.assertEqual(app.get_country("Afghanistan").is_besieged(), False)
        self.assertEqual(app.get_country("Saudi Arabia").troops(), 2)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 3)
        prestige_rolls = (2, 3, 5)
        app.handle_withdraw("Afghanistan", "track", 5, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_good())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 1)
        self.assertEqual(app.get_country("Afghanistan").get_aid(), 0)
        self.assertEqual(app.get_country("Afghanistan").is_besieged(), True)
        self.assertEqual(app.get_country("Saudi Arabia").troops(), 2)
        self.assertEqual(app.prestige, 4)
        self.assertEqual(app.troops, 8)
