from lwotai.ideologies.attractive import Attractive


class Potent(Attractive):

    def name(self):
        return "Potent"

    def difference(self):
        return "... and just three more cells than troops allows Major Jihad (modifies 8.4.2)"

    def excess_cells_for_major_jihad(self):
        return 3

