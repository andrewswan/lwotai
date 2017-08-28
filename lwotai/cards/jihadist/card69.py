import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card69(JihadistCard):

    def __init__(self):
        super(Card69, self).__init__(69, "Kazakh Strain", 2, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        central_asia = app.get_country("Central Asia")
        return central_asia.total_cells() > 0 and "CTR" not in central_asia.markers

    def play_event(self, _side, app):
        roll = random.randint(1, 6)
        app.execute_card_heu("Central Asia", roll)
