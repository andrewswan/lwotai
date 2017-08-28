from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card79(JihadistCard):

    def __init__(self):
        super(Card79, self).__init__(79, "Clean Operatives", 3, False, False, False, False)

    def play_event(self, _side, app):
        app.handle_travel(2, False, False, True)
