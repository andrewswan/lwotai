from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class HandleJihadTest(LabyrinthTestCase):
    """Test handleJihad"""

    def test_handle_jihad(self):
        # Many Cells
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 5
        app.get_country("Gulf States").activeCells = 4
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 1)
        self.assertEqual(ops_left, 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 5
        app.get_country("Gulf States").activeCells = 4
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 2)
        self.assertEqual(ops_left, 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 5
        app.get_country("Gulf States").activeCells = 4
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 3)
        self.assertEqual(ops_left, 0)

        # 1 cell
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 1
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 1)
        self.assertEqual(ops_left, 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 1
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 2)
        self.assertEqual(ops_left, 1)
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 1
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 3)
        self.assertEqual(ops_left, 2)

        # 2 cell
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 1)
        self.assertEqual(ops_left, 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 2)
        self.assertEqual(ops_left, 0)
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 3)
        self.assertEqual(ops_left, 1)

        # 3 cell
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 1
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 1)
        self.assertEqual(ops_left, 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 1
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 2)
        self.assertEqual(ops_left, 0)
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.get_country("Gulf States").make_neutral()
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").sleeperCells = 1
        app.get_country("Gulf States").activeCells = 2
        app.get_country("Gulf States").troopCubes = 4
        app.get_country("Gulf States").remove_besieged()
        app.get_country("Gulf States").regimeChange = 1
        app.get_country("Gulf States").aid = 1
        ops_left = app.handle_jihad("Gulf States", 3)
        self.assertEqual(ops_left, 0)
