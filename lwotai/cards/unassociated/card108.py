import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card108(UnassociatedCard):

    def __init__(self):
        super(Card108, self).__init__(108, "Musharraf", 2, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Benazir Bhutto" not in app.markers and app.get_country("Pakistan").total_cells() > 0

    def play_event(self, side, app):
        app.remove_cell("Pakistan", side)    # 20150131PS added side
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_ally()
        app.output_to_history("Pakistan now Poor Ally.", False)
        app.output_to_history(app.get_country("Pakistan").summary(), True)
