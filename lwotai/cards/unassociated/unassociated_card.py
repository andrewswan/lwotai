from lwotai.cards.abstract_card import AbstractCard


class UnassociatedCard(AbstractCard):
    """A card whose event is not associated with either side"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell):
        super(UnassociatedCard, self).__init__(number, "Unassociated", name, ops, remove, mark, lapsing, puts_cell)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return True

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
            return False
        return self._really_playable(side, app, ignore_itjihad)
