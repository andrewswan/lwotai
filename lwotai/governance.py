from lwotai.utils import Utils


class Governance(object):
    """The governance level of a country"""
    def __init__(self, name, max_success_roll, levels_above_poor):
        self.__levels_above_poor = levels_above_poor
        self.__max_success_roll = Utils.require_type(max_success_roll, int)
        self.__name = Utils.require_type(name, str)
        self.__next_better = None
        self.__next_worse = None

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.name() == self.__name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Governance("{}", {}, {})'.format(self.__name, self.__max_success_roll, self.__levels_above_poor)

    def __str__(self):
        return self.__name

    def max_success_roll(self):
        return self.__max_success_roll

    def name(self):
        return self.__name

    def __hash__(self):
        return self.max_success_roll()

    def is_success(self, roll):
        return roll <= self.max_success_roll()

    def set_next_better_and_worse(self, next_better, next_worse):
        self.__next_better = Utils.require_type_or_none(next_better, Governance)
        self.__next_worse = Utils.require_type_or_none(next_worse, Governance)

    def improve(self):
        if self.__next_better is None:
            return self
        return self.__next_better

    def worsen(self):
        if self.__next_worse is None:
            return self
        return self.__next_worse

    def is_better_than(self, other):
        return self.__max_success_roll < other.max_success_roll()

    def is_worse_than(self, other):
        return self.__max_success_roll > other.max_success_roll()

    def levels_above_poor(self):
        return self.__levels_above_poor

    def min_us_ops(self):
        return self.__max_success_roll


# The possible Governances (or None)
GOOD = Governance("Good", 1, 2)
FAIR = Governance("Fair", 2, 1)
POOR = Governance("Poor", 3, 0)
ISLAMIST_RULE = Governance("Islamist Rule", 4, -1)

# The relative values of governances
GOOD.set_next_better_and_worse(None, FAIR)
FAIR.set_next_better_and_worse(GOOD, POOR)
POOR.set_next_better_and_worse(FAIR, None)  # Islamist Rule requires revolution


def governance_with_level(level):
    """Returns the governance of the given level"""
    if level == 0:
        return None
    elif level == 1:
        return GOOD
    elif level == 2:
        return FAIR
    elif level == 3:
        return POOR
    elif level == 4:
        return ISLAMIST_RULE
    raise ValueError('No such governance level "%d"' % level)
