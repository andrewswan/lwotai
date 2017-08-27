from lwotai.cards.abstract_card import AbstractCard


class Card42(AbstractCard):

    def __init__(self):
        super(Card42, self).__init__(42, "US", "Pakistani Offensive", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        pakistan = app.get_country("Pakistan")
        return pakistan.is_ally() and "FATA" in pakistan.markers

    def play_event(self, side, app):
        if "FATA" in app.get_country("Pakistan").markers:
            app.get_country("Pakistan").markers.remove("FATA")
            app.output_to_history("FATA removed from Pakistan", True)
