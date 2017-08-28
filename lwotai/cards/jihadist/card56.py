from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card56(JihadistCard):

    def __init__(self):
        super(Card56, self).__init__(56, "Vieira de Mello Slain", 1, True, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_regime_change() and c.total_cells() > 0)

    def play_event(self, side, app):
        app.markers.append("Vieira de Mello Slain")
        app.output_to_history("Vieira de Mello Slain in play.", False)
        app.change_prestige(-1)
