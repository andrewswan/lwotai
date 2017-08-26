from lwotai.cards.abstract_card import AbstractCard


class Card2(AbstractCard):

    def __init__(self):
        super(Card2, self).__init__(2, "US", "Biometrics", 1, False, False, True)

    def play_event(self, side, app):
        app.lapsing.append("Biometrics")
        app.output_to_history("Biometrics in play. This turn, travel to adjacent Good countries must roll to"
                              " succeed and no non-adjacent travel.", True)
