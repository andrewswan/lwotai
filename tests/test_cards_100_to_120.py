import unittest

from labyrinth_test_case import LabyrinthTestCase
from lwotai.governance import GOOD
from lwotai.labyrinth import Labyrinth


class Card100(LabyrinthTestCase):
    """His Ut-Tahrir"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(100).playable("US", app, True))
        self.assertTrue(app.card(100).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(100).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(100).playEvent("US", app)
        self.assertEqual(app.funding, 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(100).playEvent("Jihadist", app)
        self.assertEqual(app.funding, 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.card(100).playEvent("US", app)
        self.assertEqual(app.funding, 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.card(100).playEvent("Jihadist", app)
        self.assertEqual(app.funding, 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 10
        app.card(100).playEvent("US", app)
        self.assertEqual(app.funding, 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 10
        app.card(100).playEvent("Jihadist", app)
        self.assertEqual(app.funding, 3)


class Card101(LabyrinthTestCase):
    """Kosovo"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(101).playable("US", app, True))
        self.assertTrue(app.card(101).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(101).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(101).playEvent("US", app)
        self.assertEqual(app.prestige, 8)
        self.assertEqual(app.get_posture("Serbia"), "Soft")

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.set_posture("United States", "Soft")
        app.card(101).playEvent("Jihadist", app)
        self.assertEqual(app.prestige, 8)
        self.assertEqual(app.get_posture("Serbia"), "Hard")


class Card102(LabyrinthTestCase):
    """Former Soviet Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(102).playable("US", app, True))
        self.assertTrue(app.card(102).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(102).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(102).playEvent("US", app)
        self.assertTrue(app.get_country("Central Asia").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Central Asia")
        app.get_country("Central Asia").make_good()
        app.get_country("Central Asia").make_ally()
        app.card(102).playEvent("Jihadist", app)
        self.assertFalse(app.get_country("Central Asia").is_good())
        self.assertTrue(app.get_country("Central Asia").is_neutral())


class Card103(LabyrinthTestCase):
    """Hizballah"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(103).playable("US", app, True))
        self.assertTrue(app.card(103).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(103).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.card(103).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(103).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_poor())
        self.assertTrue(app.get_country("Lebanon").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Lebanon")
        app.get_country("Lebanon").make_good()
        app.get_country("Lebanon").make_ally()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").make_ally()
        app.card(103).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_poor())
        self.assertTrue(app.get_country("Lebanon").is_neutral())

        # no countries
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.card(103).playEvent("US", app)

        # one country
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.test_country("Gulf States")
        app.get_country("Gulf States").sleeperCells = 1
        app.card(103).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)


class Card104(LabyrinthTestCase):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(104).playable("US", app, True))
        self.assertTrue(app.card(104).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(104).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.card(104).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Yemen"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.test_country("Yemen")
        app.get_country("Yemen").sleeperCells = 1
        app.card(104).playEvent("US", app)
        self.assertEqual(app.get_country("Yemen").sleeperCells, 0)

        app.card(104).playEvent("Jihadist", app)


class Card105(LabyrinthTestCase):
    """Iran"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(105).playable("US", app, True))
        self.assertTrue(app.card(105).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(105).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.card(105).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Yemen"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.test_country("Yemen")
        app.get_country("Yemen").sleeperCells = 1
        app.card(105).playEvent("US", app)
        self.assertEqual(app.get_country("Yemen").sleeperCells, 0)

        app.card(105).playEvent("Jihadist", app)


class Card106(LabyrinthTestCase):
    """Jaysh al-Mahdi"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(106).playable("US", app, True))
        self.assertFalse(app.card(106).playable("Jihadist", app, False))
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        self.assertFalse(app.card(106).playable("US", app, True))
        self.assertFalse(app.card(106).playable("Jihadist", app, False))
        app.get_country("Iraq").troopCubes = 1
        self.assertTrue(app.card(106).playable("US", app, True))
        self.assertTrue(app.card(106).playable("Jihadist", app, False))
        app.get_country("Iraq").sleeperCells = 0
        self.assertFalse(app.card(106).playable("US", app, True))
        self.assertFalse(app.card(106).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(106).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 3
        app.get_country("Iraq").troopCubes = 1
        app.card(106).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 2
        app.get_country("Iraq").troopCubes = 1
        app.card(106).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").troopCubes = 1
        app.card(106).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Lebanon"])
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 2
        app.get_country("Iraq").troopCubes = 1
        app.get_country("Lebanon").sleeperCells = 2
        app.get_country("Lebanon").troopCubes = 1
        print "Choose Lebanon"
        app.card(106).playEvent("US", app)
        self.assertEqual(app.get_country("Lebanon").sleeperCells, 0)

        print "HERE"
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 2
        app.get_country("Iraq").troopCubes = 1
        app.card(106).playEvent("Jihadist", app)


class Card107(LabyrinthTestCase):
    """Kurdistan"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(107).playable("US", app, True))
        self.assertTrue(app.card(107).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(107).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.card(107).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").aid, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(107).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Turkey").is_poor())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_good()
        app.card(107).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Turkey").governance_is_worse_than(GOOD))
        self.assertTrue(app.get_country("Iraq").is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_fair()
        app.test_country("Turkey")
        app.get_country("Turkey").make_fair()
        app.get_country("Turkey").aid = 1
        app.card(107).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Turkey").is_poor())
        self.assertTrue(app.get_country("Iraq").is_fair())


class Card108(LabyrinthTestCase):
    """Musharraf"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(108).playable("US", app, True))
        self.assertFalse(app.card(108).playable("Jihadist", app, False))
        app.test_country("Pakistan")
        app.get_country("Pakistan").activeCells = 1
        self.assertTrue(app.card(108).playable("US", app, True))
        self.assertTrue(app.card(108).playable("Jihadist", app, False))
        app.markers.append("Benazir Bhutto")
        self.assertFalse(app.card(108).playable("US", app, True))
        self.assertFalse(app.card(108).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(108).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 1
        app.get_country("Pakistan").make_good()
        app.card(108).playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.get_country("Pakistan").is_poor())
        self.assertTrue(app.get_country("Pakistan").is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 3
        app.get_country("Pakistan").make_islamist_rule()
        app.get_country("Pakistan").make_adversary()
        app.card(108).playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 2, True)
        self.assertTrue(app.get_country("Pakistan").is_poor())
        self.assertTrue(app.get_country("Pakistan").is_ally())


class Card109(LabyrinthTestCase):
    """Tora Bora"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(109).playable("US", app, True))
        self.assertFalse(app.card(109).playable("Jihadist", app, False))
        app.test_country("Pakistan")
        app.get_country("Pakistan").activeCells = 2
        self.assertFalse(app.card(109).playable("US", app, True))
        self.assertFalse(app.card(109).playable("Jihadist", app, False))
        app.get_country("Pakistan").regimeChange = 1
        self.assertTrue(app.card(109).playable("US", app, True))
        self.assertTrue(app.card(109).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(109).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 2
        app.get_country("Pakistan").regimeChange = 1
        app.card(109).playEvent("US", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 2
        app.get_country("Pakistan").regimeChange = 1
        app.card(109).playEvent("Jihadist", app)
        self.assertCells(app, "Pakistan", 0, True)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 2
        app.get_country("Pakistan").regimeChange = 1
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 2
        app.get_country("Iraq").regimeChange = 1
        print "Choose Iraq"
        app.card(109).playEvent("US", app)
        self.assertCells(app, "Iraq", 0, True)
        self.assertTrue(app.prestige != 7)


class Card110(LabyrinthTestCase):
    """Zarqawi"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(110).playable("US", app, True))
        self.assertFalse(app.card(110).playable("Jihadist", app, False))
        app.test_country("Iraq")
        app.get_country("Iraq").troopCubes = 1
        self.assertTrue(app.card(110).playable("US", app, True))
        self.assertTrue(app.card(110).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(110).playable("US", app, True))
        self.assertFalse(app.card(110).playable("Jihadist", app, False))
        app.test_country("Syria")
        app.get_country("Syria").troopCubes = 1
        self.assertTrue(app.card(110).playable("US", app, True))
        self.assertTrue(app.card(110).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(110).playable("US", app, True))
        self.assertFalse(app.card(110).playable("Jihadist", app, False))
        app.test_country("Lebanon")
        app.get_country("Lebanon").troopCubes = 1
        self.assertTrue(app.card(110).playable("US", app, True))
        self.assertTrue(app.card(110).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(110).playable("US", app, True))
        self.assertFalse(app.card(110).playable("Jihadist", app, False))
        app.test_country("Jordan")
        app.get_country("Jordan").troopCubes = 1
        self.assertTrue(app.card(110).playable("US", app, True))
        self.assertTrue(app.card(110).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(110).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").troopCubes = 2
        app.card(110).playEvent("US", app)
        self.assertEqual(app.prestige, 10)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").troopCubes = 2
        app.card(110).playEvent("Jihadist", app)
        self.assertEqual(app.get_country("Iraq").total_cells(True), 3)
        self.assertEqual(app.get_country("Iraq").plots, 1)


class Card111(LabyrinthTestCase):
    """Zawahiri"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(111).playable("US", app, True))
        self.assertTrue(app.card(111).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_islamist_rule()
        self.assertFalse(app.card(111).playable("US", app, True))
        self.assertTrue(app.card(111).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").markers.append("FATA")
        self.assertFalse(app.card(111).playable("US", app, True))
        self.assertTrue(app.card(111).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.card(111).playable("US", app, True))
        self.assertTrue(app.card(111).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(111).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(111).playEvent("US", app)
        self.assertEqual(app.funding, 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(111).playEvent("Jihadist", app)
        self.assertEqual(app.prestige, 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_islamist_rule()
        app.card(111).playEvent("Jihadist", app)
        self.assertEqual(app.prestige, 4)


class Card112(LabyrinthTestCase):
    """Bin Ladin"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(112).playable("US", app, True))
        self.assertTrue(app.card(112).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_islamist_rule()
        self.assertFalse(app.card(112).playable("US", app, True))
        self.assertTrue(app.card(112).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.get_country("Pakistan").markers.append("FATA")
        self.assertFalse(app.card(112).playable("US", app, True))
        self.assertTrue(app.card(112).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Pakistan")
        app.markers.append("Al-Anbar")
        self.assertFalse(app.card(112).playable("US", app, True))
        self.assertTrue(app.card(112).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(112).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(112).playEvent("US", app)
        self.assertEqual(app.funding, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(112).playEvent("Jihadist", app)
        self.assertEqual(app.prestige, 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_islamist_rule()
        app.card(112).playEvent("Jihadist", app)
        self.assertEqual(app.prestige, 3)


class Card113(LabyrinthTestCase):
    """Darfur"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(113).playable("US", app, True))
        self.assertTrue(app.card(113).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(113).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(113).playEvent("US", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").aid, 1)
        self.assertTrue(app.get_country("Sudan").is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Sudan")
        app.get_country("Sudan").make_adversary()
        app.card(113).playEvent("US", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").aid, 1)
        self.assertTrue(app.get_country("Sudan").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.card(113).playEvent("US", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").besieged, 1)
        self.assertTrue(app.get_country("Sudan").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.test_country("Sudan")
        app.get_country("Sudan").make_ally()
        app.card(113).playEvent("US", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").besieged, 1)
        self.assertTrue(app.get_country("Sudan").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(113).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").aid, 1)
        self.assertTrue(app.get_country("Sudan").is_ally())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Sudan")
        app.get_country("Sudan").make_adversary()
        app.card(113).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").aid, 1)
        self.assertTrue(app.get_country("Sudan").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.card(113).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").besieged, 1)
        self.assertTrue(app.get_country("Sudan").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 6
        app.test_country("Sudan")
        app.get_country("Sudan").make_ally()
        app.card(113).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Sudan").is_governed())
        self.assertEqual(app.get_country("Sudan").besieged, 1)
        self.assertTrue(app.get_country("Sudan").is_neutral())


class Card114(LabyrinthTestCase):
    """GTMO"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(114).playable("US", app, True))
        self.assertTrue(app.card(114).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(114).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(114).playEvent("US", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(114).playEvent("Jihadist", app)
        self.assertTrue("GTMO" in app.lapsing)
        self.assertTrue(app.prestige != 7)


class Card115(LabyrinthTestCase):
    """Hambali"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.test_country("Indonesia/Malaysia")
        app.get_country("Indonesia/Malaysia").sleeperCells = 1
        app.get_country("Indonesia/Malaysia").make_ally()
        self.assertTrue(app.card(115).playable("US", app, True))
        self.assertTrue(app.card(115).playable("Jihadist", app, False))
        app.get_country("Indonesia/Malaysia").sleeperCells = 0
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.get_country("Indonesia/Malaysia").sleeperCells = 1
        app.get_country("Indonesia/Malaysia").make_neutral()
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.test_country("Pakistan")
        app.get_country("Pakistan").sleeperCells = 1
        app.get_country("Pakistan").make_ally()
        self.assertTrue(app.card(115).playable("US", app, True))
        self.assertTrue(app.card(115).playable("Jihadist", app, False))
        app.get_country("Pakistan").sleeperCells = 0
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.get_country("Pakistan").sleeperCells = 1
        app.get_country("Pakistan").make_neutral()
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.test_country("India")
        app.get_country("India").sleeperCells = 1
        app.set_posture("India", "Hard")
        self.assertTrue(app.card(115).playable("US", app, True))
        self.assertTrue(app.card(115).playable("Jihadist", app, False))
        app.get_country("India").sleeperCells = 0
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.get_country("India").sleeperCells = 1
        app.set_posture("India", "Soft")
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.test_country("Thailand")
        app.get_country("Thailand").sleeperCells = 1
        app.set_posture("Thailand", "Hard")
        self.assertTrue(app.card(115).playable("US", app, True))
        self.assertTrue(app.card(115).playable("Jihadist", app, False))
        app.get_country("Thailand").sleeperCells = 0
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.get_country("Thailand").sleeperCells = 1
        app.set_posture("Thailand", "Soft")
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.test_country("Philippines")
        app.get_country("Philippines").sleeperCells = 1
        app.set_posture("Philippines", "Hard")
        self.assertTrue(app.card(115).playable("US", app, True))
        self.assertTrue(app.card(115).playable("Jihadist", app, False))
        app.get_country("Philippines").sleeperCells = 0
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))
        app.get_country("Philippines").sleeperCells = 1
        app.set_posture("Philippines", "Soft")
        self.assertFalse(app.card(115).playable("US", app, True))
        self.assertFalse(app.card(115).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(115).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Philippines")
        app.get_country("Philippines").sleeperCells = 1
        app.set_posture("Philippines", "Hard")
        app.card(115).playEvent("US", app)
        self.assertEqual(app.get_country("Philippines").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Indonesia/Malaysia"])
        app.test_country("Indonesia/Malaysia")
        app.get_country("Indonesia/Malaysia").sleeperCells = 1
        app.get_country("Indonesia/Malaysia").make_ally()
        app.test_country("Philippines")
        app.get_country("Philippines").sleeperCells = 1
        app.set_posture("Philippines", "Hard")
        print "Choose Indonesia/Malaysia"
        app.card(115).playEvent("US", app)
        self.assertEqual(app.get_country("Indonesia/Malaysia").sleeperCells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Indonesia/Malaysia")
        app.get_country("Indonesia/Malaysia").sleeperCells = 1
        app.get_country("Indonesia/Malaysia").make_ally()
        app.card(115).playEvent("Jihadist", app)
        self.assertEqual(app.get_country("Indonesia/Malaysia").plots, 1)


class Card116(LabyrinthTestCase):
    """KSM"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(116).playable("Jihadist", app, False))
        self.assertFalse(app.card(116).playable("US", app, True))
        app.test_country("Iraq")
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").plots = 1
        self.assertTrue(app.card(116).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(116).playable("Jihadist", app, False))
        self.assertFalse(app.card(116).playable("US", app, True))
        app.test_country("Canada")
        app.get_country("Canada").plots = 1
        self.assertTrue(app.card(116).playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(116).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").plots = 2
        app.test_country("Pakistan")
        app.get_country("Pakistan").make_neutral()
        app.get_country("Pakistan").plots = 2
        app.test_country("Canada")
        app.get_country("Canada").plots = 1
        app.card(116).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").plots, 0)
        self.assertEqual(app.get_country("Pakistan").plots, 2)
        self.assertEqual(app.get_country("Canada").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.card(116).playEvent("Jihadist", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.get_country("Iraq").activeCells, 0)
        self.assertEqual(app.get_country("Iraq").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").make_islamist_rule()
        app.get_country("Iraq").sleeperCells = 1
        app.card(116).playEvent("Jihadist", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.get_country("Iraq").activeCells, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.card(116).playEvent("Jihadist", app)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.get_country("Iraq").activeCells, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.get_country("United States").activeCells, 0)
        self.assertEqual(app.get_country("United States").plots, 1)


class Card117(LabyrinthTestCase):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(117).playable("Jihadist", app, False))
        self.assertTrue(app.card(117).playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(117).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(117).playEvent("US", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y"])
        app.card(117).playEvent("Jihadist", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 4)
        app.card(117).playEvent("US", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 5)


class Card118(LabyrinthTestCase):
    """Oil Price Spike"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(118).playable("Jihadist", app, False))
        self.assertTrue(app.card(118).playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(118).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(118).playEvent("US", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y"])
        app.card(118).playEvent("Jihadist", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 4)
        app.card(118).playEvent("US", app)
        self.assertEqual(app.country_resources_by_name("Saudi Arabia"), 5)


class Card119(LabyrinthTestCase):
    """Saleh"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(119).playable("Jihadist", app, False))
        self.assertTrue(app.card(119).playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(119).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(119).playEvent("US", app)
        self.assertTrue(app.get_country("Yemen").is_governed())
        self.assertTrue(app.get_country("Yemen").is_ally())
        self.assertEqual(app.get_country("Yemen").aid, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Yemen").make_islamist_rule()
        app.get_country("Yemen").make_neutral()
        app.card(119).playEvent("US", app)
        self.assertTrue(app.get_country("Yemen").is_governed())
        self.assertTrue(app.get_country("Yemen").is_neutral())
        self.assertEqual(app.get_country("Yemen").aid, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(119).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Yemen").is_governed())
        self.assertTrue(app.get_country("Yemen").is_adversary())
        self.assertEqual(app.get_country("Yemen").besieged, 1)


class Card120(LabyrinthTestCase):
    """US Election"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(120).playable("Jihadist", app, False))
        self.assertTrue(app.card(120).playable("US", app, True))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(120).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.execute_card_us_election(5)
        self.assertEqual(app.prestige, 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.execute_card_us_election(4)
        self.assertEqual(app.prestige, 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(120).playEvent("US", app)
        self.assertTrue(app.prestige != 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(120).playEvent("US", app)
        self.assertTrue(app.prestige != 7)


if __name__ == "__main__":
    unittest.main()   