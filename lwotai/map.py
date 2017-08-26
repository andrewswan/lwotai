from lwotai.countries.iran import Iran
from lwotai.countries.muslim import MuslimCountry
from lwotai.countries.non_muslim import NonMuslimCountry
from lwotai.countries.types import SHIA_MIX, SUNNI
from lwotai.governance import GOOD, FAIR
from lwotai.postures.posture import HARD


def _get_countries(app):
    """Returns the countries to add to the map"""
    return [
        # Iran
        Iran(app),
        # Non-Muslim
        NonMuslimCountry(app, "Benelux",        None, GOOD, True),
        NonMuslimCountry(app, "Canada",         None, GOOD, False, schengen_link=True),
        NonMuslimCountry(app, "Caucasus",       None, FAIR, False),
        NonMuslimCountry(app, "China",          None, FAIR, False),
        NonMuslimCountry(app, "Eastern Europe", None, GOOD, True),
        NonMuslimCountry(app, "France",         None, GOOD, True,  2),
        NonMuslimCountry(app, "Germany",        None, GOOD, True),
        NonMuslimCountry(app, "India",          None, GOOD, False),
        NonMuslimCountry(app, "Israel",         HARD, GOOD, False),
        NonMuslimCountry(app, "Italy",          None, GOOD, True),
        NonMuslimCountry(app, "Kenya/Tanzania", None, FAIR, False),
        NonMuslimCountry(app, "Philippines",    None, FAIR, False, 3),
        NonMuslimCountry(app, "Russia",         None, FAIR, False, schengen_link=True),
        NonMuslimCountry(app, "Scandinavia",    None, GOOD, True),
        NonMuslimCountry(app, "Serbia",         None, GOOD, False, schengen_link=True),
        NonMuslimCountry(app, "Spain",          None, GOOD, True,  2),
        NonMuslimCountry(app, "Thailand",       None, FAIR, False),
        NonMuslimCountry(app, "United Kingdom", None, GOOD, False, 3, schengen_link=True),
        NonMuslimCountry(app, "United States",  HARD, GOOD, False, schengen_link=True),
        # Shia-Mix
        MuslimCountry(app, "Afghanistan",        SHIA_MIX, False, 1),
        MuslimCountry(app, "Gulf States",        SHIA_MIX, True, 3),
        MuslimCountry(app, "Iraq",               SHIA_MIX, True, 3),
        MuslimCountry(app, "Lebanon",            SHIA_MIX, False, 1, schengen_link=True),
        MuslimCountry(app, "Pakistan",           SHIA_MIX, False, 2),
        MuslimCountry(app, "Saudi Arabia",       SHIA_MIX, True, 3),
        MuslimCountry(app, "Turkey",             SHIA_MIX, False, 2, schengen_link=True),
        MuslimCountry(app, "Yemen",              SHIA_MIX, False, 1),
        # Sunni
        MuslimCountry(app, "Algeria/Tunisia",    SUNNI, True, 2, schengen_link=True),
        MuslimCountry(app, "Central Asia",       SUNNI, False, 2),
        MuslimCountry(app, "Egypt",              SUNNI, False, 3),
        MuslimCountry(app, "Indonesia/Malaysia", SUNNI, True, 3),
        MuslimCountry(app, "Jordan",             SUNNI, False, 1),
        MuslimCountry(app, "Libya",              SUNNI, True, 1, schengen_link=True),
        MuslimCountry(app, "Morocco",            SUNNI, False, 2, schengen_link=True),
        MuslimCountry(app, "Somalia",            SUNNI, False, 1),
        MuslimCountry(app, "Sudan",              SUNNI, True, 1),
        MuslimCountry(app, "Syria",              SUNNI, False, 2)
    ]


class Map(object):
    """The board map, i.e. the countries and the links between them"""

    def __init__(self, app):
        self._map = {}
        for country in _get_countries(app):
            self._map[country.name] = country

        self._link_country("Afghanistan", "Central Asia", "Iran", "Pakistan")
        self._link_country("Algeria/Tunisia", "Libya", "Morocco")
        self._link_country("Canada", "United Kingdom", "United States")
        self._link_country("Caucasus", "Central Asia", "Iran", "Russia", "Turkey")
        self._link_country("Central Asia", "Afghanistan", "Caucasus", "China", "Iran", "Russia")
        self._link_country("China", "Central Asia", "Thailand")
        self._link_country("Egypt", "Israel", "Libya", "Sudan")
        self._link_country("Gulf States", "Iran", "Iraq", "Pakistan", "Saudi Arabia")
        self._link_country("India", "Indonesia/Malaysia", "Pakistan")
        self._link_country("Indonesia/Malaysia", "India", "Pakistan", "Philippines", "Thailand")
        self._link_country("Iran", "Afghanistan", "Caucasus", "Central Asia", "Gulf States", "Iraq", "Pakistan",
                           "Turkey")
        self._link_country("Iraq", "Gulf States", "Iran", "Jordan", "Saudi Arabia", "Syria", "Turkey")
        self._link_country("Israel", "Egypt", "Jordan", "Lebanon")
        self._link_country("Jordan", "Iraq", "Israel", "Saudi Arabia", "Syria")
        self._link_country("Kenya/Tanzania", "Somalia", "Sudan")
        self._link_country("Lebanon", "Israel", "Syria")
        self._link_country("Libya", "Algeria/Tunisia", "Egypt", "Sudan")
        self._link_country("Morocco", "Algeria/Tunisia")
        self._link_country("Pakistan", "Afghanistan", "Gulf States", "India", "Indonesia/Malaysia", "Iran")
        self._link_country("Philippines", "Indonesia/Malaysia", "Thailand", "United States")
        self._link_country("Russia", "Caucasus", "Central Asia", "Serbia", "Turkey")
        self._link_country("Saudi Arabia", "Gulf States", "Iraq", "Jordan", "Yemen")
        self._link_country("Serbia", "Russia", "Turkey")
        self._link_country("Somalia", "Kenya/Tanzania", "Sudan", "Yemen")
        self._link_country("Sudan", "Egypt", "Kenya/Tanzania", "Libya", "Somalia")
        self._link_country("Syria", "Iraq", "Jordan", "Lebanon", "Turkey")
        self._link_country("Thailand", "China", "Indonesia/Malaysia", "Philippines")
        self._link_country("Turkey", "Caucasus", "Iran", "Iraq", "Russia", "Serbia", "Syria")
        self._link_country("United Kingdom", "Canada", "United States")
        self._link_country("United States", "Canada", "Philippines", "United Kingdom")
        self._link_country("Yemen", "Saudi Arabia", "Somalia")
        self._shia_mix_table = self._get_shia_mix_table()

    def _link_country(self, country, *other_countries):
        """Links the first named country to the other named countries"""
        for other_country in other_countries:
            self._map[country].links.append(self._map[other_country])

    def country_names(self):
        """Returns the names of all countries on this map"""
        return self._map.keys()

    def find(self, predicate):
        """Returns the Countries matching the given predicate"""
        return [country for country in self._map.values() if predicate(country)]

    def find_by_name(self, partial_name):
        """Returns a list of country_names containing the given partial name, case-insensitively"""
        return [country_name for country_name in self._map if partial_name.lower() in country_name.lower()]

    def get(self, country_name):
        """Returns the Country with the given name, or None if it doesn't exist"""
        try:
            return self._map[country_name]
        except KeyError:
            return None

    def countries(self):
        """Returns all Countries on the map"""
        return self._map.values()

    def count_countries(self, predicate):
        """Returns the number of countries that match the given predicate"""
        return len(self.find(predicate))

    def contains(self, predicate):
        """Indicates whether the map contains any countries matching the given predicate"""
        return self.count_countries(predicate) > 0

    def _get_resources(self, predicate):
        return sum([c.resources for c in self.find(predicate)])

    def get_good_resources(self):
        """Returns the total number of resources controlled by Good governance countries"""
        return self._get_resources(lambda c: c.is_good())

    def get_islamist_rule_resources(self):
        """Returns the total number of resources controlled by Good governance countries"""
        return self._get_resources(lambda c: c.is_islamist_rule())

    def get_net_hard_countries(self):
        """Returns the net amount of hard countries in the world (exc. USA); a negative number means more are soft"""
        net_hard_countries = 0
        for country in self.countries():
            if country.name != "United States":
                if country.is_hard():
                    net_hard_countries += 1
                elif country.is_soft():
                    net_hard_countries -= 1
        return max(-3, min(net_hard_countries, 3))

    def look_up_shia_mix_country(self, rolls):
        """Choose a country from the AI's Shia-Mix table, using the given rolls"""
        assert len(rolls) == 3, "Expected 3 rolls but got %s" % rolls
        return self._shia_mix_table[sum(rolls)]

    @staticmethod
    def _get_shia_mix_table():
        return {
            3: "Turkey",
            4: "Turkey",
            5: "Saudi Arabia",
            6: "Saudi Arabia",
            7: "Lebanon",
            8: "Lebanon",
            9: "Yemen",
            10: "Yemen",
            11: "Iraq",
            12: "Iraq",
            13: "Pakistan",
            14: "Pakistan",
            15: "Gulf States",
            16: "Gulf States",
            17: "Afghanistan",
            18: "Afghanistan"
        }
