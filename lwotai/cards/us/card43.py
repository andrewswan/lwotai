from lwotai.cards.us.us_card import USCard


class Card43(USCard):

    def __init__(self):
        super(Card43, self).__init__(43, "Patriot Act", 3, True, True, False)

    def play_event(self, side, app):
        app.markers.append("Patriot Act")
