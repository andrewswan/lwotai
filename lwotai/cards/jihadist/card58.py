from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card58(JihadistCard):

    def __init__(self):
        super(Card58, self).__init__(58, "Al-Anbar", 2, True, True, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Anbar Awakening" not in app.markers

    def play_as_jihadist(self, app):
        app.markers.append("Al-Anbar")
        app.output_to_history("Al-Anbar in play.", True)
        app.test_country("Iraq")
        if app.cells > 0:
            app.place_cell("Iraq")
