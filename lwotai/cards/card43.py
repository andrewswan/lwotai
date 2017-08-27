from lwotai.cards.abstract_card import AbstractCard


class Card43(AbstractCard):

    def __init__(self):
        super(Card43, self).__init__(43, "US", "Patriot Act", 3, True, True, False)

    def play_event(self, side, app):
        app.markers.append("Patriot Act")
