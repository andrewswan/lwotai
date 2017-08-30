from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card120(UnassociatedCard):

    def __init__(self):
        super(Card120, self).__init__(120, "US Election", 3, False, False, False, False)

    def do_play_event(self, side, app):
        posture_roll = app.roll_d6()
        if posture_roll <= 4:
            app.us().make_soft()
            app.output_to_history("United States Posture now Soft.", False)
        else:
            app.us().make_hard()
            app.output_to_history("United States Posture now Hard.", False)
        app.change_prestige(-1 if app.gwot_penalty() else 1)
