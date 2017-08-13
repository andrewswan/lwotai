from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class WOIRollModifiers(LabyrinthTestCase):
    """Test War of Ideas Roll Modifiers"""

    def test_prestige(self):
        """Prestige"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.prestige = 1
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 1)
        app.prestige = 2
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 1)
        app.prestige = 3
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 1)
        app.prestige = 4
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 2)
        app.prestige = 5
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 2)
        app.prestige = 6
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 2)
        app.prestige = 7
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.prestige = 8
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.prestige = 9
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.prestige = 10
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)
        app.prestige = 11
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)
        app.prestige = 12
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)

    def test_aid(self):
        """Aid"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.get_country("Gulf States").aid = 1
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)

    def test_to_good(self):
        """Going to Good"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.get_country("Gulf States").make_poor()
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)
        app.get_country("Gulf States").make_fair()
        app.get_country("Gulf States").make_neutral()
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)

    def test_gwot_penalty(self):
        """GWOT Penalty"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.get_country("United States").posture = "Soft"
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 2)
        app.get_country("Canada").posture = "Hard"
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 1)
        app.get_country("France").posture = "Hard"
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 0)
        app.get_country("Germany").posture = "Hard"
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 0)

    def test_adjacent_countries(self):
        """Adjacent countries Ally Good"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.get_country('Pakistan').make_good()
        app.get_country('Pakistan').make_neutral()
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 3)
        app.get_country('Pakistan').make_ally()
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)
        app.get_country('Iraq').make_good()
        app.get_country('Iraq').make_ally()
        self.assertEqual(app.modified_woi_roll(3, "Gulf States"), 4)