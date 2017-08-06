from lwotai.ideologies.ideology import Ideology


class Normal(Ideology):

    def name(self):
        return "Normal"

    def difference(self):
        """Returns a description of the difference between this and the previous ideology, if any"""
        return ""

    def excess_cells_for_major_jihad(self):
        """
        Returns the number of cells that the Jihadist player needs, in excess
        of the number of troops, in order to conduct a Major Jihad
        """
        return 5

    def failed_jihad_rolls_remove_cells(self):
        """Indicates whether the Jihadist player must remove a cell for each failed Jihad roll"""
        return True

    def ops_to_recruit(self, cells):
        """Returns the number of Ops required to recruit the given number of cells"""
        return cells

    def plots_per_success(self):
        """Returns the number of available Plot markers placed by a Plot success"""
        return 1

    def recruits_per_success(self):
        """Returns the number of cells placed by each Recruit success"""
        return 1

    def us_must_play_all_cards(self):
        """Indicates whether the US player is required to play all their cards"""
        return False
