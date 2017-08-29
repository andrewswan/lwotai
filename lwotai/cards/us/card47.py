from lwotai.cards.us.us_card import USCard


class Card47(USCard):

    def __init__(self):
        super(Card47, self).__init__(47, "The door of Itjihad was closed", 3, False, False, True)

    def play_as_us(self, app):
        app.lapsing.append("The door of Itjihad was closed")
