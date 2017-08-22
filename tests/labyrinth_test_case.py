import unittest


class LabyrinthTestCase(unittest.TestCase):
    """Assertions, setup functions, etc. for reuse by subclasses"""

    def assertCells(self, app, country, expected_cells, include_sadr = False):
        """Asserts that the given country contains the given number of cells"""
        self.assertEqual(expected_cells, app.map.get(country).total_cells(include_sadr))

    def assert_new_messages(self, app, message_count_before, expected_messages):
        expected_message_count = len(expected_messages)
        self.assertEquals(len(app.history), message_count_before + expected_message_count)
        new_messages = app.history[-expected_message_count:]
        self.assertEquals(new_messages, expected_messages)

    @staticmethod
    def schengen_countries(app):
        """Returns the Country objects for the Schengen countries"""
        return [country for country in app.map.countries() if country.schengen]

    @staticmethod
    def set_up_test_scenario(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
        app.map.get("Libya").make_poor()
        app.map.get("Libya").make_adversary()
        app.map.get("Syria").make_fair()
        app.map.get("Syria").make_adversary()
        app.map.get("Iraq").make_poor()
        app.map.get("Iraq").make_adversary()
        app.map.get("Iraq").plots = 2
        app.map.get("Saudi Arabia").make_poor()
        app.map.get("Saudi Arabia").make_ally()
        app.map.get("Saudi Arabia").troopCubes = 2
        app.map.get("Pakistan").make_fair()
        app.map.get("Pakistan").make_neutral()
        app.map.get("Pakistan").troopCubes = 2
        app.map.get("Pakistan").activeCells = 4
        app.map.get("Gulf States").make_fair()
        app.map.get("Gulf States").make_ally()
        app.map.get("Gulf States").troopCubes = 4
        app.map.get("Gulf States").sleeperCells = 1
        app.map.get("Gulf States").activeCells = 4
        app.map.get("Afghanistan").make_islamist_rule()
        app.map.get("Afghanistan").make_adversary()
        app.map.get("Afghanistan").sleeperCells = 4
        app.map.get("Somalia").make_besieged()
        app.map.get("United States").make_hard()

    @staticmethod
    def set_up_test_scenario_2(app):
        app.prestige = 7
        app.troops = 3
        app.funding = 9
        app.cells = 11
        app.map.get("Libya").make_poor()
        app.map.get("Libya").make_adversary()
        app.map.get("Syria").make_fair()
        app.map.get("Syria").make_adversary()
        app.map.get("Iraq").make_poor()
        app.map.get("Iraq").make_adversary()
        app.map.get("Iraq").plots = 2
        app.map.get("Saudi Arabia").make_poor()
        app.map.get("Saudi Arabia").make_ally()
        app.map.get("Saudi Arabia").troopCubes = 2
        app.map.get("Pakistan").make_fair()
        app.map.get("Pakistan").make_neutral()
        app.map.get("Pakistan").troopCubes = 2
        app.map.get("Pakistan").activeCells = 4
        app.map.get("Gulf States").make_fair()
        app.map.get("Gulf States").make_ally()
        app.map.get("Gulf States").troopCubes = 2
        app.map.get("Gulf States").sleeperCells = 1
        app.map.get("Gulf States").activeCells = 4
        app.map.get("Afghanistan").make_good()
        app.map.get("Afghanistan").make_ally()
        app.map.get("Afghanistan").activeCells = 4
        app.map.get("Afghanistan").regimeChange = 1
        app.map.get("Afghanistan").troopCubes = 6
        app.map.get("Afghanistan").aid = 1
        app.map.get("Afghanistan").remove_besieged()
        app.map.get("Somalia").make_besieged()
        app.map.get("United States").make_hard()

    @staticmethod
    def set_up_test_scenario_3(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
        app.map.get("Libya").make_poor()
        app.map.get("Libya").make_adversary()
        app.map.get("Syria").make_fair()
        app.map.get("Syria").make_adversary()
        app.map.get("Iraq").make_poor()
        app.map.get("Iraq").make_adversary()
        app.map.get("Iraq").plots = 2
        app.map.get("Saudi Arabia").make_poor()
        app.map.get("Saudi Arabia").make_ally()
        app.map.get("Saudi Arabia").troopCubes = 2
        app.map.get("Pakistan").make_fair()
        app.map.get("Pakistan").make_neutral()
        app.map.get("Pakistan").troopCubes = 2
        app.map.get("Pakistan").activeCells = 4
        app.map.get("Gulf States").make_fair()
        app.map.get("Gulf States").make_ally()
        app.map.get("Gulf States").troopCubes = 4
        app.map.get("Gulf States").sleeperCells = 1
        app.map.get("Gulf States").activeCells = 4
        app.map.get("Afghanistan").make_islamist_rule()
        app.map.get("Afghanistan").make_adversary()
        app.map.get("Afghanistan").sleeperCells = 4
        app.map.get("Somalia").make_besieged()
        app.map.get("United States").make_hard()
        app.map.get("France").make_hard()
        app.map.get("France").cadre = 1
        app.map.get("Spain").make_soft()
        app.map.get("Spain").sleeperCells = 1
        app.map.get("Germany").make_hard()
        app.map.get("Germany").activeCells = 1
        app.map.get("Germany").sleeperCells = 1

    @staticmethod
    def set_up_blank_test_scenario(app):
        app.prestige = 7
        app.troops = 9
        app.funding = 5
        app.cells = 11
