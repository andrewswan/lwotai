from lwotai.cards.abstract_card import AbstractCard


class Card6and7(AbstractCard):

    def __init__(self, number):
        super(Card6and7, self).__init__(number, "US", "Sanctions", 1, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Patriot Act" in app.markers

    def play_event(self, side, app):
        if "Patriot Act" in app.markers:
            app.change_funding(-2)
        else:
            return False
