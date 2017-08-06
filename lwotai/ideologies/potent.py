from attractive import Attractive
from ideology import Ideology


class Potent(Attractive):

    def __init__(self):
        Ideology.__init__(self, "Potent")

    def difference(self):
        return "The above, plus just three more cells than troops allows Major Jihad (modifies 8.4.2)."

    def excess_cells_for_major_jihad(self):
        return 3

