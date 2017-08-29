import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card98(UnassociatedCard):

    def __init__(self):
        super(Card98, self).__init__(98, "Gaza Withdrawal", 1, True, False, False, True)

    def do_play_event(self, side, app):
        if side == "US":
            app.change_funding(-1)
        else:
            app.place_cells("Israel", 1)
