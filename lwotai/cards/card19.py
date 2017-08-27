from lwotai.cards.abstract_card import AbstractCard


class Card19(AbstractCard):

    def __init__(self):
        super(Card19, self).__init__(19, "US", "Kemalist Republic", 2, False, False, False)

    def play_event(self, side, app):
        app.output_to_history("Turkey now a Fair Ally.", False)
        app.get_country("Turkey").make_fair()
        app.get_country("Turkey").make_ally()
        app.output_to_history(app.get_country("Turkey").summary(), True)
