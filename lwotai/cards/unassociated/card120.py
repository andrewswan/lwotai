from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card120(UnassociatedCard):

    def __init__(self):
        super(Card120, self).__init__(120, "US Election", 3, False, False, False, False)

    def do_play_event(self, side, app):
        app.execute_card_us_election()
