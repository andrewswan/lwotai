from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class SummaryTest(LabyrinthTestCase):
    """Test the get_summary() method"""

    def test_summary(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)

        # Invoke
        summary = app.get_summary()

        # Assert
        self.assertEqual(summary, [
            'Jihadist Ideology: Normal',
            '',
            'VICTORY',
            'Good Resources: 0        Islamist Resources: 1',
            'Fair/Good Countries: 3   Poor/Islamist Countries: 4',
            '',
            'GWOT',
            'US Posture: Hard    World Posture: Hard 1',
            'US Prestige: 7',
            '',
            'TROOPS',
            'War: 9 troops available',
            '',
            'JIHADIST FUNDING',
            'Funding: 5    Cells Available: 11',
            '',
            'EVENTS',
            'Markers: None',
            'Lapsing: None'
        ])
