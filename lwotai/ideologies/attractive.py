from lwotai.ideologies.coherent import Coherent


class Attractive(Coherent):
    """
    Contrary to what the 2011 rulebook says, this ideology does indeed extend
    the Coherent one, see https://boardgamegeek.com/article/7952594#7952594.
    """

    def name(self):
        return "Attractive"

    def difference(self):
        return "as above, plus each Recruit success places two available cells (modifies 8.2.1)"

    def ops_to_recruit(self, cells):
        return (cells / 2) + (cells % 2)

    def recruits_per_success(self):
        """Returns the number of cells placed by each Recruit success"""
        return 2
