import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card91(JihadistCard):

    def __init__(self):
        super(Card91, self).__init__(91, "Regional al-Qaeda", 3, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        targets = app.find_countries(lambda c: c.is_muslim() and c.is_ungoverned())
        return len(targets) >= 2

    def play_event(self, _side, app):
        possibles = app.find_countries(lambda c: c.is_muslim() and c.is_ungoverned())
        random.shuffle(possibles)
        cells_to_place = 2 if app.num_islamist_rule() > 0 else 1
        app.place_cells(possibles[0].name, cells_to_place)
        app.place_cells(possibles[1].name, cells_to_place)
