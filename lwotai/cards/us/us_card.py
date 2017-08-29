from lwotai.cards.card import Card


class USCard(Card):
    """A card with a US event"""

    def __init__(self, number, name, ops, remove, mark, lapsing):
        super(USCard, self).__init__(number, "US", name, ops, remove, mark, lapsing)

    def do_play_event(self, _side, app):
        """The event on US cards can be played only by the US player"""
        self.play_as_us(app)

    def play_as_us(self, app):
        """Subclasses to override"""
        pass
