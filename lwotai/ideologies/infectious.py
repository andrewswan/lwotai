from lwotai.ideologies.potent import Potent


class Infectious(Potent):

    def name(self):
        return "Infectious"

    def difference(self):
        return "as above, plus the US must play all its cards (modifies 5.2.4)"

    def us_must_play_all_cards(self):
        return True
