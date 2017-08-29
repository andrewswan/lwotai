import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card96(UnassociatedCard):

    def __init__(self):
        super(Card96, self).__init__(96, "Danish Cartoons", 1, True, False, False, False)

    def play_event(self, _side, app):
        posture = app.get_posture_from_user("Select Scandinavia's Posture (hard or soft): ")
        app.set_posture("Scandinavia", posture)
        app.output_to_history("Scandinavia posture now %s." % posture, False)
        possibles = app.find_countries(lambda c: c.is_muslim() and not c.is_islamist_rule())
        target = random.choice(possibles)
        app.test_country(target.name)
        if app.num_islamist_rule() > 0:
            app.output_to_history("Place any available plot in %s." % target.name, False)
        else:
            app.output_to_history("Place a Plot 1 in %s." % target.name, False)
        target.plots += 1
