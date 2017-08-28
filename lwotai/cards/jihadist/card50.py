import random

from cards.jihadist.jihadist_card import JihadistCard
from lwotai.governance import GOOD


class Card50(JihadistCard):

    def __init__(self):
        super(Card50, self).__init__(50, "Ansar al-Islam", 1, True, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").governance_is_worse_than(GOOD)

    def play_event(self, side, app):
        possible = ["Iraq", "Iran"]
        target_name = random.choice(possible)
        app.place_cells(target_name, 1)
