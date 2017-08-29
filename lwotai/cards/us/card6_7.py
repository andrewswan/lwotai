from lwotai.cards.us.us_card import USCard


class Card6and7(USCard):

    def __init__(self, number):
        super(Card6and7, self).__init__(number, "Sanctions", 1, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Patriot Act" in app.markers

    def play_as_us(self, app):
        if "Patriot Act" in app.markers:
            app.change_funding(-2)
        else:
            return False
