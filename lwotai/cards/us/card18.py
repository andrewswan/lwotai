from lwotai.cards.us.us_card import USCard


class Card18(USCard):

    def __init__(self):
        super(Card18, self).__init__(18, "Intel Community", 2, False, False, False)

    def play_as_us(self, app):
        app.output_to_history("Examine Jihadist hand. Do not change order of cards.", False)
        app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment,"
                              " regime_change, withdraw, or war_of_ideas).", False)
        app.output_to_history(
            "You may now interrupt this action phase to play another card (Use the u command).", True)
