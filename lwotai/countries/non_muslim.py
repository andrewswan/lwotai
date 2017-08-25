from lwotai.countries.country import Country
from lwotai.postures.posture import HARD, SOFT
from lwotai.utils import Utils


class NonMuslimCountry(Country):
    """Does not include Iran"""

    def __init__(self, app, name, posture, governance, schengen, recruit=0, schengen_link=False):
        super(NonMuslimCountry, self).__init__(app, name, governance, schengen, recruit, False, 0, schengen_link)
        self.__posture = Utils.require_none_or_one_of(posture, [HARD, SOFT])

    def can_have_posture(self):
        """Indicates whether this country can have a posture (excludes the US)"""
        return self.name != "United States"

    def check_is_tested(self):
        """Asserts that this country has been tested (throws if not)"""
        if self._ought_to_have_been_tested():
            assert self.is_governed(), "Ungoverned country: %s" % self.print_country()
            assert self.__posture, "%s has no posture" % self.name

    def get_disrupt_summary(self):
        return "%s - %d Active Cells, %d Sleeper Cells, %d Cadre, Ops Reqd %d, Posture %s" %\
               (self.name, self.activeCells, self.sleeperCells, self.cadre, self.get_governance().min_us_ops(),
                self.__posture)

    def get_posture(self):
        return self.__posture

    def is_hard(self):
        return self.__posture == HARD

    def is_muslim(self):
        return False

    def is_iran(self):
        return False

    def is_non_muslim(self):
        return True

    def is_soft(self):
        return self.__posture == SOFT

    def make_hard(self):
        """Sets this country to Hard posture"""
        self.set_posture(HARD)

    def make_soft(self):
        """Sets this country to Soft posture"""
        self.set_posture(SOFT)

    def remove_posture(self):
        """Removes any posture from this country"""
        self.__posture = None

    def set_posture(self, new_posture):
        """Sets or clears the posture of this country"""
        self.__posture = Utils.require_none_or_one_of(new_posture, [HARD, SOFT])

    def toggle_posture(self):
        """Switches this country between Hard and Soft posture (error if no posture set)"""
        if self.is_hard():
            self.make_soft()
        elif self.is_soft():
            self.make_hard()
        else:
            raise Exception("%s has no posture" % self.name)

    def summary(self):
        """Returns a textual summary of this Country"""
        summary = "%s - Posture: %s\n    " % (self.name, self.__posture)
        item_strings = []
        if self.activeCells:
            item_strings.append("Active: %d" % self.activeCells)
        if self.sleeperCells:
            item_strings.append("Sleeper: %d" % self.sleeperCells)
        if self.cadre:
            item_strings.append("Cadre: %d" % self.cadre)
        if self.plots:
            item_strings.append("Plots: %d" % self.plots)
        if self.troopCubes:
            # We don't include NATO here, that's a marker
            item_strings.append("Troop cubes: %d" % self.troopCubes)
        if self.markers:
            item_strings.append("Markers: %s" % ", ".join(self.markers))
        if item_strings:
            summary += ", ".join(item_strings)
        else:
            summary += "Empty"
        return summary

    def test(self, test_roll):
        """Tests this country's posture, if not already set, using the given roll"""
        if not self.get_posture():
            if test_roll <= 4:
                self.make_soft()
            else:
                self.make_hard()
            self.app.output_to_history("%s tested, posture %s" % (self.name, self.get_posture()), False)
