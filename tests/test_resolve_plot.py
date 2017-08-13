from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class ResolvePlotTest(LabyrinthTestCase):
    """Resolve _plots"""

    def test_resolve_non_muslim_non_us_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Germany").plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.get_country("Germany").posture, "Soft")
        self.assertEqual(app.get_country("Spain").posture, "Hard")
        self.assertEqual(app.get_country("Scandinavia").posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Germany").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Germany").plots = 2
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.get_country("Germany").posture, "Soft")
        self.assertEqual(app.get_country("Spain").posture, "Hard")
        self.assertEqual(app.get_country("Scandinavia").posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Germany").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Germany").plots = 1
        app.resolvePlot("Germany", 2, 5, [], ["Spain", "Scandinavia"], [4, 5], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.get_country("Germany").posture, "Hard")
        self.assertEqual(app.get_country("Spain").posture, "Soft")
        self.assertEqual(app.get_country("Scandinavia").posture, "Hard")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Germany").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").plots = 1
        app.resolvePlot("Canada", 2, 5, [], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.get_country("Canada").posture, "Hard")
        self.assertEqual(app.get_country("Spain").posture, "")
        self.assertEqual(app.get_country("Scandinavia").posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Canada").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Russia").plots = 1
        app.resolvePlot("Russia", 2, 4, [], [], [], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.get_country("Russia").posture, "Soft")
        self.assertEqual(app.get_country("Spain").posture, "")
        self.assertEqual(app.get_country("Scandinavia").posture, "")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Russia").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Germany").plots = 1
        app.resolvePlot("Germany", 1, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.get_country("Germany").posture, "Soft")
        self.assertEqual(app.get_country("Spain").posture, "Hard")
        self.assertEqual(app.get_country("Scandinavia").posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Germany").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.get_country("Germany").plots = 1
        app.resolvePlot("Germany", 3, 4, [], ["Spain", "Scandinavia"], [5, 4], [])
        self.assertEqual(app.funding, 7)
        self.assertEqual(app.get_country("Germany").posture, "Soft")
        self.assertEqual(app.get_country("Spain").posture, "Hard")
        self.assertEqual(app.get_country("Scandinavia").posture, "Soft")
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Germany").plots, 0)

    def test_resolve_muslim_iran_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2])
        self.assertEqual(app.funding, 7)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iran").plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.get_country("Iran").is_fair())
        self.assertEqual(app.get_country("Iran").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iran").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.get_country("Iraq").troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.get_country("Iraq").troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3])
        self.assertEqual(app.funding, 6)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.get_country("Iraq").plots, 0)

    def test_resolve_us_plots(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").plots = 1
        app.get_country("United States").posture = "Hard"
        app.resolvePlot("United States", 1, 4, [1, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.get_country("United States").posture, "Soft")
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.get_country("United States").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").plots = 1
        app.get_country("United States").posture = "Soft"
        app.resolvePlot("United States", 2, 4, [5, 6, 1], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.get_country("United States").posture, "Soft")
        self.assertEqual(app.prestige, 8)
        self.assertEqual(app.get_country("United States").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").plots = 1
        app.get_country("United States").posture = "Soft"
        app.resolvePlot("United States", 3, 5, [5, 6, 4], [], [], [])
        self.assertEqual(app.funding, 9)
        self.assertEqual(app.get_country("United States").posture, "Hard")
        self.assertEqual(app.prestige, 11)
        self.assertEqual(app.get_country("United States").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.gameOver)
        app.get_country("United States").plots = 1
        app.get_country("United States").posture = "Soft"
        app.resolvePlot("United States", "WMD", 0, [], [], [], [])
        self.assertEqual(app.get_country("United States").plots, 0)
        self.assertTrue(app.gameOver)

    def test_resolve_muslim_iran_plots_with_backlash(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 1, 0, [], [], [], [3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 1)
        app.resolvePlot("Iraq", 1, 0, [], [], [], [2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 3)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 1, 2], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.get_country("Iraq").is_fair())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iran").plots = 1
        app.resolvePlot("Iran", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.get_country("Iran").is_fair())
        self.assertEqual(app.get_country("Iran").aid, 0)
        self.assertEqual(app.prestige, 7)
        self.assertEqual(app.get_country("Iran").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.get_country("Iraq").troopCubes = 1
        app.resolvePlot("Iraq", 3, 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 4)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 6)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 0
        app.get_country("Iraq").plots = 1
        app.get_country("Iraq").troopCubes = 1
        app.resolvePlot("Iraq", "WMD", 0, [], [], [], [3, 3, 3], True)
        self.assertEqual(app.funding, 1)
        self.assertTrue(app.get_country("Iraq").is_poor())
        self.assertEqual(app.get_country("Iraq").aid, 0)
        self.assertEqual(app.prestige, 1)
        self.assertEqual(app.get_country("Iraq").plots, 0)
