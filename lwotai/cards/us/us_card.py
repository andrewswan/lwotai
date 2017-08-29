from lwotai.cards.abstract_card import AbstractCard


class USCard(AbstractCard):
    """A card with a US event"""

    def __init__(self, number, name, ops, remove, mark, lapsing):
        super(USCard, self).__init__(number, "US", name, ops, remove, mark, lapsing, False)

    def playable(self, side, app, ignore_itjihad):
        return side != "Jihadist" and self._really_playable(side, app, ignore_itjihad)

    def play_event(self, side, app):
        super(USCard, self).play_event(side, app)
        self.play_as_us(app)

    def play_as_us(self, app):
        """Subclasses to override"""
        pass
