from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card87and88and89(JihadistCard):

    def __init__(self, number):
        super(Card87and88and89, self).__init__(number, "Martyrdom Operation", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: not c.is_islamist_rule() and c.total_cells(True) > 0)

    def play_as_jihadist(self, app):
        if app.execute_plot(1, False, [1], True) == 1:
            app.output_to_history("No plots could be placed.")
            app.handle_radicalization(app.card(self.number).ops)
