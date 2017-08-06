from ideology import Ideology
from potent import Potent


class Infectious(Potent):

    def __init__(self):
        Ideology.__init__(self, "Infectious")

    def difference(self):
        return "The above, plus the US must play all its cards (modifies 5.2.4)."

    def us_must_play_all_cards(self):
        return True
