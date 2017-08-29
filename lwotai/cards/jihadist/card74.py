from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card74(JihadistCard):

    def __init__(self):
        super(Card74, self).__init__(74, "Schengen Visas", 2, False, False, False, False)

    def play_as_jihadist(self, app):
        if app.cells == 15:
            app.output_to_history("No cells to travel.", False)
        else:
            app.handle_travel(2, False, True)
