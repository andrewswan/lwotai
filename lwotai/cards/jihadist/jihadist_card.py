from lwotai.cards.abstract_card import AbstractCard


class JihadistCard(AbstractCard):
    """A card with a Jihadist event"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell):
        super(JihadistCard, self).__init__(number, "Jihadist", name, ops, remove, mark, lapsing, puts_cell)

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
            return False
        return side != "US" and self._really_playable(side, app, ignore_itjihad)

    def play_event(self, side, app):
        super(JihadistCard, self).play_event(side, app)
        self.play_as_jihadist(app)

    def play_as_jihadist(self, app):
        """Subclasses to override"""
        pass
