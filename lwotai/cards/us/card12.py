from lwotai.cards.us.us_card import USCard


class Card12(USCard):

    def __init__(self):
        super(Card12, self).__init__(12, "Al-Azhar", 2, False, False, False)

    def play_event(self, side, app):
        app.test_country("Egypt")
        funding_change = -2 if app.num_islamist_rule() else -4
        app.change_funding(funding_change, True)
