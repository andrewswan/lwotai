from lwotai.cards.us.us_card import USCard


class Card19(USCard):

    def __init__(self):
        super(Card19, self).__init__(19, "Kemalist Republic", 2, False, False, False)

    def play_as_us(self, app):
        app.output_to_history("Turkey now a Fair Ally.", False)
        app.get_country("Turkey").make_fair()
        app.get_country("Turkey").make_ally()
        app.output_to_history(app.get_country("Turkey").summary(), True)
