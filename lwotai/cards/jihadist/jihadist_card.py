from lwotai.cards.card import Card


class JihadistCard(Card):
    """A card with a Jihadist event"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell):
        super(JihadistCard, self).__init__(number, "Jihadist", name, ops, remove, mark, lapsing, puts_cell)

    def do_play_event(self, side, app):
        """The event on Jihadist cards can be played only by the Jihadist player"""
        self.play_as_jihadist(app)

    def play_as_jihadist(self, app):
        """Subclasses to override"""
        pass
