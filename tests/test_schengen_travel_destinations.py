from mockito import when, mock

from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth
from lwotai.postures.posture import HARD
from lwotai.randomizer import Randomizer


class TravelDestinationsForSchengenVisasTest(LabyrinthTestCase):

    def test_us_hard_and_one_unmarked_schengen(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.set_posture("United States", HARD)
        schengen_countries = self.schengen_countries(app)
        for schengen_country in schengen_countries[1:]:
            schengen_country.make_soft()
        unmarked_country = schengen_countries[0]
        unmarked_country.remove_posture()

        # Invoke
        destinations = app.travel_destinations_schengen_visas()

        # Check
        expected_country = unmarked_country.name
        self.assertEqual(destinations, [expected_country, expected_country])

    def test_us_hard_and_multiple_unmarked_schengens(self):
        # Set up
        mock_randomizer = mock(Randomizer())
        app = Labyrinth(1, 1, self.set_up_test_scenario, randomizer=mock_randomizer)
        schengen_countries = self.schengen_countries(app)
        schengen_country_names = [country.name for country in schengen_countries]
        chosen_countries = ['c1', 'c2']
        when(mock_randomizer).pick(2, schengen_country_names).thenReturn(chosen_countries)
        app.set_posture("United States", HARD)
        for country in schengen_countries:
            country.remove_posture()

        # Invoke
        destinations = app.travel_destinations_schengen_visas()

        # Check
        self.assertEqual(destinations, chosen_countries)
