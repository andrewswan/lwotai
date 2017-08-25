from lwotai.countries.country import Country
from lwotai.governance import FAIR


class Iran(Country):
    """Special class for the country of Iran"""

    def __init__(self, app):
        super(Iran, self).__init__(app, "Iran", FAIR, False, 0, False, 0)

    def is_muslim(self):
        return False  # Rule 4.4

    def is_shia_mix(self):
        return False

    # ---------- Alignment ----------

    def alignment(self):
        return None

    def is_adversary(self):
        return False

    def is_aligned(self):
        return False

    def is_ally(self):
        return False

    def is_iran(self):
        return True

    def is_neutral(self):
        return False

    @staticmethod
    def make_adversary():
        raise Exception("Not in Iran")

    @staticmethod
    def make_ally():
        raise Exception("Not in Iran")

    @staticmethod
    def make_neutral():
        raise Exception("Not in Iran")

    # ---------- Governance ----------

    @staticmethod
    def improve_governance():
        raise Exception("Not in Iran")

    def is_fair(self):
        return True

    def is_good(self):
        return False

    def is_poor(self):
        return

    @staticmethod
    def test(roll):
        """Tests this country using the given roll"""
        pass

    @staticmethod
    def worsen_governance():
        raise Exception("Not in Iran")

    # ---------- Posture ----------

    def is_hard(self):
        return False

    def is_soft(self):
        return False

    @staticmethod
    def make_hard():
        raise Exception("Not in Iran")

    @staticmethod
    def make_soft():
        raise Exception("Not in Iran")

    def summary(self):
        """Returns a textual summary of this Country"""
        summary = "Iran, Fair"
        item_strings = []
        if self.activeCells:
            item_strings.append("Active: %d" % self.activeCells)
        if self.sleeperCells:
            item_strings.append("Sleeper: %d" % self.sleeperCells)
        if self.cadre:
            item_strings.append("Cadre: %d" % self.cadre)
        if self.plots:
            item_strings.append("Plots: %d" % self.plots)
        if self.markers:
            item_strings.append("Markers: %s" % ", ".join(self.markers))
        if item_strings:
            summary += "\n    " + ", ".join(item_strings)
        return summary
