from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class MinorJihadChoiceTest(LabyrinthTestCase):
    """Test minorJihadInGoodFairChoice"""

    def test_minor_jihad_one_cell_one_ops(self):
        # one cell in each country, one ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            ret_val = app.minor_jihad_in_good_fair_choice(1)
            self.assertTrue((ret_val == [("Gulf States", 1)]) or (ret_val == [("Saudi Arabia", 1)]))
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Jordan", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])

    def test_minor_jihad_one_cell_two_ops(self):
        # one cell in each country, two ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 1)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Saudi Arabia", 1), ("Gulf States", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        retVal = app.minor_jihad_in_good_fair_choice(2)
        self.assertTrue((("Gulf States", 1) in retVal) and (("Saudi Arabia", 1) in retVal) and len(retVal) == 2)
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 1), ("Jordan", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Jordan", 1), ("Gulf States", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 1), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Pakistan", 1), ("Gulf States", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 1), ("Jordan", 1)])

    def test_minor_jihad_one_cell_three_ops(self):
        # one cell in each country, three ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 1)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Saudi Arabia", 1), ("Gulf States", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        self.assertTrue((("Gulf States", 1) in app.minor_jihad_in_good_fair_choice(3)) and
                        (("Saudi Arabia", 1) in app.minor_jihad_in_good_fair_choice(3))
                        and len(app.minor_jihad_in_good_fair_choice(3)) == 2)
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 1), ("Jordan", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Jordan", 1), ("Gulf States", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 1), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Pakistan", 1), ("Gulf States", 1), ("Jordan", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 1), ("Jordan", 1), ("Pakistan", 1)])

    def test_minor_jihad_two_cell_one_ops(self):
        # two cells in each country, one ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            retVal = app.minor_jihad_in_good_fair_choice(1)
            self.assertTrue(retVal == [("Gulf States", 1)] or retVal == [("Saudi Arabia", 1)])
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Jordan", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])

    def test_minor_jihad_two_cell_two_ops(self):
        # two cell in each country, two ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Saudi Arabia", 2)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            retVal = app.minor_jihad_in_good_fair_choice(2)
            self.assertTrue(retVal == [("Gulf States", 2)] or retVal == [("Saudi Arabia", 2)])
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Jordan", 2)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Pakistan", 2)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])

    def test_minor_jihad_two_cell_three_ops(self):
        # two cell in each country, three ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 2)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Saudi Arabia", 2), ("Gulf States", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            retVal = app.minor_jihad_in_good_fair_choice(3)
            self.assertTrue(retVal == [("Saudi Arabia", 2), ("Gulf States", 1)] or
                            retVal == [("Gulf States", 2), ("Saudi Arabia", 1)])
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 2), ("Jordan", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Jordan", 2), ("Gulf States", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 2), ("Jordan", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 2
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Pakistan", 2), ("Gulf States", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 2), ("Jordan", 1)])

    def test_minor_jihad_three_cell_one_ops(self):
        # three cells in each country, one ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Saudi Arabia", 1)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        self.assertTrue(app.minor_jihad_in_good_fair_choice(1) in [[("Gulf States", 1)], [("Saudi Arabia", 1)]])
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Jordan", 1)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Pakistan", 1)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Gulf States", 1)])

    def test_minor_jihad_three_cell_two_ops(self):
        # three cell in each country, two ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Saudi Arabia", 2)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            retVal = app.minor_jihad_in_good_fair_choice(2)
            self.assertTrue(retVal == [("Gulf States", 2)] or retVal == [("Saudi Arabia", 2)])
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Jordan", 2)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Pakistan", 2)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(2), [("Gulf States", 2)])

    def test_minor_jihad_three_cell_three_ops(self):
        # three cell in each country, three ops case

        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        # only Islamist rule has cells
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), False)
        # fair governance
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 3)])
        # good governance
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Saudi Arabia", 3)])
        # 2 good governance
        app.get_country("Gulf States").make_good()
        for i in range(10):
            retVal = app.minor_jihad_in_good_fair_choice(3)
            self.assertTrue((retVal == [("Saudi Arabia", 3)]) or (retVal == [("Gulf States", 3)]))
        # 2 good governance but Jordan has less resources    
        app.get_country("Saudi Arabia").make_poor()
        app.get_country("Jordan").make_good()
        app.get_country("Jordan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 3)])
        # but the other is besieged
        app.get_country("Jordan").make_besieged()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Jordan", 3)])
        # but the other has aid
        app.get_country("Gulf States").set_aid(1)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 3)])
        # but yet another is Pakistan    
        app.get_country("Pakistan").make_good()
        app.get_country("Pakistan").activeCells = 3
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Pakistan", 3)])
        # but Pakistan does not win against good if it is fair
        app.get_country("Pakistan").make_fair()
        self.assertEqual(app.minor_jihad_in_good_fair_choice(3), [("Gulf States", 3)])
