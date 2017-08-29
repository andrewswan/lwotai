from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card113(UnassociatedCard):

    def __init__(self):
        super(Card113, self).__init__(113, "Darfur", 3, False, False, False, False)

    def play_event(self, side, app):
        app.test_country("Sudan")
        sudan = app.get_country("Sudan")
        if app.prestige >= 7:
            sudan.add_aid(1)
            app.output_to_history("Aid added to Sudan.", False)
            if sudan.is_adversary():
                sudan.make_neutral()
                app.output_to_history("Sudan alignment improved.", False)
            elif sudan.is_neutral():
                sudan.make_ally()
                app.output_to_history("Sudan alignment improved.", False)
        else:
            sudan.make_besieged()
            app.output_to_history("Sudan now Besieged Regime.", False)
            if sudan.is_ally():
                sudan.make_neutral()
                app.output_to_history("Sudan alignment worsened.", False)
            elif sudan.is_neutral():
                sudan.make_adversary()
                app.output_to_history("Sudan alignment worsened.", False)
        app.output_to_history(sudan.summary(), True)
