from lwotai.postures.posture import SOFT

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card75(JihadistCard):

    def __init__(self):
        super(Card75, self).__init__(75, "Schroeder & Chirac", 2, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.us().is_hard()

    def play_as_jihadist(self, app):
        app.set_posture("Germany", SOFT)
        app.output_to_history("%s Posture now %s" % ("Germany", app.get_posture("Germany")), True)
        app.set_posture("France", SOFT)
        app.output_to_history("%s Posture now %s" % ("France", app.get_posture("France")), True)
        app.change_prestige(-1)
