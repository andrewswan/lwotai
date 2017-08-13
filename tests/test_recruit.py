from lwotai.labyrinth import Labyrinth
from labyrinth_test_case import LabyrinthTestCase


class RecruitTest(LabyrinthTestCase):
    """Test Recruiting"""

    def test_recruit_choice(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.recruitChoice(3))
        app.get_country("Gulf States").make_good()
        app.get_country("Gulf States").activeCells = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").cadre = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.get_country("Gulf States").activeCells = 1
        app.get_country("Gulf States").cadre = 0
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").activeCells = 1
        for i in range(10):
            ret_val = app.recruitChoice(i)
            self.assertTrue(ret_val in ["Iraq", "Gulf States"])
        app.get_country("Iraq").activeCells = 0
        app.get_country("Iraq").cadre = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.get_country("Iraq").troopCubes = 2
        self.assertEqual(app.recruitChoice(1), "Iraq")
        app.get_country("Gulf States").besieged = 1
        self.assertEqual(app.recruitChoice(1), "Gulf States")
        app.get_country("Russia").sleeperCells = 1
        self.assertEqual(app.recruitChoice(1), "Russia")
        app.get_country("Philippines").sleeperCells = 1
        self.assertEqual(app.recruitChoice(1), "Philippines")
        app.get_country("Iraq").make_islamist_rule()
        app.get_country("Iraq").activeCells = 6
        self.assertEqual(app.recruitChoice(1), "Philippines")
        app.get_country("Iraq").activeCells = 5
        self.assertEqual(app.recruitChoice(3), "Iraq")
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").activeCells = 1
        app.get_country("Gulf States").troopCubes = 5
        self.assertEqual(app.recruitChoice(3), "Iraq")
        app.get_country("Gulf States").troopCubes = 6
        self.assertEqual(app.recruitChoice(1), "Gulf States")

    def test_execute_recruit(self):
        # Normal
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)    # Coherent
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 1, [1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 1, [2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 2, [2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 12)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 13)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [2, 1, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 15
        unused_ops = app.executeRecruit("United States", 3, [2, 2, 2])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        # not enough cells
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 3, [2, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 3, [1, 2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 3, [1, 1, 2])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 1
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 1)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 2
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 0)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 1)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 3
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [2, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 1)
        self.assertEqual(app.cells, 4)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 2, [1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 2)
        self.assertEqual(app.cells, 3)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 5
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 2)

        app = Labyrinth(1, 2, self.set_up_blank_test_scenario)
        app.cells = 4
        app.funding = 9
        unused_ops = app.executeRecruit("United States", 3, [1, 1, 1])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("United States").sleeperCells, 3)
        self.assertEqual(app.cells, 1)

        # IR RC
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_poor()
        unused_ops = app.executeRecruit("Iraq", 1, [4])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 0)
        self.assertEqual(app.cells, 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_islamist_rule()
        unused_ops = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.cells, 14)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 15
        app.funding = 9
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").regimeChange = 1
        unused_ops = app.executeRecruit("Iraq", 1, [6])
        self.assertEqual(unused_ops, 0)
        self.assertEqual(app.get_country("Iraq").sleeperCells, 1)
        self.assertEqual(app.cells, 14)
