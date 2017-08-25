from lwotai.ideologies.normal import Normal


class Coherent(Normal):

    def name(self):
        return "Coherent"

    def difference(self):
        return "Each Plot success places two Available Plot markers (modifies 8.5.2)"

    def plots_per_success(self):
        """Returns the number of available Plot markers placed by a Plot success"""
        return 2
