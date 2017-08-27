from lwotai.cards.abstract_card import AbstractCard


class Card16(AbstractCard):

    def __init__(self):
        super(Card16, self).__init__(16, "US", "Euro-Islam", 2, True, False, False)

    def play_event(self, side, app):
        benelux = app.get_country("Benelux")
        new_posture = app.get_posture_from_user("Select Benelux's Posture (hard or soft): ")
        benelux.set_posture(new_posture)
        if app.num_islamist_rule() == 0:
            app.change_funding(-1, False)
            app.output_to_history("Jihadist Funding now %d" % app.funding, False)
        app.output_to_history(benelux.summary())
