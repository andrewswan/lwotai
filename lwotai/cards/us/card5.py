from lwotai.cards.us.us_card import USCard


class Card5(USCard):

    def __init__(self):
        super(Card5, self).__init__(5, "NEST", 1, True, True, False)

    def play_as_us(self, app):
        app.markers.append("NEST")
        app.output_to_history("NEST in play. If jihadists have WMD, all plots in the US placed face up.")
