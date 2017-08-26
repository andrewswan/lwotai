from lwotai.cards.abstract_card import AbstractCard


class Card12(AbstractCard):

    def __init__(self):
        super(Card12, self).__init__(12, "US", "Al-Azhar", 2, False, False, False)

    def play_event(self, side, app):
        app.test_country("Egypt")
        funding_change = -2 if app.num_islamist_rule() else -4
        app.change_funding(funding_change, True)
