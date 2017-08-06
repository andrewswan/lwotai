from ideology import Ideology
from infectious import Infectious


class Virulent(Infectious):

    def __init__(self):
        Ideology.__init__(self, "Virulent")

    def difference(self):
        return "The above, plus failed Jihad rolls do not remove cells (modifies 8.4.3)."

    def failed_jihad_rolls_remove_cells(self):
        return False
