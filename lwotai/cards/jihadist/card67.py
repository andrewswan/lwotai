from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card67(JihadistCard):

    def __init__(self):
        super(Card67, self).__init__(67, "Islamic Jihad Union", 2, True, False, False, True)

    def play_event(self, _side, app):
        app.place_cells("Central Asia", 1)
        if app.cells > 0:
            app.place_cells("Afghanistan", 1)
