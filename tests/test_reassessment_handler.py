from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class ReassessmentHandlerTest(LabyrinthTestCase):

    def test_reassessment(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        self.assertEqual(app.map["United States"].posture, "Hard")
        app.toggle_us_posture()
        self.assertEqual(app.map["United States"].posture, "Soft")
        app.toggle_us_posture()
        self.assertEqual(app.map["United States"].posture, "Hard")