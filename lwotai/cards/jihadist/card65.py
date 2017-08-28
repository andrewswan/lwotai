import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card65(JihadistCard):

    def __init__(self):
        super(Card65, self).__init__(65, "HEU", 2, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        russia = app.get_country("Russia")
        if russia.total_cells() > 0 and "CTR" not in russia.markers:
            return True
        central_asia = app.get_country("Central Asia")
        return central_asia.total_cells() > 0 and "CTR" not in central_asia.markers

    def play_event(self, _side, app):
        possibles = []
        russia = app.get_country("Russia")
        if russia.total_cells() > 0 and "CTR" not in russia.markers:
            possibles.append("Russia")
        central_asia = app.get_country("Central Asia")
        if central_asia.total_cells() > 0 and "CTR" not in central_asia.markers:
            possibles.append("Central Asia")
        target_name = random.choice(possibles)
        roll = random.randint(1, 6)
        app.execute_card_heu(target_name, roll)
