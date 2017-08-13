from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class PlacePlotsTest(LabyrinthTestCase):
    """Place Plots"""

    def test_place_plot(self):
        # no cells
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        unusedOps = app.execute_plot(2, False, [1, 2])
        self.assertEqual(unusedOps, 2)
        unusedOps = app.execute_plot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 3)

        # 1 cell in US
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 1
        unusedOps = app.execute_plot(1, True, [2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.get_country("United States").plots, 0)

        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 1)
        self.assertEqual(app.get_country("United States").plots, 1)

        # 2 cells in us
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 2
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.get_country("United States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 2
        unusedOps = app.execute_plot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.get_country("United States").plots, 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 2
        unusedOps = app.execute_plot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.get_country("United States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 2
        unusedOps = app.execute_plot(3, True, [1, 2, 3])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.get_country("United States").plots, 1)

        # 3 cells in us
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 3
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.get_country("United States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 3
        unusedOps = app.execute_plot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.get_country("United States").plots, 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 3
        unusedOps = app.execute_plot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.get_country("United States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 3
        unusedOps = app.execute_plot(2, True, [1, 2])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 2)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.get_country("United States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 3
        unusedOps = app.execute_plot(3, True, [1, 1, 3])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("United States").activeCells, 3)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.get_country("United States").plots, 2)

        # Low prestige, no GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 1)
        self.assertEqual(app.get_country("Israel").sleeperCells, 0)
        self.assertEqual(app.get_country("Israel").plots, 1)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        unusedOps = app.execute_plot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 1)
        self.assertEqual(app.get_country("Israel").sleeperCells, 0)
        self.assertEqual(app.get_country("Israel").plots, 1)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").activeCells, 1)
        self.assertEqual(app.get_country("Iraq").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.get_country("Israel").sleeperCells = 1
        app.get_country("United States").posture = "Soft"
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 0)
        self.assertEqual(app.get_country("Israel").sleeperCells, 1)
        self.assertEqual(app.get_country("Israel").plots, 0)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").activeCells, 1)
        self.assertEqual(app.get_country("Iraq").plots, 1)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 0)
        self.assertEqual(app.get_country("Israel").sleeperCells, 1)
        self.assertEqual(app.get_country("Israel").plots, 0)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").plots, 1)

        # Funding section
        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 9
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 0
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 1)
        self.assertEqual(app.get_country("Israel").activeCells, 0)
        self.assertEqual(app.get_country("Israel").sleeperCells, 1)
        self.assertEqual(app.get_country("Israel").plots, 0)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 0
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 0
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 1)
        self.assertEqual(app.get_country("Israel").sleeperCells, 0)
        self.assertEqual(app.get_country("Israel").plots, 1)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 0
        unusedOps = app.execute_plot(2, True, [1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 1)
        self.assertEqual(app.get_country("Israel").sleeperCells, 0)
        self.assertEqual(app.get_country("Israel").plots, 1)
        self.assertEqual(app.get_country("Canada").plots, 1)
        self.assertEqual(app.get_country("Iraq").plots, 0)

        # Low prestige, yes GWOT penalty
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.funding = 8
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 0
        unusedOps = app.execute_plot(3, True, [1, 1, 1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 1)
        self.assertEqual(app.get_country("Israel").sleeperCells, 0)
        self.assertEqual(app.get_country("Israel").plots, 1)
        self.assertEqual(app.get_country("Canada").plots, 1)
        self.assertEqual(app.get_country("Iraq").plots, 1)

        # High prestige
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 4
        app.markers = ["Abu Sayyaf"]
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        app.get_country("Iraq").troopCubes = 1
        app.get_country("Philippines").sleeperCells = 1
        app.get_country("Philippines").troopCubes = 1
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Israel").activeCells, 0)
        self.assertEqual(app.get_country("Israel").sleeperCells, 1)
        self.assertEqual(app.get_country("Israel").plots, 0)
        self.assertEqual(app.get_country("Canada").plots, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)
        self.assertEqual(app.get_country("Philippines").activeCells, 1)
        self.assertEqual(app.get_country("Philippines").sleeperCells, 0)
        self.assertEqual(app.get_country("Philippines").plots, 1)

        # priorities box
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.get_country("Israel").sleeperCells = 0
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Spain").sleeperCells = 0
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").sleeperCells = 1
        app.get_country("Gulf States").aid = 1
        unusedOps = app.execute_plot(1, True, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Iraq").plots, 0)
        self.assertEqual(app.get_country("Gulf States").plots, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 3
        app.get_country("Israel").sleeperCells = 0
        app.get_country("Canada").posture = "Soft"
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Spain").posture = "Soft"
        app.get_country("Spain").sleeperCells = 0
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Iraq").aid = 1
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").sleeperCells = 1
        app.get_country("Gulf States").aid = 1
        unusedOps = app.execute_plot(1, False, [1])
        self.assertEqual(unusedOps, 0)
        self.assertEqual(app.get_country("Iraq").plots, 1)
        self.assertEqual(app.get_country("Gulf States").plots, 0)
