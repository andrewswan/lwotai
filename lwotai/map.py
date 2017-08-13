from lwotai.country import Country
from lwotai.governance import GOOD, FAIR


def _get_countries(app):
    """Returns the countries to add to the map"""
    return [
        Country(app, "Algeria/Tunisia", "Suni", "", None, False, 0, True, 2, schengen_link=True),
        Country(app, "Afghanistan", "Shia-Mix", "", None, False, 0, False, 1),
        Country(app, "Benelux", "Non-Muslim", "", GOOD, True, 0, False, 0),
        Country(app, "Canada", "Non-Muslim", "", GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Caucasus", "Non-Muslim", "", FAIR, False, 0, False, 0),
        Country(app, "Central Asia", "Suni", "", None, False, 0, False, 2),
        Country(app, "China", "Non-Muslim", "", FAIR, False, 0, False, 0),
        Country(app, "Eastern Europe", "Non-Muslim", "", GOOD, True, 0, False, 0),
        Country(app, "Egypt", "Suni", "", None, False, 0, False, 3),
        Country(app, "France", "Non-Muslim", "", GOOD, True, 2, False, 0),
        Country(app, "Germany", "Non-Muslim", "", GOOD, True, 0, False, 0),
        Country(app, "Gulf States", "Shia-Mix", "", None, False, 0, True, 3),
        Country(app, "India", "Non-Muslim", "", GOOD, False, 0, False, 0),
        Country(app, "Indonesia/Malaysia", "Suni", "", None, False, 0, True, 3),
        Country(app, "Iran", "Iran", None, FAIR, False, 0, False, 0),
        Country(app, "Iraq", "Shia-Mix", "", None, False, 0, True, 3),
        Country(app, "Israel", "Non-Muslim", "Hard", GOOD, False, 0, False, 0),
        Country(app, "Italy", "Non-Muslim", "", GOOD, True, 0, False, 0),
        Country(app, "Jordan", "Suni", "", None, False, 0, False, 1),
        Country(app, "Kenya/Tanzania", "Non-Muslim", "", FAIR, False, 0, False, 0),
        Country(app, "Lebanon", "Shia-Mix", "", None, False, 0, False, 1, schengen_link=True),
        Country(app, "Libya", "Suni", "", None, False, 0, True, 1, schengen_link=True),
        Country(app, "Morocco", "Suni", "", None, False, 0, False, 2, schengen_link=True),
        Country(app, "Pakistan", "Shia-Mix", "", None, False, 0, False, 2),
        Country(app, "Philippines", "Non-Muslim", "", FAIR, False, 3, False, 0),
        Country(app, "Russia", "Non-Muslim", "", FAIR, False, 0, False, 0, schengen_link=True),
        Country(app, "Saudi Arabia", "Shia-Mix", "", None, False, 0, True, 3),
        Country(app, "Scandinavia", "Non-Muslim", "", GOOD, True, 0, False, 0),
        Country(app, "Serbia", "Non-Muslim", "", GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Somalia", "Suni", "", None, False, 0, False, 1),
        Country(app, "Spain", "Non-Muslim", "", GOOD, True, 2, False, 0),
        Country(app, "Sudan", "Suni", "", None, False, 0, True, 1),
        Country(app, "Syria", "Suni", "", None, False, 0, False, 2),
        Country(app, "Thailand", "Non-Muslim", "", FAIR, False, 0, False, 0),
        Country(app, "Turkey", "Shia-Mix", "", None, False, 0, False, 2, schengen_link=True),
        Country(app, "United Kingdom", "Non-Muslim", "", GOOD, False, 3, False, 0, schengen_link=True),
        Country(app, "United States", "Non-Muslim", "Hard", GOOD, False, 0, False, 0, schengen_link=True),
        Country(app, "Yemen", "Shia-Mix", "", None, False, 0, False, 1)
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
        """Returns the Country with the given name"""
        return self._map[country_name]

    def countries(self):
        """Returns all Countries on the map"""
        return self._map.values()

    def count_countries(self, predicate):
        """Returns the number of countries that match the given predicate"""
        return len(self.find(predicate))

    def contains(self, predicate):
        """Indicates whether the map contains any countries matching the given predicate"""
        return self.count_countries(predicate) > 0
