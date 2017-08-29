import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card93(JihadistCard):

    def __init__(self):
        super(Card93, self).__init__(93, "Taliban", 3, False, False, False, True)

    def play_event(self, _side, app):
        app.test_country("Afghanistan")
        app.get_country("Afghanistan").make_besieged()
        app.output_to_history("Afghanistan is now a Besieged Regime.", False)
        app.place_cells("Afghanistan", 1)
        app.place_cells("Pakistan", 1)
        if app.get_country("Afghanistan").is_islamist_rule() or app.get_country("Pakistan").is_islamist_rule():
            app.change_prestige(-3)
        else:
            app.change_prestige(-1)
