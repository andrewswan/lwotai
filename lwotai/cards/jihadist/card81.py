import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card81(JihadistCard):

    def __init__(self):
        super(Card81, self).__init__(81, "Foreign Fighters", 3, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.num_regime_change() > 0

    def play_event(self, _side, app):
        possibles = app.find_countries(lambda c: c.is_regime_change())
        if not possibles:
            return False
        target = random.choice(possibles)
        app.place_cells(target.name, 5)
        if target.get_aid() > 0:
            target.reduce_aid_by(1)
            app.output_to_history("One Aid removed from %s" % target.name, False)
        else:
            target.make_besieged()
            app.output_to_history("%s to Besieged Regime" % target.name, False)
        app.output_to_history(target.summary())
