from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card60(JihadistCard):

    def __init__(self):
        super(Card60, self).__init__(60, "Bhutto Shot", 2, True, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Pakistan").total_cells() > 0

    def play_as_jihadist(self, app):
        app.markers.append("Bhutto Shot")
        app.output_to_history("Bhutto Shot in play.")
