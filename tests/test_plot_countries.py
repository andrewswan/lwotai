from lwotai.labyrinth import Labyrinth

from labyrinth_test_case import LabyrinthTestCase


class PlotCountriesTest(LabyrinthTestCase):

    def test_no_countries_have_plots_at_first(self):
        # Set up
        app = Labyrinth(1, 1)

        # Invoke
        plot_countries = app.get_plot_countries()

        # Check
        self.assertEqual([], plot_countries)

    def test_two_countries_have_plots(self):
        # Set up
        app = Labyrinth(1, 1)
        actual_plot_countries = ["China", "Italy"]
        for country_name in actual_plot_countries:
            app.get_country(country_name).plots = 2

        # Invoke
        plot_countries = [c.name for c in app.get_plot_countries()]

        # Check
        plot_countries.sort()
        self.assertEqual(actual_plot_countries, plot_countries)
