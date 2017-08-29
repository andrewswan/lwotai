import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card102(UnassociatedCard):

    def __init__(self):
        super(Card102, self).__init__(102, "Former Soviet Union", 2, False, False, False, False)

    def play_event(self, side, app):
        test_roll = random.randint(1, 6)
        if test_roll <= 4:
            app.get_country("Central Asia").make_poor()
        else:
            app.get_country("Central Asia").make_fair()
        app.get_country("Central Asia").make_neutral()
        app.output_to_history(
            "Central Asia tested, governance %s" % app.get_country("Central Asia").governance_str(), False)
