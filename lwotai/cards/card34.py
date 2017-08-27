from lwotai.cards.abstract_card import AbstractCard


class Card34(AbstractCard):

    def __init__(self):
        super(Card34, self).__init__(34, "US", "Enhanced Measures", 3, False, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if "Leak-Enhanced Measures" in app.markers or app.us().is_soft():
            return False
        return app.num_disruptable() > 0

    def play_event(self, side, app):
        app.markers.append("Enhanced Measures")
        app.output_to_history("Enhanced Measures in Play.", False)
        app.output_to_history("Take a random card from the Jihadist hand.", False)
        app.disrupt_cells_or_cadre()
        app.output_to_history("", False)
