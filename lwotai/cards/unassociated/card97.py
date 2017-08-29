import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card97(UnassociatedCard):

    def __init__(self):
        super(Card97, self).__init__(97, "Fatwa", 1, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_yes_no_from_user("Do both sides have cards remaining beyond this one? (y/n): ")

    def do_play_event(self, side, app):
        app.output_to_history("Trade random cards.", False)
        if side == "US":
            app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt,"
                                  " reassessment, regime, withdraw, or woi).", False)
        else:
            app.ai_flow_chart_major_jihad(97)
