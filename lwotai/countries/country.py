from lwotai.utils import Utils

from lwotai.governance import GOOD, FAIR, POOR, Governance


class Country(object):
    """A country on the map"""

    def __init__(self, app, name, governance, schengen, recruit, oil_producing, resources, schengen_link=False):
        self.__governance = governance
        self.__oil_producing = oil_producing
        self.activeCells = 0
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
        return None

    def get_aid(self):
        return 0

    def is_adversary(self):
        return False

    def is_ally(self):
        return False

    def is_neutral(self):
        return False

    def is_aligned(self):
        return False

    def is_besieged(self):
        """Indicates whether this country is a Besieged Regime"""
        return False

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
        return False

    def is_governed(self):
        return True

    def is_muslim(self):
        return False

    def is_regime_change(self):
        return False

    def is_shia_mix(self):
        return False

    def is_soft(self):
        return False

    def is_ungoverned(self):
        return False

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

    def _ought_to_have_been_tested(self):
        """Indicates whether this country ought to have been tested by now"""
        return self.sleeperCells > 0 or self.activeCells > 0 or self.troopCubes > 0 or self.cadre > 0 or self.plots > 0

    def has_data(self):
        """Indicates whether this country contains anything not printed on the board"""
        return self._ought_to_have_been_tested() or self.is_besieged() or self.markers

    def is_non_muslim(self):
        """Indicates whether this country is Non-Muslim (which is not the opposite of Muslim)"""
        return False

    def is_non_recruit_success(self, roll):
        """Indicates whether the given die roll is a success for the Jihadist (for non-recruiting actions)"""
        return self.is_governed() and self.__governance.is_success(roll)

    def is_recruit_success(self, roll, recruit_override=None):
        max_recruit_roll = self.max_recruit_roll(recruit_override)
        return max_recruit_roll is not None and roll <= max_recruit_roll

    def governance_is_better_than(self, governance):
        return self.__governance is not None and self.__governance.is_better_than(governance)

    def governance_is_worse_than(self, governance):
        return self.__governance is not None and self.__governance.is_worse_than(governance)

    def is_major_jihad_possible(self, _ignored_1, _ignored_2, _ignored_3):
        return False

    def can_disrupt(self):
        """Indicates whether the US can conduct a Disrupt operation in this country"""
        return (
            (self.total_cells() > 0 or self.has_cadre()) and
            (self.is_ally() or self.troops() >= 2 or self.is_non_muslim())
        )

    def can_have_posture(self):
        """Indicates whether this country can have a posture (excludes the US)"""
        return False

    def can_recruit(self, madrassas):
        return (self.total_cells(True) > 0 or
                self.has_cadre() or
                (madrassas and self.governance_is_worse_than(FAIR)))

    def get_disrupt_summary(self):
        return "%s - %d Active Cells, %d Sleeper Cells, %d Cadre, Ops Reqd %d, Troops: %d" %\
               (self.name, self.activeCells, self.sleeperCells, self.cadre, self.__governance.min_us_ops(),
                self.troops())

    def get_governance(self):
        return self.__governance

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

    def check_is_tested(self):
        """Asserts that this country has been tested (throws if not)"""
        pass

    def governance_str(self):
        if self.is_ungoverned():
            return "Untested"
        return str(self.__governance)

    def has_cadre(self):
        """Indicates whether this country contains any cadre"""
        return self.cadre > 0

    def print_country(self):
        """Prints a textual summary of this Country"""
        print self.summary()

    def set_governance(self, _):
        """Sets this country to have the given level of Governance (must not be None)"""
        raise Exception("Can't set the governance of %s" % self.name)

    def _do_set_governance(self, new_governance):
        self.__governance = Utils.require_type_or_none(new_governance, Governance)

    def summary(self):
        pass
