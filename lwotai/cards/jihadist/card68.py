from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card68(JihadistCard):

    def __init__(self):
        super(Card68, self).__init__(68, "Jemaah Islamiya", 2, False, False, False, True)

    def play_as_jihadist(self, app):
        app.place_cells("Indonesia/Malaysia", 2)
