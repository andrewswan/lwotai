from lwotai.cards.us.us_card import USCard


class Card42(USCard):

    def __init__(self):
        super(Card42, self).__init__(42, "Pakistani Offensive", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        pakistan = app.get_country("Pakistan")
        return pakistan.is_ally() and "FATA" in pakistan.markers

    def play_as_us(self, app):
        if "FATA" in app.get_country("Pakistan").markers:
            app.get_country("Pakistan").markers.remove("FATA")
            app.output_to_history("FATA removed from Pakistan", True)
