from lwotai.card import Card


class AbstractCard(Card):
    """The class from which all card classes will ultimately inherit, to split up the long 'Card' class"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing):
        super(AbstractCard, self).__init__(number, card_type, name, ops, remove, mark, lapsing)

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        return True  # Bypass huge method in superclass

    def puts_cell(self):
        """Whether this card's event places a cell"""
        return False  # Bypass huge method in superclass

    def play_event(self, side, app):
        """Executes this card's event as the given side (US or Jihadist)"""
        pass  # Bypass huge method in superclass
