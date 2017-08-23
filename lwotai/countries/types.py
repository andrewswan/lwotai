from lwotai.utils import Utils


class CountryType(object):
    """A type of country in the game"""

    def __init__(self, name):
        self.__name = Utils.require_type(name, str)

    def __repr__(self):
        return super(CountryType, self).__repr__()

    def __eq__(self, o):
        try:
            return self.__name == o.__name
        except AttributeError:
            return False

    def __ne__(self, o):
        return not self.__eq__(o)


# The four conutry types in the game - these are mutually exclusive
NON_MUSLIM = CountryType("Non-Muslim")
IRAN = CountryType("Iran")
SUNNI = CountryType("Sunni")
SHIA_MIX = CountryType("Shia-Mix")
