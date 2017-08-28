from lwotai.cards.abstract_card import AbstractCard


class Card47(AbstractCard):

    def __init__(self):
        super(Card47, self).__init__(47, "US", "The door of Itjihad was closed", 3, False, False, True)

    def play_event(self, side, app):
        app.lapsing.append("The door of Itjihad was closed")
