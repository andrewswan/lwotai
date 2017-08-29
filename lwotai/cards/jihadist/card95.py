from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card95(JihadistCard):

    def __init__(self):
        super(Card95, self).__init__(95, "Wahhabism", 3, False, False, False, False)

    def play_as_jihadist(self, app):
        if app.get_country("Saudi Arabia").is_islamist_rule():
            app.change_funding(9)
        else:
            app.change_funding(app.get_country("Saudi Arabia").governance_as_funding())
