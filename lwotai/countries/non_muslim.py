from lwotai.countries.types import NON_MUSLIM

from lwotai.countries.country import Country


class NonMuslimCountry(Country):
    """Does not include Iran"""

    def __init__(self, app, name, posture, governance, schengen, recruit=0, schengen_link=False):
        super(NonMuslimCountry, self).__init__(
            app, name, NON_MUSLIM, posture, governance, schengen, recruit, False, 0, schengen_link)
