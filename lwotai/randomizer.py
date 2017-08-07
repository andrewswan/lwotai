import random


class Randomizer(object):
    """Picks things at random. To make tests repeatable, mock this out."""
    def __init__(self):
        pass

    def pick(self, quantity, candidates):
        """Picks the given quantity of items from the given list of candidates (returns a list)"""
        assert quantity <= len(candidates)
        new_list = list(candidates)
        random.shuffle(new_list)
        return new_list[0:quantity]

    def pick_one(self, candidates):
        """Picks the one item from the given list of candidates (returns the item)"""
        return self.pick(1, candidates)[0]

    def roll_d6(self, times):
        """Returns the result of rolling a six-sided die the given number of
        times (returns a list of that size containing numbers from 1 to 6)"""
        return [self.pick_one(range(1, 7)) for _ in range(times)]
