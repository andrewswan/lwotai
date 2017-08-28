from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card57(JihadistCard):

    def __init__(self):
        super(Card57, self).__init__(57, "Abu Sayyaf", 2, True, True, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Moro Talks" not in app.markers

    def play_event(self, _side, app):
        app.place_cells("Philippines", 1)
        app.markers.append("Abu Sayyaf")
