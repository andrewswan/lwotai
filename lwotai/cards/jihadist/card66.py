from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card66(JihadistCard):

    def __init__(self):
        super(Card66, self).__init__(66, "Homegrown", 2, False, False, False, True)

    def play_event(self, _side, app):
        app.place_cells("United Kingdom", 1)
