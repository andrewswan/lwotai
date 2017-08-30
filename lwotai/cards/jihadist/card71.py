import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card71(JihadistCard):

    def __init__(self):
        super(Card71, self).__init__(71, "Loose Nuke", 2, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        russia = app.get_country("Russia")
        return russia.total_cells() > 0 and "CTR" not in russia.markers

    def play_as_jihadist(self, app):
        roll = app.roll_d6()
        app.execute_card_heu("Russia", roll)  # TODO rename method to get_wmd or similar
