from lwotai.cards.card import Card


class AbstractCard(Card):
    """The class from which all card classes will ultimately inherit, to split up the long 'Card' class"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing, puts_cell=False):
        super(AbstractCard, self).__init__(number, card_type, name, ops, remove, mark, lapsing)
        self.__puts_cell = puts_cell

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        # Bypasses huge method in superclass
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        return self._really_playable(side, app, ignore_itjihad)

    def _really_playable(self, _side, _app, _ignore_itjihad):
        """Indicates whether this card is playable, assuming the side is valid"""
        return True

    def puts_cell(self):
        """Whether this card's event places a cell"""
        # Bypass huge method in superclass
        return self.__puts_cell

    def play_event(self, side, app):
        """Executes this card's event as the given side (US or Jihadist)"""
        app.output_to_history("Card played for Event.")
