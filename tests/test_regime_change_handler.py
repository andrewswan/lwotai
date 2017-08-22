from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class RegimeChangeHandlerTest(LabyrinthTestCase):
    """Test Regime Change"""

    def test_regime_change(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_soft()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 4
        prestige_rolls = (3, 2, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 4
        prestige_rolls = (3, 2, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_poor())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 5)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 5
        prestige_rolls = (3, 2, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_fair())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 5)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 5
        prestige_rolls = (5, 2, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_fair())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 9)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 5
        prestige_rolls = (2, 6, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_fair())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 2)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 9)
        gov_roll = 5
        prestige_rolls = (6, 6, 5)
        app.handle_regime_change("Afghanistan", "track", 6, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_fair())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 6)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 12)
        self.assertEqual(app.troops, 3)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.troops -= 8
        app.get_country("Pakistan").change_troops(8)
        app.get_country("United States").make_hard()
        self.assertTrue(app.get_country("Afghanistan").is_islamist_rule())
        self.assertTrue(app.get_country("Afghanistan").is_adversary())
        self.assertEqual(app.get_country("Afghanistan").troops(), 0)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 4)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 0)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.troops, 1)
        self.assertEqual(app.get_country("Pakistan").troops(), 10)
        gov_roll = 5
        prestige_rolls = (6, 6, 5)
        app.handle_regime_change("Afghanistan", "Pakistan", 7, gov_roll, prestige_rolls)
        self.assertTrue(app.get_country("Afghanistan").is_fair())
        self.assertTrue(app.get_country("Afghanistan").is_ally())
        self.assertEqual(app.get_country("Afghanistan").troops(), 7)
        self.assertEqual(app.get_country("Afghanistan").sleeperCells, 0)
        self.assertEqual(app.get_country("Afghanistan").activeCells, 4)
        self.assertEqual(app.get_country("Afghanistan").regimeChange, 1)
        self.assertEqual(app.prestige, 12)
        self.assertEqual(app.troops, 1)
        self.assertEqual(app.get_country("Pakistan").troops(), 3)
