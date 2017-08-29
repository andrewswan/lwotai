from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card63(JihadistCard):

    def __init__(self):
        super(Card63, self).__init__(63, "Gaza War", 2, False, False, False, False)

    def play_as_jihadist(self, app):
        app.change_funding(1)
        app.change_prestige(-1)
        app.output_to_history("US discards a random card.")
