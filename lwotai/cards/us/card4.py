from lwotai.cards.us.us_card import USCard


class Card4(USCard):

    def __init__(self):
        super(Card4, self).__init__(4, "Moro Talks", 1, True, True, False)

    def play_as_us(self, app):
        app.markers.append("Moro Talks")
        app.markers.remove("Abu Sayyaf")
        app.output_to_history("Moro Talks in play.", False)
        app.test_country("Philippines")
        app.change_funding(-1)
