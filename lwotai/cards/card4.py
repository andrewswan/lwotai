from lwotai.cards.abstract_card import AbstractCard


class Card4(AbstractCard):

    def __init__(self):
        super(Card4, self).__init__(4, "US", "Moro Talks", 1, True, True, False)

    def play_event(self, side, app):
        app.markers.append("Moro Talks")
        app.markers.remove("Abu Sayyaf")
        app.output_to_history("Moro Talks in play.", False)
        app.test_country("Philippines")
        app.change_funding(-1)
