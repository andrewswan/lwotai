from lwotai.cards.card import Card


class UnassociatedCard(Card):
    """A card whose event is not associated with either side"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell):
        super(UnassociatedCard, self).__init__(number, "Unassociated", name, ops, remove, mark, lapsing, puts_cell)
