from cards.jihadist.jihadist_card import JihadistCard


class Card49(JihadistCard):

    def __init__(self):
        super(Card49, self).__init__(49, "Al-Ittihad al-Islami", 1, True, False, False, True)

    def play_event(self, side, app):
        app.place_cells("Somalia", 1)
