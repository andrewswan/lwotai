from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class IsAdjacent(LabyrinthTestCase):
    """Test isAdjacent"""

    def test_is_adjacent(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.is_adjacent("Iran", "Iraq"))
        self.assertTrue(app.is_adjacent("Germany", "Spain"))
        self.assertTrue(app.is_adjacent("Libya", "Italy"))
        self.assertTrue(app.is_adjacent("Benelux", "Russia"))
        self.assertTrue(app.is_adjacent("Lebanon", "France"))
        self.assertFalse(app.is_adjacent("United States", "Lebanon"))