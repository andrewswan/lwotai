from lwotai.cards.jihadist.jihadist_card import JihadistCard
from lwotai.governance import POOR


class Card64(JihadistCard):

    def __init__(self):
        super(Card64, self).__init__(64, "Hariri Killed", 2, True, False, False, False)

    def play_event(self, _side, app):
        app.test_country("Lebanon")
        app.test_country("Syria")
        syria = app.get_country("Syria")
        syria.make_adversary()
        app.output_to_history("Syria now Adversary.", False)
        if syria.governance_is_better_than(POOR):
            app.worsen_governance("Syria")
            app.output_to_history("Governance in Syria worsened.", False)
            app.output_to_history(syria.summary())
        app.output_to_history(app.get_country("Lebanon").summary())
