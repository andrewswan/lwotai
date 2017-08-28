from lwotai.cards.abstract_card import AbstractCard


class JihadistCard(AbstractCard):
    """A card with a Jihadist event"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell):
        super(JihadistCard, self).__init__(number, "Jihadist", name, ops, remove, mark, lapsing, puts_cell)
