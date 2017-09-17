from labyrinth_test_case import LabyrinthTestCase
from lwotai.ai import AIPlayer
from lwotai.labyrinth import Labyrinth


class AIPlayerTest(LabyrinthTestCase):

    app = Labyrinth(1, 1, LabyrinthTestCase.set_up_blank_test_scenario)
    ai = AIPlayer(app)

    def test_recruit_choice(self):
        self.assertFalse(self.ai._recruit_choice(3))
        self.app.get_country("Gulf States").make_good()
        self.app.get_country("Gulf States").activeCells = 1
        self._assert_recruit(1, "Gulf States")
        self.app.get_country("Gulf States").activeCells = 0
        self.app.get_country("Gulf States").cadre = 1
        self._assert_recruit(1, "Gulf States")
        self.app.get_country("Gulf States").activeCells = 1
        self.app.get_country("Gulf States").cadre = 0
        self.app.get_country("Iraq").make_good()
        self.app.get_country("Iraq").activeCells = 1
        for i in range(10):
            ret_val = self.ai._recruit_choice(i)
            self.assertTrue(ret_val in ["Iraq", "Gulf States"])
        self.app.get_country("Iraq").activeCells = 0
        self.app.get_country("Iraq").cadre = 1
        self._assert_recruit(1, "Gulf States")
        self.app.get_country("Iraq").troopCubes = 2
        self._assert_recruit(1, "Iraq")
        self.app.get_country("Gulf States").make_besieged()
        self._assert_recruit(1, "Gulf States")
        self.app.get_country("Russia").sleeperCells = 1
        self._assert_recruit(1, "Russia")
        self.app.get_country("Philippines").sleeperCells = 1
        self._assert_recruit(1, "Philippines")
        self.app.get_country("Iraq").make_islamist_rule()
        self.app.get_country("Iraq").activeCells = 6
        self._assert_recruit(1, "Philippines")
        self.app.get_country("Iraq").activeCells = 5
        self._assert_recruit(3, "Iraq")
        self.app.get_country("Gulf States").make_regime_change()
        self.app.get_country("Gulf States").activeCells = 1
        self.app.get_country("Gulf States").troopCubes = 5
        self._assert_recruit(3, "Iraq")
        self.app.get_country("Gulf States").troopCubes = 6
        self._assert_recruit(1, "Gulf States")

    def _assert_recruit(self, ops, country_name):
        self.assertEqual(self.ai._recruit_choice(ops), country_name)
