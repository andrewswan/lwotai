from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class TravelTest(LabyrinthTestCase):
    """Test Travel"""

    def test_travel_first_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Gulf States").besieged = 0
        app.get_country("Gulf States").aid = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Gulf States").aid = 0
        app.get_country("Gulf States").regimeChange = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Gulf States").make_islamist_rule()
        app.get_country("Afghanistan").make_poor()
        app.get_country("Afghanistan").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.get_country("Gulf States").make_poor()
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").aid = 1
        iraqCount = 0
        gulfCount = 0
        for i in range(100):
            dest = app.travel_destinations(1)
            if dest == ["Gulf States"]:
                gulfCount += 1
            elif dest == ["Iraq"]:
                iraqCount += 1
            self.assertTrue(dest == ["Gulf States"] or dest == ["Iraq"])
        self.assertTrue(iraqCount > 0)
        self.assertTrue(gulfCount > 0)

        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").aid = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Pakistan"])

    def test_travel_second_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("Afghanistan").make_poor()
        app.get_country("Afghanistan").troopCubes = 1
        app.get_country("Afghanistan").sleeperCells = 4
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Afghanistan"])

        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        dest = app.travel_destinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

    def test_travel_third_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("Jordan").make_fair()
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.get_country("Gulf States").make_fair()
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Gulf States").make_poor()
        app.get_country("Algeria/Tunisia").make_fair()
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Jordan"])

        app.get_country("Germany").sleeperCells = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Algeria/Tunisia"])

    def test_travel_fourth_box(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("United States").make_hard()

        app.get_country("Canada").make_hard()
        app.get_country("United Kingdom").make_hard()
        app.get_country("Serbia").make_hard()
        app.get_country("India").make_hard()
        app.get_country("Scandinavia").make_hard()
        app.get_country("Eastern Europe").make_hard()
        app.get_country("Benelux").make_hard()
        app.get_country("Germany").make_hard()
        app.get_country("France").make_hard()
        app.get_country("Italy").make_hard()
        app.get_country("Spain").make_hard()
        app.get_country("Russia").make_hard()
        app.get_country("Caucasus").make_hard()
        app.get_country("China").make_hard()
        app.get_country("Kenya/Tanzania").make_hard()
        app.get_country("Thailand").make_hard()
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Philippines"])

    def test_travel_multiple(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        dest = app.travel_destinations(3)

        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Afghanistan").make_poor()
        app.get_country("Afghanistan").troopCubes = 1
        app.get_country("Afghanistan").sleeperCells = 4
        dest = app.travel_destinations(2)
        self.assertEqual(dest, ["Gulf States", "Afghanistan"])

        app.get_country("Jordan").make_fair()
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.get_country("United States").make_hard()
        app.get_country("Canada").make_hard()
        app.get_country("United Kingdom").make_hard()
        app.get_country("Serbia").make_hard()
        app.get_country("India").make_hard()
        app.get_country("Scandinavia").make_hard()
        app.get_country("Eastern Europe").make_hard()
        app.get_country("Benelux").make_hard()
        app.get_country("Germany").make_hard()
        app.get_country("France").make_hard()
        app.get_country("Italy").make_hard()
        app.get_country("Spain").make_hard()
        app.get_country("Russia").make_hard()
        app.get_country("Caucasus").make_hard()
        app.get_country("China").make_hard()
        app.get_country("Kenya/Tanzania").make_hard()
        app.get_country("Thailand").make_hard()
        dest = app.travel_destinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.get_country("Gulf States").make_islamist_rule()
        dest = app.travel_destinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "Philippines"])

        app.get_country("Kenya/Tanzania").remove_posture()
        phCount = 0
        ktCount = 0
        for i in range(100):
            dest = app.travel_destinations(3)
            if dest == ["Afghanistan", "Jordan", "Philippines"]:
                phCount += 1
            elif dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"]:
                ktCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "Philippines"] or
                            dest == ["Afghanistan", "Jordan", "Kenya/Tanzania"])
        self.assertTrue(phCount > 0)
        self.assertTrue(ktCount > 0)

        app.get_country("United States").make_soft()
        app.get_country("China").make_soft()
        dest = app.travel_destinations(3)
        self.assertEqual(dest, ["Afghanistan", "Jordan", "China"])

        app.get_country("Benelux").make_soft()
        chinaCount = 0
        beneluxCount = 0
        for i in range(100):
            dest = app.travel_destinations(3)
            if dest == ["Afghanistan", "Jordan", "China"]:
                chinaCount += 1
            elif dest == ["Afghanistan", "Jordan", "Benelux"]:
                beneluxCount += 1
            self.assertTrue(dest == ["Afghanistan", "Jordan", "China"] or dest == ["Afghanistan", "Jordan", "Benelux"])
        self.assertTrue(chinaCount > 0)
        self.assertTrue(beneluxCount > 0)

    def test_travel_from(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

        app.get_country("Lebanon").make_fair()
        app.get_country("Lebanon").activeCells = 1
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Lebanon"])

        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").activeCells = 1
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

        app.get_country("Egypt").make_fair()
        app.get_country("Egypt").activeCells = 1
        app.get_country("Egypt").regimeChange = 1
        app.get_country("Egypt").troopCubes = 2
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.get_country("Egypt").activeCells = 3
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Egypt"])

        app.get_country("Yemen").make_islamist_rule()
        app.get_country("Yemen").activeCells = 3
        app.get_country("Yemen").troopCubes = 2
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Egypt"])
        sources = app.travel_sources(dest, 2)
        self.assertEqual(sources, ["Yemen"])

        #multi

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)

        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1

        app.get_country("Afghanistan").make_poor()
        app.get_country("Afghanistan").troopCubes = 1
        app.get_country("Afghanistan").sleeperCells = 4

        app.get_country("Jordan").make_fair()
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(3)
        self.assertEqual(dest, ["Gulf States", "Afghanistan", "Jordan"])

        app.get_country("Lebanon").make_fair()
        app.get_country("Lebanon").activeCells = 1

        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").activeCells = 1

        app.get_country("Egypt").make_fair()
        app.get_country("Egypt").regimeChange = 1
        app.get_country("Egypt").troopCubes = 2
        app.get_country("Egypt").activeCells = 3

        app.get_country("Yemen").make_islamist_rule()
        app.get_country("Yemen").activeCells = 4
        app.get_country("Yemen").troopCubes = 2
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Iraq"])

        app.get_country("Yemen").activeCells = 5
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Egypt"])

        app.get_country("Yemen").activeCells = 6
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Yemen", "Yemen"])

        app.get_country("Yemen").activeCells = 4
        sources = app.travel_sources(dest, 3)
        app.get_country("Egypt").activeCells = 4
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Egypt", "Egypt"])

        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").troopCubes = 2
        app.get_country("Iraq").activeCells = 4
        app.get_country("Egypt").activeCells = 0
        app.get_country("Egypt").sleeperCells = 4
        sources = app.travel_sources(dest, 3)
        self.assertEqual(sources, ["Yemen", "Iraq", "Iraq"])
