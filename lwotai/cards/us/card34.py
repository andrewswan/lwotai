from lwotai.cards.us.us_card import USCard


class Card34(USCard):

    def __init__(self):
        super(Card34, self).__init__(34, "Enhanced Measures", 3, False, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if "Leak-Enhanced Measures" in app.markers or app.us().is_soft():
            return False
        return app.num_disruptable() > 0

    def play_as_us(self, app):
        app.markers.append("Enhanced Measures")
        app.output_to_history("Enhanced Measures in Play.", False)
        app.output_to_history("Take a random card from the Jihadist hand.", False)
        app.disrupt_cells_or_cadre()
        app.output_to_history("", False)
