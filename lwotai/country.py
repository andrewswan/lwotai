from lwotai.alignment import ALLY, NEUTRAL, ADVERSARY
from lwotai.governance import GOOD, FAIR, POOR, ISLAMIST_RULE
from lwotai.governance import Governance
from lwotai.utils import Utils


class Country(object):
    """A country on the map"""
    __alignment = None
    __governance = None
    app = None
    name = ""
    type = ""
    posture = ""
    schengen = False
    recruit = 0
    troopCubes = 0
    activeCells = 0
    sleeperCells = 0
    oil = False
    resources = 0
    links = []
    markers = []
    schengenLink = False
    aid = 0
    besieged = 0    #20150131PS - fixed spelling
    regimeChange = 0
    cadre = 0
    plots = 0

    def __init__(self, theApp, theName, theType, thePosture, theGovernance, theSchengen, theRecruit, no1, no2, no3, theOil, theResources):
        self.app = theApp
        self.name = theName
        self.type = theType
        self.posture = thePosture
        self.make_governance(theGovernance)
        self.schengen = theSchengen
        self.recruit = theRecruit
        self.troopCubes = 0
        self.activeCells = 0
        self.sleeperCells = 0
        self.oil = theOil
        self.resources = theResources
        self.aid = 0
        self.besieged = 0
        self.regimeChange = 0
        self.cadre = 0
        self.plots = 0
        self.links = []
        self.markers = []
        self.schengenLink = False

    def alignment(self):
        return self.__alignment

    def is_adversary(self):
        return self.__alignment == ADVERSARY

    def is_ally(self):
        return self.__alignment == ALLY

    def is_neutral(self):
        return self.__alignment == NEUTRAL

    def is_aligned(self):
        return self.__alignment is not None

    def is_unaligned(self):
        return self.__alignment is None

    def make_adversary(self):
        self.__alignment = ADVERSARY

    def make_ally(self):
        self.__alignment = ALLY

    def make_neutral(self):
        self.__alignment = NEUTRAL

    def is_good(self):
        return self.__governance == GOOD

    def is_fair(self):
        return self.__governance == FAIR

    def is_poor(self):
        return self.__governance == POOR

    def is_islamist_rule(self):
        return self.__governance == ISLAMIST_RULE

    def is_governed(self):
        return self.__governance is not None

    def is_ungoverned(self):
        return not self.is_governed()

    def make_good(self):
        self.__governance = GOOD

    def make_fair(self):
        self.__governance = FAIR

    def make_poor(self):
        self.__governance = POOR

    def make_islamist_rule(self):
        self.__governance = ISLAMIST_RULE

    def make_ungoverned(self):
        self.__governance = None

    def make_governance(self, governance):
        self.__governance = Utils.require_type_or_none(governance, Governance)

    def make_hard(self):
        """Sets a Non-Muslim country to Hard posture"""
        if self.type == "Non-Muslim":
            self.posture = "Hard"

    def make_soft(self):
        """Sets a Non-Muslim country to Soft posture"""
        if self.type == "Non-Muslim":
            self.posture = "Soft"

    def remove_posture(self):
        """Removes any posture from a Non-Muslim country"""
        if self.type == "Non-Muslim":
            self.posture = ""

    def remove_plot_marker(self):
        """Removes one plot marker from this country, if any are present"""
        if self.plots > 0:
            self.plots -= 1

    def check_is_tested(self):
        if self._ought_to_have_been_tested():
            assert self.is_governed(), "Ungoverned country: %s" % self.printCountry()
            if self.type == "Non-Muslim":
                assert self.posture != "", "%s has no posture" % self.name
            elif self.type != "Iran":
                assert self.is_aligned(), "%s is unaligned" % self.name

    def _ought_to_have_been_tested(self):
        """Indicates whether this country ought to have been tested by now"""
        return self.sleeperCells > 0 or self.activeCells > 0 or \
               self.troopCubes > 0 or self.aid > 0 or \
               self.regimeChange > 0 or self.cadre > 0 or \
               self.plots > 0

    def is_non_recruit_success(self, roll):
        return self.is_governed() and self.__governance.is_success(roll)

    def is_recruit_success(self, roll, recruit_override = None):
        max_recruit_roll = self.max_recruit_roll(recruit_override)
        return max_recruit_roll is not None and roll <= max_recruit_roll

    def improve_governance(self):
        self.__governance = self.__governance.improve()
        if self.is_good():
            self.regimeChange = 0
            self.aid = 0
            self.besieged = 0

    def worsenGovernance(self):
        self.__governance = self.__governance.worsen()

    def governance_is_better_than(self, governance):
        return self.__governance is not None and self.__governance.is_better_than(governance)

    def governance_is_worse_than(self, governance):
        return self.__governance is not None and self.__governance.is_worse_than(governance)

    def is_muslim(self):
        return self.type == "Suni" or self.type == "Shia-Mix"

    def is_major_jihad_possible(self, ops, excess_cells_needed, bhutto_in_play):
        if self.is_islamist_rule():
            return False
        if not self.is_muslim():
            return False
        if bhutto_in_play and self.name == "Pakistan":
            return False
        if self.totalCells(True) - self.troops() < excess_cells_needed:
            return False
        ops_needed_from_poor = 1 if self.besieged else 2
        ops_needed = ops_needed_from_poor + self.__governance.levels_above_poor()
        return ops >= ops_needed

    def can_recruit(self, madrassas):
        return (self.totalCells(True) > 0 or
                self.has_cadre() or
                (madrassas and self.governance_is_worse_than(FAIR)))

    def is_regime_change(self):
        return self.regimeChange > 0

    def can_disrupt(self):
        """Indicates whether the US can conduct a Disrupt operation in this country"""
        return (
            (self.totalCells() > 0 or self.has_cadre()) and
            (self.is_ally() or self.troops() >= 2 or self.type == "Non-Muslim")
        )

    def get_disrupt_summary(self):
        postureStr = ""
        troopsStr = ""
        if self.type == "Non-Muslim":
            postureStr = ", Posture %s" % self.posture
        else:
            troopsStr = ", Troops: %d" % self.troops()
        return "%s - %d Active Cells, %d Sleeper Cells, %d Cadre, Ops Reqd %d%s%s" % (self.name, self.activeCells,
                                                                                      self.sleeperCells, self.cadre, self.__governance.min_us_ops(), troopsStr, postureStr)

    def max_recruit_roll(self, recruit_override = None):
        if recruit_override:
            return recruit_override
        if self.recruit > 0:
            return self.recruit
        if self.is_governed():
            return self.__governance.max_success_roll()
        return None

    def governance_as_funding(self):
        return self.__governance.max_success_roll()

    def get_recruit_score(self, ops):
        if self.is_regime_change() and self.troops() - self.totalCells(True) >= 5:
            return 100000000
        if self.is_islamist_rule() and self.totalCells(True) < 2 * ops:
            return 10000000
        if not self.is_islamist_rule() and not self.is_regime_change():
            return self.max_recruit_roll() * 1000000
        return None

    def totalCells(self, includeSadr = False):
        total = self.activeCells + self.sleeperCells
        if includeSadr and "Sadr" in self.markers:
            total += 1
        return total

    def numActiveCells(self):
        total = self.activeCells
        if "Sadr" in self.markers:
            total += 1
        return total

    def reduce_aid_by(self, aid_lost):
        """Reduces the level of aid by the given amount, but not below zero"""
        self.aid = max(self.aid - aid_lost, 0)

    def removeActiveCell(self):
        self.activeCells -= 1
        if self.activeCells < 0:        #20150131PS - changed from <= to <
            if "Sadr" in self.markers:
                self.markers.remove("Sadr")
                self.app.outputToHistory("Sadr removed from %s" % self.name, False)
                self.activeCells = 0    # 20150131PS - added
                return
            else:
                self.activeCells = 0
        self.app.outputToHistory("Active cell Removed to Funding Track", False)
        self.app.cells += 1

    def troops(self):
        troopCount = self.troopCubes
        if "NATO" in self.markers:
            troopCount += 2
        return troopCount

    def changeTroops(self, delta):
        self.troopCubes += delta
        if self.troopCubes < 0:
            if "NATO" in self.markers:
                self.markers.remove("NATO")
                self.app.outputToHistory("NATO removed from %s" % self.name, True)
            self.troopCubes = 0

    def govStr(self):
        if self.is_ungoverned():
            return "Untested"
        return str(self.__governance)

    def has_cadre(self):
        """Indicates whether this country contains any cadre"""
        return self.cadre > 0

    @staticmethod
    def typePretty(theType):
        if theType == "Non-Muslim":
            return "NM"
        elif theType == "Suni":
            return "SU"
        elif theType == "Shia-Mix":
            return "SM"
        else:
            return "IR"

    def countryStr(self):
        markersStr = ""
        if len(self.markers) != 0:
            markersStr = "\n   Markers: %s" % ", ".join(self.markers)
        if self.type == "Shia-Mix" or self.type == "Suni":
            return "%s, %s %s, %d Resource(s)\n   Troops:%d Active:%d Sleeper:%d Cadre:%d Aid:%d Besieged:%d Reg Ch:%d Plots:%d %s" % (self.name, self.govStr(), self.__alignment, self.app.countryResources(self.name), self.troops(), self.activeCells, self.sleeperCells, self.cadre, self.aid, self.besieged, self.regimeChange, self.plots, markersStr)
        elif self.name == "Philippines":
            return "%s - Posture:%s\n   Troops:%d Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.posture, self.troops(), self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)
        elif self.type == "Non-Muslim" and self.type != "United States":    # 20150131PS This is illogical but does no harm
            return "%s - Posture:%s\n   Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.posture, self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)
        elif self.type == "Iran":
            return "%s, %s\n   Active:%d Sleeper:%d Cadre:%d Plots:%d %s" % (self.name, self.govStr(), self.activeCells, self.sleeperCells, self.cadre, self.plots, markersStr)

    def printCountry(self):
        print self.countryStr()

