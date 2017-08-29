from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card54(JihadistCard):

    def __init__(self):
        super(Card54, self).__init__(54, "Moqtada al-Sadr", 1, True, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").troops() > 0

    def play_as_jihadist(self, app):
        app.get_country("Iraq").markers.append("Sadr")
        app.output_to_history("Sadr Marker added in Iraq", True)
