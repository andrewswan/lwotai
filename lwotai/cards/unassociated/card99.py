import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card99(UnassociatedCard):

    def __init__(self):
        super(Card99, self).__init__(99, "HAMAS Elected", 1, True, False, False, False)

    def play_event(self, side, app):
        app.output_to_history("US selects and discards one card.", False)
        app.change_prestige(-1)
        app.change_funding(-1)
