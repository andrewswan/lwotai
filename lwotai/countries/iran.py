from lwotai.countries.types import IRAN
from lwotai.countries.country import Country
from lwotai.governance import FAIR


class Iran(Country):
    """Special class for the country of Iran"""

    def __init__(self, app):
        super(Iran, self).__init__(app, "Iran", IRAN, None, FAIR, False, 0, False, 0)

    def is_muslim(self):
        return False  # Rule 4.4

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

    def make_adversary(self):
        raise

    def make_ally(self):
        raise

    def make_neutral(self):
        raise

    # ---------- Governance ----------

    def improve_governance(self):
        raise

    def is_fair(self):
        return True

    def is_good(self):
        return False

    def is_poor(self):
        return 

    def worsen_governance(self):
        raise

    # ---------- Posture ----------

    def is_hard(self):
        return False

    def is_soft(self):
        return False

    def make_hard(self):
        raise

    def make_soft(self):
        raise

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
