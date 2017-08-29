from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card52(JihadistCard):

    def __init__(self):
        super(Card52, self).__init__(52, "IEDs", 1, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_regime_change() and c.total_cells(True) > 0)

    def play_as_jihadist(self, app):
        app.output_to_history("US randomly discards one card.")
