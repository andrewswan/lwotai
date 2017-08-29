from lwotai.postures.posture import SOFT

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card90(JihadistCard):

    def __init__(self):
        super(Card90, self).__init__(90, "Quagmire", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        valid_target = app.contains_country(lambda c: c.is_regime_change() and c.total_cells(True) > 0)
        return valid_target and app.prestige < 7

    def play_event(self, _side, app):
        app.set_posture("United States", SOFT)
        app.output_to_history("US Posture now Soft.", False)
        app.output_to_history("US randomly discards two cards and Jihadist plays them.", False)
        app.output_to_history("Do this using the 'jihadist_card' command for each card.", True)
