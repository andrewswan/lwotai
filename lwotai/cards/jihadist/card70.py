from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card70(JihadistCard):

    def __init__(self):
        super(Card70, self).__init__(70, "Lashkar-e-Tayyiba", 2, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Indo-Pakistani Talks" not in app.markers

    def play_event(self, _side, app):
        app.place_cells("Pakistan", 1)
        if app.cells > 0:
            app.place_cells("India", 1)
