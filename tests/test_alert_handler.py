from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class AlertHandlerTest(LabyrinthTestCase):
    """Test Alert"""

    def test_alert_reduces_plot_count_by_one(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.map.get("Iraq")
        self.assertEqual(iraq.plots, 2)
        app.alert_plot("Iraq")
        self.assertEqual(iraq.plots, 1)
        app.alert_plot("Iraq")
        self.assertEqual(iraq.plots, 0)
        with self.assertRaises(AssertionError):
            app.alert_plot("Iraq")
