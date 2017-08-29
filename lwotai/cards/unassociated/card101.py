from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card101(UnassociatedCard):

    def __init__(self):
        super(Card101, self).__init__(101, "Kosovo", 1, False, False, False, False)

    def play_event(self, side, app):
        app.change_prestige(1)
        app.test_country("Serbia")
        serbia = app.get_country("Serbia")
        if app.us().is_soft():
            serbia.make_hard()
        else:
            serbia.make_soft()
        app.output_to_history("Serbia Posture now %s." % app.get_posture("Serbia"), True)
