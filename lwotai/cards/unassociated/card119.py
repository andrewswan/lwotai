from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card119(UnassociatedCard):

    def __init__(self):
        super(Card119, self).__init__(119, "Saleh", 3, False, False, False, False)

    def play_event(self, side, app):
        app.test_country("Yemen")
        yemen = app.get_country("Yemen")
        if side == "US":
            if not yemen.is_islamist_rule():
                if yemen.is_adversary():
                    yemen.make_neutral()
                elif yemen.is_neutral():
                    yemen.make_ally()
                app.output_to_history("Yemen Alignment improved to %s." % yemen.alignment(), False)
                yemen.add_aid(1)
                app.output_to_history("Aid added to Yemen.")
        else:
            if yemen.is_ally():
                yemen.make_neutral()
            elif yemen.is_neutral():
                yemen.make_adversary()
            app.output_to_history("Yemen Alignment worsened to %s." % yemen.alignment(), False)
            yemen.make_besieged()
            app.output_to_history("Yemen now Besieged Regime.")
