from lwotai.countries.country import Country
from lwotai.countries.iran import Iran
from lwotai.governance import GOOD, FAIR
from postures.posture import HARD


def _get_countries(app):
    """Returns the countries to add to the map"""
    return [
        Country(app, "Algeria/Tunisia", "Suni", None, None, False, 0, True, 2, schengen_link=True),
        Country(app, "Afghanistan", "Shia-Mix", None, None, False, 0, False, 1),
        Country(app, "Benelux", "Non-Muslim", None, GOOD, True, 0, False, 0),
        Country(app, "Canada", "Non-Muslim", None, GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Caucasus", "Non-Muslim", None, FAIR, False, 0, False, 0),
        Country(app, "Central Asia", "Suni", None, None, False, 0, False, 2),
        Country(app, "China", "Non-Muslim", None, FAIR, False, 0, False, 0),
        Country(app, "Eastern Europe", "Non-Muslim", None, GOOD, True, 0, False, 0),
        Country(app, "Egypt", "Suni", None, None, False, 0, False, 3),
        Country(app, "France", "Non-Muslim", None, GOOD, True, 2, False, 0),
        Country(app, "Germany", "Non-Muslim", None, GOOD, True, 0, False, 0),
        Country(app, "Gulf States", "Shia-Mix", None, None, False, 0, True, 3),
        Country(app, "India", "Non-Muslim", None, GOOD, False, 0, False, 0),
        Country(app, "Indonesia/Malaysia", "Suni", None, None, False, 0, True, 3),
        Iran(app),
        Country(app, "Iraq", "Shia-Mix", None, None, False, 0, True, 3),
        Country(app, "Israel", "Non-Muslim", HARD, GOOD, False, 0, False, 0),
        Country(app, "Italy", "Non-Muslim", None, GOOD, True, 0, False, 0),
        Country(app, "Jordan", "Suni", None, None, False, 0, False, 1),
        Country(app, "Kenya/Tanzania", "Non-Muslim", None, FAIR, False, 0, False, 0),
        Country(app, "Lebanon", "Shia-Mix", None, None, False, 0, False, 1, schengen_link=True),
        Country(app, "Libya", "Suni", None, None, False, 0, True, 1, schengen_link=True),
        Country(app, "Morocco", "Suni", None, None, False, 0, False, 2, schengen_link=True),
        Country(app, "Pakistan", "Shia-Mix", None, None, False, 0, False, 2),
        Country(app, "Philippines", "Non-Muslim", None, FAIR, False, 3, False, 0),
        Country(app, "Russia", "Non-Muslim", None, FAIR, False, 0, False, 0, schengen_link=True),
        Country(app, "Saudi Arabia", "Shia-Mix", None, None, False, 0, True, 3),
        Country(app, "Scandinavia", "Non-Muslim", None, GOOD, True, 0, False, 0),
        Country(app, "Serbia", "Non-Muslim", None, GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Somalia", "Suni", None, None, False, 0, False, 1),
        Country(app, "Spain", "Non-Muslim", None, GOOD, True, 2, False, 0),
        Country(app, "Sudan", "Suni", None, None, False, 0, True, 1),
        Country(app, "Syria", "Suni", None, None, False, 0, False, 2),
        Country(app, "Thailand", "Non-Muslim", None, FAIR, False, 0, False, 0),
        Country(app, "Turkey", "Shia-Mix", None, None, False, 0, False, 2, schengen_link=True),
        Country(app, "United Kingdom", "Non-Muslim", None, GOOD, False, 3, False, 0, schengen_link=True),
        Country(app, "United States", "Non-Muslim", HARD, GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Yemen", "Shia-Mix", None, None, False, 0, False, 1)
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
