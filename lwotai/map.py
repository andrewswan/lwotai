from lwotai.country import Country
from lwotai.governance import GOOD, FAIR


class Map(object):
    """The map on the board"""

    def __init__(self, app):
        self._map = {
            "Algeria/Tunisia":
                Country(app, "Algeria/Tunisia", "Suni", "", None, False, 0, True, 2, schengen_link=True),
            "Afghanistan":
                Country(app, "Afghanistan", "Shia-Mix", "", None, False, 0, False, 1),
            "Benelux":
                Country(app, "Benelux", "Non-Muslim", "", GOOD, True, 0, False, 0),
            "Canada":
                Country(app, "Canada", "Non-Muslim", "", GOOD, False, 0, False, 0, schengen_link=True),
            "Caucasus":
                Country(app, "Caucasus", "Non-Muslim", "", FAIR, False, 0, False, 0),
            "Central Asia":
                Country(app, "Central Asia", "Suni", "", None, False, 0, False, 2),
            "China":
                Country(app, "China", "Non-Muslim", "", FAIR, False, 0, False, 0),
            "Eastern Europe":
                Country(app, "Eastern Europe", "Non-Muslim", "", GOOD, True, 0, False, 0),
            "Egypt":
                Country(app, "Egypt", "Suni", "", None, False, 0, False, 3),
            "France":
                Country(app, "France", "Non-Muslim", "", GOOD, True, 2, False, 0),
            "Germany":
                Country(app, "Germany", "Non-Muslim", "", GOOD, True, 0, False, 0),
            "Gulf States":
                Country(app, "Gulf States", "Shia-Mix", "", None, False, 0, True, 3),
            "India":
                Country(app, "India", "Non-Muslim", "", GOOD, False, 0, False, 0),
            "Indonesia/Malaysia":
                Country(app, "Indonesia/Malaysia", "Suni", "", None, False, 0, True, 3),
            "Iran":
                Country(app, "Iran", "Iran", None, FAIR, False, 0, False, 0),
            "Iraq":
                Country(app, "Iraq", "Shia-Mix", "", None, False, 0, True, 3),
            "Israel":
                Country(app, "Israel", "Non-Muslim", "Hard", GOOD, False, 0, False, 0),
            "Italy":
                Country(app, "Italy", "Non-Muslim", "", GOOD, True, 0, False, 0),
            "Jordan":
                Country(app, "Jordan", "Suni", "", None, False, 0, False, 1),
            "Kenya/Tanzania":
                Country(app, "Kenya/Tanzania", "Non-Muslim", "", FAIR, False, 0, False, 0),
            "Lebanon":
                Country(app, "Lebanon", "Shia-Mix", "", None, False, 0, False, 1, schengen_link=True),
            "Libya":
                Country(app, "Libya", "Suni", "", None, False, 0, True, 1, schengen_link=True),
            "Morocco":
                Country(app, "Morocco", "Suni", "", None, False, 0, False, 2, schengen_link=True),
            "Pakistan":
                Country(app, "Pakistan", "Shia-Mix", "", None, False, 0, False, 2),
            "Philippines":
                Country(app, "Philippines", "Non-Muslim", "", FAIR, False, 3, False, 0),
            "Russia":
                Country(app, "Russia", "Non-Muslim", "", FAIR, False, 0, False, 0, schengen_link=True),
            "Saudi Arabia":
                Country(app, "Saudi Arabia", "Shia-Mix", "", None, False, 0, True, 3),
            "Scandinavia":
                Country(app, "Scandinavia", "Non-Muslim", "", GOOD, True, 0, False, 0),
            "Serbia":
                Country(app, "Serbia", "Non-Muslim", "", GOOD, False, 0, False, 0, schengen_link=True),
            "Somalia":
                Country(app, "Somalia", "Suni", "", None, False, 0, False, 1),
            "Spain":
                Country(app, "Spain", "Non-Muslim", "", GOOD, True, 2, False, 0),
            "Sudan":
                Country(app, "Sudan", "Suni", "", None, False, 0, True, 1),
            "Syria":
                Country(app, "Syria", "Suni", "", None, False, 0, False, 2),
            "Thailand":
                Country(app, "Thailand", "Non-Muslim", "", FAIR, False, 0, False, 0),
            "Turkey":
                Country(app, "Turkey", "Shia-Mix", "", None, False, 0, False, 2, schengen_link=True),
            "United Kingdom":
                Country(app, "United Kingdom", "Non-Muslim", "", GOOD, False, 3, False, 0, schengen_link=True),
            "United States":
                Country(app, "United States", "Non-Muslim", "Hard", GOOD, False, 0, False, 0, schengen_link=True),
            "Yemen":
                Country(app, "Yemen", "Shia-Mix", "", None, False, 0, False, 1)
        }

        # Canada
        self._map["Canada"].links.append(self._map["United States"])
        self._map["Canada"].links.append(self._map["United Kingdom"])
        # United States
        self._map["United States"].links.append(self._map["Canada"])
        self._map["United States"].links.append(self._map["United Kingdom"])
        self._map["United States"].links.append(self._map["Philippines"])
        # United Kingdom
        self._map["United Kingdom"].links.append(self._map["Canada"])
        self._map["United Kingdom"].links.append(self._map["United States"])
        # Serbia
        self._map["Serbia"].links.append(self._map["Russia"])
        self._map["Serbia"].links.append(self._map["Turkey"])
        # Israel
        self._map["Israel"].links.append(self._map["Lebanon"])
        self._map["Israel"].links.append(self._map["Jordan"])
        self._map["Israel"].links.append(self._map["Egypt"])
        # India
        self._map["India"].links.append(self._map["Pakistan"])
        self._map["India"].links.append(self._map["Indonesia/Malaysia"])
        # Russia
        self._map["Russia"].links.append(self._map["Serbia"])
        self._map["Russia"].links.append(self._map["Turkey"])
        self._map["Russia"].links.append(self._map["Caucasus"])
        self._map["Russia"].links.append(self._map["Central Asia"])
        # Caucasus
        self._map["Caucasus"].links.append(self._map["Russia"])
        self._map["Caucasus"].links.append(self._map["Turkey"])
        self._map["Caucasus"].links.append(self._map["Iran"])
        self._map["Caucasus"].links.append(self._map["Central Asia"])
        # China
        self._map["China"].links.append(self._map["Central Asia"])
        self._map["China"].links.append(self._map["Thailand"])
        # Kenya/Tanzania
        self._map["Kenya/Tanzania"].links.append(self._map["Sudan"])
        self._map["Kenya/Tanzania"].links.append(self._map["Somalia"])
        # Thailand
        self._map["Thailand"].links.append(self._map["China"])
        self._map["Thailand"].links.append(self._map["Philippines"])
        self._map["Thailand"].links.append(self._map["Indonesia/Malaysia"])
        # Philippines
        self._map["Philippines"].links.append(self._map["United States"])
        self._map["Philippines"].links.append(self._map["Thailand"])
        self._map["Philippines"].links.append(self._map["Indonesia/Malaysia"])
        # Morocco
        self._map["Morocco"].links.append(self._map["Algeria/Tunisia"])
        # Algeria/Tunisia
        self._map["Algeria/Tunisia"].links.append(self._map["Morocco"])
        self._map["Algeria/Tunisia"].links.append(self._map["Libya"])
        # Libya
        self._map["Libya"].links.append(self._map["Algeria/Tunisia"])
        self._map["Libya"].links.append(self._map["Egypt"])
        self._map["Libya"].links.append(self._map["Sudan"])
        # Egypt
        self._map["Egypt"].links.append(self._map["Libya"])
        self._map["Egypt"].links.append(self._map["Israel"])
        self._map["Egypt"].links.append(self._map["Sudan"])
        # Sudan
        self._map["Sudan"].links.append(self._map["Libya"])
        self._map["Sudan"].links.append(self._map["Egypt"])
        self._map["Sudan"].links.append(self._map["Kenya/Tanzania"])
        self._map["Sudan"].links.append(self._map["Somalia"])
        # Somalia
        self._map["Somalia"].links.append(self._map["Sudan"])
        self._map["Somalia"].links.append(self._map["Kenya/Tanzania"])
        self._map["Somalia"].links.append(self._map["Yemen"])
        # Jordan
        self._map["Jordan"].links.append(self._map["Israel"])
        self._map["Jordan"].links.append(self._map["Syria"])
        self._map["Jordan"].links.append(self._map["Iraq"])
        self._map["Jordan"].links.append(self._map["Saudi Arabia"])
        # Syria
        self._map["Syria"].links.append(self._map["Turkey"])
        self._map["Syria"].links.append(self._map["Lebanon"])
        self._map["Syria"].links.append(self._map["Jordan"])
        self._map["Syria"].links.append(self._map["Iraq"])
        # Central Asia
        self._map["Central Asia"].links.append(self._map["Russia"])
        self._map["Central Asia"].links.append(self._map["Caucasus"])
        self._map["Central Asia"].links.append(self._map["Iran"])
        self._map["Central Asia"].links.append(self._map["Afghanistan"])
        self._map["Central Asia"].links.append(self._map["China"])
        # Indonesia/Malaysia
        self._map["Indonesia/Malaysia"].links.append(self._map["Thailand"])
        self._map["Indonesia/Malaysia"].links.append(self._map["India"])
        self._map["Indonesia/Malaysia"].links.append(self._map["Philippines"])
        self._map["Indonesia/Malaysia"].links.append(self._map["Pakistan"])
        # Turkey
        self._map["Turkey"].links.append(self._map["Serbia"])
        self._map["Turkey"].links.append(self._map["Russia"])
        self._map["Turkey"].links.append(self._map["Caucasus"])
        self._map["Turkey"].links.append(self._map["Iran"])
        self._map["Turkey"].links.append(self._map["Syria"])
        self._map["Turkey"].links.append(self._map["Iraq"])
        # Lebanon
        self._map["Lebanon"].links.append(self._map["Syria"])
        self._map["Lebanon"].links.append(self._map["Israel"])
        # Yemen
        self._map["Yemen"].links.append(self._map["Saudi Arabia"])
        self._map["Yemen"].links.append(self._map["Somalia"])
        # Iraq
        self._map["Iraq"].links.append(self._map["Syria"])
        self._map["Iraq"].links.append(self._map["Turkey"])
        self._map["Iraq"].links.append(self._map["Iran"])
        self._map["Iraq"].links.append(self._map["Gulf States"])
        self._map["Iraq"].links.append(self._map["Saudi Arabia"])
        self._map["Iraq"].links.append(self._map["Jordan"])
        # Saudi Arabia
        self._map["Saudi Arabia"].links.append(self._map["Jordan"])
        self._map["Saudi Arabia"].links.append(self._map["Iraq"])
        self._map["Saudi Arabia"].links.append(self._map["Gulf States"])
        self._map["Saudi Arabia"].links.append(self._map["Yemen"])
        # Gulf States
        self._map["Gulf States"].links.append(self._map["Iran"])
        self._map["Gulf States"].links.append(self._map["Pakistan"])
        self._map["Gulf States"].links.append(self._map["Saudi Arabia"])
        self._map["Gulf States"].links.append(self._map["Iraq"])
        # Pakistan
        self._map["Pakistan"].links.append(self._map["Iran"])
        self._map["Pakistan"].links.append(self._map["Afghanistan"])
        self._map["Pakistan"].links.append(self._map["India"])
        self._map["Pakistan"].links.append(self._map["Gulf States"])
        self._map["Pakistan"].links.append(self._map["Indonesia/Malaysia"])
        # Afghanistan
        self._map["Afghanistan"].links.append(self._map["Central Asia"])
        self._map["Afghanistan"].links.append(self._map["Pakistan"])
        self._map["Afghanistan"].links.append(self._map["Iran"])
        # Iran
        self._map["Iran"].links.append(self._map["Central Asia"])
        self._map["Iran"].links.append(self._map["Afghanistan"])
        self._map["Iran"].links.append(self._map["Pakistan"])
        self._map["Iran"].links.append(self._map["Gulf States"])
        self._map["Iran"].links.append(self._map["Iraq"])
        self._map["Iran"].links.append(self._map["Turkey"])
        self._map["Iran"].links.append(self._map["Caucasus"])

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
