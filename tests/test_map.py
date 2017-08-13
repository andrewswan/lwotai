from labyrinth_test_case import LabyrinthTestCase
from lwotai.map import Map


class MapTest(LabyrinthTestCase):

    @staticmethod
    def create_test_map():
        return Map(None)

    def test_all_links_are_reciprocal(self):
        game_map = self.create_test_map()
        for country in game_map.countries():
            for linked_country in country.links:
                self.assertTrue(country in linked_country.links,
                                "%s is not in the links of %s" % (country, linked_country))

    def test_country_names(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        country_names = game_map.country_names()

        # Assert
        self.assertEqual(38, len(country_names))
        self.assertTrue("France" in country_names)

    def test_find_by_partial_miscased_name(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        country_names = game_map.find_by_name("f stat")

        # Assert
        self.assertEqual(["Gulf States"], country_names)

    def test_find_by_false_predicate(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        unlinked_countries = game_map.find(lambda c: not c.schengen and not c.links)

        # Assert
        self.assertEqual([], unlinked_countries, "Found %s" % unlinked_countries)

    def test_find_by_partially_true_predicate(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        u_countries = game_map.find(lambda c: c.name.startswith("U"))

        # Assert
        u_country_names = [country.name for country in u_countries]
        self.assertEqual(["United States", "United Kingdom"], u_country_names)

    def test_links_from_afghanistan(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        links = game_map.get("Afghanistan").links

        # Assert
        link_names = [c.name for c in links]
        expected_link_names = ["Central Asia", "Iran", "Pakistan"]
        self.assertEqual(expected_link_names, link_names)
