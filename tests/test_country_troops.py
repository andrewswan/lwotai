from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class CountryTroops(LabyrinthTestCase):
    """Test countryResources"""

    def test_country_without_nato_has_no_extra_troops(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = app.get_country("Iran")
        iran.change_troops(2)

        # Invoke
        troops = iran.troops()

        # Check
        self.assertEqual(2, troops)

    def test_country_with_nato_has_two_extra_troops(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iran = app.get_country("Iran")
        iran.change_troops(2)
        iran.markers.append("NATO")

        # Invoke
        troops = iran.troops()

        # Check
        self.assertEqual(4, troops)
