from lwotai.cards.us.us_card import USCard


class Card20(USCard):

    def __init__(self):
        super(Card20, self).__init__(20, "King Abdullah", 2, True, False, False)

    def play_event(self, side, app):
        app.output_to_history("Jordan now a Fair Ally.", False)
        app.get_country("Jordan").make_fair()
        app.get_country("Jordan").make_ally()
        app.output_to_history(app.get_country("Jordan").summary(), True)
        app.change_prestige(1)
        app.change_funding(-1)
