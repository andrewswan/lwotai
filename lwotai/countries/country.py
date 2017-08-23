from lwotai.alignment import ALLY, NEUTRAL, ADVERSARY
from lwotai.countries.types import CountryType, SHIA_MIX
from lwotai.governance import GOOD, FAIR, POOR, ISLAMIST_RULE
from lwotai.governance import Governance
from lwotai.utils import Utils


class Country(object):
    """A country on the map"""

    def __init__(self, app, name, country_type, governance, schengen, recruit, oil_producing, resources,
                 schengen_link=False):
        self.__alignment = None
        self.__besieged = False
        self.__governance = governance
        self.__oil_producing = oil_producing
        self.__regime_change = False
        self.__type = Utils.require_type(country_type, CountryType)
        self.activeCells = 0
        self.aid = 0
        self.app = app
        self.cadre = 0
        self.links = []
        self.markers = []
        self.name = name
        self.plots = 0
        self.recruit = recruit
        self.resources = resources
        self.schengen = schengen
        self.schengenLink = schengen_link
        self.sleeperCells = 0
        self.troopCubes = 0

    def __repr__(self):
        return self.name

    def alignment(self):
        return self.__alignment

    def is_adversary(self):
        return self.__alignment == ADVERSARY

    def is_ally(self):
        return self.__alignment == ALLY

    def is_neutral(self):
        return self.__alignment == NEUTRAL

    def is_aligned(self):
        return self.__alignment

    def is_besieged(self):
        """Indicates whether this country is a Besieged Regime"""
        return self.__besieged

    def make_adversary(self):
        self.__alignment = ADVERSARY

    def make_ally(self):
        self.__alignment = ALLY

    def make_besieged(self):
        self.__besieged = True

    def remove_besieged(self):
        self.__besieged = False

    def make_neutral(self):
        self.__alignment = NEUTRAL

    def is_good(self):
        return self.__governance == GOOD

    def is_fair(self):
        return self.__governance == FAIR

    def is_hard(self):
        return False

    def is_poor(self):
        return self.__governance == POOR

    def is_iran(self):
        return False

    def is_islamist_rule(self):
        return self.__governance == ISLAMIST_RULE

    def is_governed(self):
        return self.__governance is not None

    def is_regime_change(self):
        return self.__regime_change

    def is_shia_mix(self):
        return self.__type == SHIA_MIX

    def is_soft(self):
        return False

    def is_ungoverned(self):
        return not self.is_governed()

    def make_good(self):
        self.__governance = GOOD

    def make_fair(self):
        self.__governance = FAIR

    def make_poor(self):
        self.__governance = POOR

    def make_regime_change(self):
        self.__regime_change = True

    def make_islamist_rule(self):
        self.__governance = ISLAMIST_RULE

    def make_ungoverned(self):
        self.__governance = None

    def make_governance(self, governance):
        self.__governance = Utils.require_type_or_none(governance, Governance)

    def remove_regime_change(self):
        self.__regime_change = False

    def remove_plot_marker(self):
        """Removes one plot marker from this country, if any are present; returns True if one was removed"""
        if self.plots > 0:
            self.plots -= 1
            return True
        return False

    def activate_sleepers(self, sleeper_cells_to_activate):
        """Activates the given number of sleeper cells in this country"""
        assert sleeper_cells_to_activate <= self.sleeperCells
        self.activeCells += sleeper_cells_to_activate
        self.sleeperCells -= sleeper_cells_to_activate

    def check_is_tested(self):
        if self._ought_to_have_been_tested():
            assert self.is_governed(), "Ungoverned country: %s" % self.print_country()
            if self.is_muslim():
                assert self.is_aligned(), "%s is unaligned" % self.name

    def _ought_to_have_been_tested(self):
        """Indicates whether this country ought to have been tested by now"""
        return self.sleeperCells > 0 or self.activeCells > 0 or self.troopCubes > 0 or self.aid > 0 or \
            self.is_regime_change() or self.cadre > 0 or self.plots > 0

    def has_data(self):
        """Indicates whether this country contains anything not printed on the board"""
        return self._ought_to_have_been_tested() or self.is_besieged() or self.markers

    def is_non_muslim(self):
        """Indicates whether this country is Non-Muslim (which is not the opposite of Muslim)"""
        return False  # Overridden in NonMuslimCountry class

    def is_non_recruit_success(self, roll):
        return self.is_governed() and self.__governance.is_success(roll)

    def is_recruit_success(self, roll, recruit_override=None):
        max_recruit_roll = self.max_recruit_roll(recruit_override)
        return max_recruit_roll is not None and roll <= max_recruit_roll

    def improve_governance(self):
        self.__governance = self.__governance.improve()
        if self.is_good():
            self.aid = 0
            self.remove_besieged()
            self.remove_regime_change()

    def worsen_governance(self):
        self.__governance = self.__governance.worsen()

    def governance_is_better_than(self, governance):
        return self.__governance is not None and self.__governance.is_better_than(governance)

    def governance_is_worse_than(self, governance):
        return self.__governance is not None and self.__governance.is_worse_than(governance)

    def is_muslim(self):
        """Indicates whether this country is Muslim (does not include Iran)"""
        return True

    def is_major_jihad_possible(self, ops, excess_cells_needed, bhutto_in_play):
        if self.is_islamist_rule():
            return False
        if not self.is_muslim():
            return False
        if bhutto_in_play and self.name == "Pakistan":
            return False
        if self.total_cells(True) - self.troops() < excess_cells_needed:
            return False
        ops_needed_from_poor = 1 if self.is_besieged() else 2
        ops_needed = ops_needed_from_poor + self.__governance.levels_above_poor()
        return ops >= ops_needed

    def can_have_posture(self):
        """Indicates whether this country can have a posture (excludes the US)"""
        return False

    def can_recruit(self, madrassas):
        return (self.total_cells(True) > 0 or
                self.has_cadre() or
                (madrassas and self.governance_is_worse_than(FAIR)))

    def can_disrupt(self):
        """Indicates whether the US can conduct a Disrupt operation in this country"""
        return (
            (self.total_cells() > 0 or self.has_cadre()) and
            (self.is_ally() or self.troops() >= 2 or self.is_non_muslim())
        )

    def get_disrupt_summary(self):
        return "%s - %d Active Cells, %d Sleeper Cells, %d Cadre, Ops Reqd %d, Troops: %d" %\
               (self.name, self.activeCells, self.sleeperCells, self.cadre, self.__governance.min_us_ops(),
                self.troops())

    def max_recruit_roll(self, recruit_override=None):
        if recruit_override:
            return recruit_override
        if self.recruit > 0:
            return self.recruit
        if self.is_governed():
            return self.__governance.max_success_roll()
        return None

    def governance_as_funding(self):
        return self.__governance.max_success_roll()

    def get_posture(self):
        """Returns the Posture of this country (might be None)"""
        return None

    def get_recruit_score(self, ops):
        if self.is_regime_change() and self.troops() - self.total_cells(True) >= 5:
            return 100000000
        if self.is_islamist_rule() and self.total_cells(True) < 2 * ops:
            return 10000000
        if not self.is_islamist_rule() and not self.is_regime_change():
            return self.max_recruit_roll() * 1000000
        return None

    def total_cells(self, include_sadr=False):
        total = self.activeCells + self.sleeperCells
        if include_sadr and "Sadr" in self.markers:
            total += 1
        return total

    def num_active_cells(self):
        total = self.activeCells
        if "Sadr" in self.markers:
            total += 1
        return total

    def reduce_aid_by(self, aid_lost):
        """Reduces the level of aid by the given amount, but not below zero"""
        self.aid = max(self.aid - aid_lost, 0)

    def remove_active_cell(self):
        self.activeCells -= 1
        if self.activeCells < 0:  # 20150131PS - changed from <= to <
            if "Sadr" in self.markers:
                self.markers.remove("Sadr")
                self.app.output_to_history("Sadr removed from %s" % self.name, False)
                self.activeCells = 0    # 20150131PS - added
                return
            else:
                self.activeCells = 0
        self.app.output_to_history("Active cell Removed to Funding Track", False)
        self.app.cells += 1

    def get_resources(self, oil_price_spikes):
        """
        Returns the amount of resources produced by this country,
        given how many oil price spikes are in effect.
        """
        if self.__oil_producing:
            return self.resources + oil_price_spikes
        else:
            return self.resources

    def test(self, test_roll):
        """Tests this (Muslim) country's governance, if as yet untested, using the given roll"""
        if self.is_ungoverned():
            if test_roll <= 4:
                self.make_poor()
            else:
                self.make_fair()
            self.make_neutral()
            self.app.output_to_history("%s tested, governance %s" % (self.name, self.governance_str()), False)

    def troops(self):
        """Returns the effective number of troops in this country (including NATO)"""
        return self.troopCubes + 2 if "NATO" in self.markers else self.troopCubes

    def change_troops(self, delta):
        self.troopCubes += delta
        if self.troopCubes < 0:
            if "NATO" in self.markers:
                self.markers.remove("NATO")
                self.app.output_to_history("NATO removed from %s" % self.name, True)
            self.troopCubes = 0

    def governance_str(self):
        if self.is_ungoverned():
            return "Untested"
        return str(self.__governance)

    def has_cadre(self):
        """Indicates whether this country contains any cadre"""
        return self.cadre > 0

    def summary(self):
        """Returns a textual summary of this Country"""
        markers_str = ""
        if self.markers:
            markers_str = "\n   Markers: %s" % ", ".join(self.markers)
        assert self.is_muslim(), "Type is %s" % self.__type
        resources = self.get_resources(self.app.oil_price_spikes())
        return "%s, %s %s, %d Resource(s)\n" \
               "   Troops:%d Active:%d Sleeper:%d Cadre:%d Aid:%d Besieged:%d Reg Ch:%s Plots:%d %s" %\
               (self.name, self.governance_str(), self.__alignment, resources, self.troops(), self.activeCells,
                self.sleeperCells, self.cadre, self.aid, self.is_besieged(), self.is_regime_change(), self.plots,
                markers_str)

    def print_country(self):
        """Prints a textual summary of this Country"""
        print self.summary()
