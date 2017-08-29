import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card92(JihadistCard):

    def __init__(self):
        super(Card92, self).__init__(92, "Saddam", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        iraq = app.get_country("Iraq")
        return "Saddam Captured" not in app.markers and iraq.is_poor() and iraq.is_adversary()

    def play_as_jihadist(self, app):
        app.funding = 9
        app.output_to_history("Jihadist Funding now 9.")
