from lwotai.alignment import ADVERSARY, ALLY, NEUTRAL
from lwotai.countries.country import Country
from lwotai.countries.types import SUNNI, SHIA_MIX
from lwotai.governance import ISLAMIST_RULE, GOOD, FAIR, POOR
from lwotai.utils import Utils


class MuslimCountry(Country):
    """A Shia-Mix or Sunni country; does not include Iran"""

    def __init__(self, app, name, country_type, oil_producing, resources, schengen_link=False):
        super(MuslimCountry, self).__init__(app, name, None, False, 0, oil_producing, resources, schengen_link)
        self.__aid = 0
        self.__alignment = None
        self.__besieged = False
        self.__regime_change = False
        self.__type = Utils.require_one_of(country_type, [SHIA_MIX, SUNNI])

    def _ought_to_have_been_tested(self):
        return super(MuslimCountry, self)._ought_to_have_been_tested() or self.__aid or self.__regime_change

    def add_aid(self, aid_to_add):
        """Adds the given number of Aid markers to this country"""
        assert aid_to_add >= 0, "Cannot add %d aid" % aid_to_add
        self.__aid += aid_to_add

    def alignment(self):
        return self.__alignment

    def check_is_tested(self):
        if self._ought_to_have_been_tested():
            assert self.is_governed(), "Ungoverned country: %s" % self.print_country()
            assert self.is_aligned(), "%s is unaligned" % self.name

    @staticmethod
    def get_adjustable_attributes():
        """Returns a list of this country's adjustable attributes"""
        return ["active", "aid", "alignment", "besieged", "cadre", "governance", "marker", "plots", "regime", "sleeper",
                "troops"]

    def get_aid(self):
        """Returns the number of Aid markers in this country (0 or more)"""
        return self.__aid

    def improve_governance(self):
        self.set_governance(self.get_governance().improve())
        if self.is_good():
            self.__aid = 0
            self.remove_besieged()
            self.remove_regime_change()

    def is_adversary(self):
        return self.__alignment == ADVERSARY

    def is_aligned(self):
        return self.__alignment

    def is_ally(self):
        return self.__alignment == ALLY

    def is_besieged(self):
        """Indicates whether this country is a Besieged Regime"""
        return self.__besieged

    def is_governed(self):
        return self.get_governance() is not None

    def is_islamist_rule(self):
        return self.get_governance() == ISLAMIST_RULE

    def is_major_jihad_possible(self, ops, excess_cells_needed, bhutto_in_play):
        if self.is_islamist_rule():
            return False
        if bhutto_in_play and self.name == "Pakistan":
            return False
        if self.total_cells(True) - self.troops() < excess_cells_needed:
            return False
        ops_needed_from_poor = 1 if self.is_besieged() else 2
        ops_needed = ops_needed_from_poor + self.get_governance().levels_above_poor()
        return ops >= ops_needed

    def is_muslim(self):
        return True

    def is_neutral(self):
        return self.__alignment == NEUTRAL

    def is_regime_change(self):
        return self.__regime_change

    def is_shia_mix(self):
        return self.__type == SHIA_MIX

    def is_ungoverned(self):
        return not self.is_governed()

    def make_adversary(self):
        self.__alignment = ADVERSARY

    def make_ally(self):
        self.__alignment = ALLY

    def make_besieged(self):
        self.__besieged = True

    def make_good(self):
        self.set_governance(GOOD)

    def make_fair(self):
        self.set_governance(FAIR)

    def make_islamist_rule(self):
        self.set_governance(ISLAMIST_RULE)

    def make_neutral(self):
        self.__alignment = NEUTRAL

    def make_poor(self):
        self.set_governance(POOR)

    def make_regime_change(self):
        self.__regime_change = True

    def make_ungoverned(self):
        self.set_governance(None)

    def reduce_aid_by(self, aid_to_lose):
        """Reduces the level of aid by the given amount, if possible; returns the amount actually removed"""
        assert aid_to_lose >= 0, "%d must not be negative" % aid_to_lose
        aid_actually_removed = min(aid_to_lose, self.__aid)
        self.__aid -= aid_actually_removed
        return aid_actually_removed

    def remove_besieged(self):
        self.__besieged = False

    def remove_regime_change(self):
        self.__regime_change = False

    def set_aid(self, aid):
        """Sets the number of Aid markers in this country (to 0 or more)"""
        self.__aid = max(0, aid)

    def summary(self):
        """Returns a textual summary of this Country"""
        resources = self.get_resources(self.app.oil_price_spikes())
        summary = "%s, %s %s, %d Resource(s)\n    " % (self.name, self.governance_str(), self.__alignment, resources)
        item_strings = []
        if self.troopCubes:
            # We don't include NATO here, that's a marker
            item_strings.append("Troop cubes: %d" % self.troopCubes)
        if self.activeCells:
            item_strings.append("Active: %d" % self.activeCells)
        if self.sleeperCells:
            item_strings.append("Sleeper: %d" % self.sleeperCells)
        if self.has_cadre():
            item_strings.append("Cadre: %d" % self.cadre)
        if self.__aid:
            item_strings.append("Aid: %d" % self.__aid)
        if self.is_besieged():
            item_strings.append("Besieged Regime")
        if self.is_regime_change():
            item_strings.append("Regime Change")
        if self.plots:
            item_strings.append("Plots: %d" % self.plots)
        if self.markers:
            item_strings.append("Markers: %s" % ", ".join(self.markers))
        if item_strings:
            summary += ", ".join(item_strings)
        else:
            summary += "Empty"
        return summary

    def test(self, test_roll):
        """Tests this country's governance, if as yet untested, using the given roll"""
        if self.is_ungoverned():
            if test_roll <= 4:
                self.make_poor()
            else:
                self.make_fair()
            self.make_neutral()
            self.app.output_to_history("%s tested, governance %s" % (self.name, self.governance_str()), False)

    def worsen_governance(self):
        self.set_governance(self.get_governance().worsen())
