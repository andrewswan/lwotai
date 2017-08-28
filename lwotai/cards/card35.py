from lwotai.cards.us_card import USCard


class Card35(USCard):

    def __init__(self):
        super(Card35, self).__init__(35, "Hijab", 3, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.num_islamist_rule() == 0

    def play_event(self, side, app):
        app.test_country("Turkey")
        app.get_country("Turkey").improve_governance()
        app.output_to_history("Turkey Governance now %s." % app.get_country("Turkey").governance_str(), False)
        app.change_funding(-2)
        posture = app.get_posture_from_user("Select France's Posture (hard or soft): ")
        app.set_posture("France", posture)
        app.output_to_history(app.get_country("Turkey").summary(), False)
        app.output_to_history(app.get_country("France").summary())
