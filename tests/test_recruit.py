from lwotai.labyrinth import Labyrinth
from labyrinth_test_case import LabyrinthTestCase


class RecruitTest(LabyrinthTestCase):
    """Test Recruiting"""

    def test_execute_recruit(self):
        # Normal
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 1, [1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 1, [2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [2, 1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [2, 2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)    # Coherent
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 1, [1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 1, [2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 2, [2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [2, 1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.execute_recruit("United States", 3, [2, 2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        # not enough cells
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 3, [2, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 3, [1, 1, 2])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 4)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 3)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 4
        app.funding = 9
        unused_ops = app.execute_recruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 1)

        # IR RC
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_poor()
        unused_ops = app.execute_recruit("Iraq", 1, [4])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_islamist_rule()
        unused_ops = app.execute_recruit("Iraq", 1, [6])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_regime_change()
        unused_ops = app.execute_recruit("Iraq", 1, [6])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.cells, 14)
