from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card100(UnassociatedCard):

    def __init__(self):
        super(Card100, self).__init__(100, "Hizb Ut-Tahrir", 1, False, False, False, False)

    def play_event(self, side, app):
        if app.troops >= 10:
            app.change_funding(-2)
        elif app.troops < 5:
            app.change_funding(2)
