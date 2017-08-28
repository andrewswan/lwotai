from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card77(JihadistCard):

    def __init__(self):
        super(Card77, self).__init__(77, "Al Jazeera", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if app.get_country("Saudi Arabia").troops() > 0:
            return True
        return app.contains_country(lambda c: app.is_adjacent("Saudi Arabia", c.name) and c.troops() > 0)

    def play_event(self, _side, app):
        choices = app.minor_jihad_in_good_fair_choice(1, False, True)
        if choices:
            target = app.get_country(choices[0][0])
            if target.is_ally():
                target.make_neutral()
            elif target.is_neutral():
                target.make_adversary()
            app.output_to_history("%s Alignment shifted to %s." % (target.name, target.alignment()))
        else:
            app.output_to_history("No countries to shift.")
