from lwotai.countries.country import Country

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

    def test_get_good_resources(self):
        # Set up
        game_map = self.create_test_map()
        game_map.get("Gulf States").make_good()

        # Invoke
        good_resources = game_map.get_good_resources()

        # Assert
        self.assertEqual(3, good_resources)

    def test_get_islamist_rule_resources(self):
        # Set up
        game_map = self.create_test_map()
        game_map.get("Gulf States").make_islamist_rule()

        # Invoke
        islamist_rule_resources = game_map.get_islamist_rule_resources()

        # Assert
        self.assertEqual(3, islamist_rule_resources)

    def test_get_net_hard_countries_when_more_are_hard(self):
        # Set up
        game_map = self.create_test_map()
        game_map.get("France").make_soft()

        # Invoke
        net_hard_countries = game_map.get_net_hard_countries()

        # Assert
        self.assertEqual(0, net_hard_countries)  # Israel is hard

    def test_get_net_hard_countries_when_more_are_soft(self):
        # Set up
        game_map = self.create_test_map()
        for country_name in ["Benelux", "Canada", "China", "France", "Germany", "India", "Russia", "Scandinavia"]:
            game_map.get(country_name).make_soft()

        # Invoke
        net_hard_countries = game_map.get_net_hard_countries()

        # Assert
        self.assertEqual(-3, net_hard_countries)  # should max out at -3

    def test_get_net_hard_countries_when_more_are_hard(self):
        # Set up
        game_map = self.create_test_map()
        for country_name in ["Benelux", "Canada", "China", "France", "Germany", "India", "Russia", "Scandinavia"]:
            game_map.get(country_name).make_hard()

        # Invoke
        net_hard_countries = game_map.get_net_hard_countries()

        # Assert
        self.assertEqual(3, net_hard_countries)  # should be capped at 3

    def test_getting_invalid_country_name_returns_none(self):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        country = game_map.get("gdjgjhghjsdgjf")

        # Assert
        self.assertEqual(None, country)

    def test_us_links_to_schengen_area(self):
        # Set up
        game_map = self.create_test_map()
        us = game_map.get("United States")

        # Invoke
        schengen_link = us.schengenLink

        # Check
        self.assertTrue(schengen_link)

    def test_pick_random_shia_mix_country(self):
        self._assert_random_shia_mix_country("Turkey", [1, 1, 1])
        self._assert_random_shia_mix_country("Turkey", [1, 2, 1])
        self._assert_random_shia_mix_country("Saudi Arabia", [1, 2, 2])
        self._assert_random_shia_mix_country("Saudi Arabia", [3, 2, 1])
        self._assert_random_shia_mix_country("Lebanon", [3, 2, 2])
        self._assert_random_shia_mix_country("Lebanon", [4, 1, 3])
        self._assert_random_shia_mix_country("Yemen", [4, 2, 3])
        self._assert_random_shia_mix_country("Yemen", [6, 1, 3])
        self._assert_random_shia_mix_country("Iraq", [5, 3, 3])
        self._assert_random_shia_mix_country("Iraq", [5, 3, 4])
        self._assert_random_shia_mix_country("Pakistan", [6, 3, 4])
        self._assert_random_shia_mix_country("Pakistan", [6, 2, 6])
        self._assert_random_shia_mix_country("Gulf States", [6, 3, 6])
        self._assert_random_shia_mix_country("Gulf States", [6, 5, 5])
        self._assert_random_shia_mix_country("Afghanistan", [6, 5, 6])
        self._assert_random_shia_mix_country("Afghanistan", [6, 6, 6])

    def _assert_random_shia_mix_country(self, expected_name, rolls):
        # Set up
        game_map = self.create_test_map()

        # Invoke
        country = game_map.look_up_shia_mix_country(rolls)

        # Check
        self.assertIsInstance(country, str)
        self.assertEqual(expected_name, country)
