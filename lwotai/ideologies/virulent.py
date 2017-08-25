from lwotai.ideologies.infectious import Infectious


class Virulent(Infectious):

    def name(self):
        return "Virulent"

    def difference(self):
        return "as above, plus failed Jihad rolls do not remove cells (modifies 8.4.3)"

    def failed_jihad_rolls_remove_cells(self):
        return False
