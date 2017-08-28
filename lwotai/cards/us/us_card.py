from lwotai.cards.abstract_card import AbstractCard


class USCard(AbstractCard):
    """A card with a US event"""

    def __init__(self, number, name, ops, remove, mark, lapsing):
        super(USCard, self).__init__(number, "US", name, ops, remove, mark, lapsing, False)
