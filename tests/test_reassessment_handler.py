from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth
from postures.posture import HARD, SOFT


class ReassessmentHandlerTest(LabyrinthTestCase):

    def test_reassessment(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.us_posture(), HARD)
        app.toggle_us_posture()
        self.assertEqual(app.us_posture(), SOFT)
        app.toggle_us_posture()
        self.assertEqual(app.us_posture(), HARD)
