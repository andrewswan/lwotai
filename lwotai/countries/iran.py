from lwotai.countries.country import Country
from lwotai.governance import FAIR


class Iran(Country):
    """Special class for the country of Iran"""

    def __init__(self, app):
        super(Iran, self).__init__(app, "Iran", "Iran", None, FAIR, False, 0, False, 0)

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
