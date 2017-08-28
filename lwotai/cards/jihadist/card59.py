from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card59(JihadistCard):

    def __init__(self):
        super(Card59, self).__init__(59, "Amerithrax", 2, False, False, False, False)

    def play_event(self, _side, app):
        app.output_to_history("US side discards its highest-value US-associated event card, if it has any.")
