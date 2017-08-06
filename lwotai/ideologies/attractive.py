from lwotai.ideologies.coherent import Coherent


class Attractive(Coherent):

    def name(self):
        return "Attractive"

    def difference(self):
        return "Each Recruit success places two available cells (modifies 8.2.1)."

    def ops_to_recruit(self, cells):
        return (cells / 2) + (cells % 2)

    def recruits_per_success(self):
        """Returns the number of cells placed by each Recruit success"""
        return 2
