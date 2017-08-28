from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card76(JihadistCard):

    def __init__(self):
        super(Card76, self).__init__(76, "Abu Ghurayb", 3, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_regime_change() and c.total_cells(True) > 0)

    def play_event(self, _side, app):
        app.output_to_history("Draw 2 cards.", False)
        app.change_prestige(-2)
        allies = app.minor_jihad_in_good_fair_choice(1, True)
        if allies:
            target_name = allies[0][0]
            app.get_country(target_name).make_neutral()
            app.output_to_history("%s Alignment shifted to Neutral." % target_name)
        else:
            app.output_to_history("No Allies to shift.")
