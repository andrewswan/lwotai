class Deck(object):
    """The deck of cards in the game"""

    def __init__(self, cards):
        self.cards = {}
        # Store the given list of cards in a dict, indexed by their number
        for card in cards:
            self.cards[card.number] = card

    def get(self, card_number):
        """Returns the card with the given number"""
        assert isinstance(card_number, int)
        card = self.cards[card_number]
        if not card:
            raise ValueError("Invalid card number %d" % card_number)
        return card
