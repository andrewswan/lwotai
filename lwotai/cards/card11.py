from lwotai.cards.us_card import USCard


class Card11(USCard):

    def __init__(self):
        super(Card11, self).__init__(11, "Abbas", 2, True, True, False)

    def play_event(self, side, app):
        islamist_rule_adjacent_to_israel = \
            app.contains_country(lambda c: app.is_adjacent(c.name, "Israel") and c.is_islamist_rule())
        app.markers.append("Abbas")
        app.output_to_history("Abbas in play.", False)
        if app.troops >= 5 and not islamist_rule_adjacent_to_israel:
            app.change_prestige(1, False)
            app.change_funding(-2, True)
