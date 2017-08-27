from lwotai.cards.abstract_card import AbstractCard


class Card36(AbstractCard):

    def __init__(self):
        super(Card36, self).__init__(36, "US", "Indo-Pakistani Talks", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        pakistan = app.get_country('Pakistan')
        return pakistan.is_good() or pakistan.is_fair()

    def play_event(self, side, app):
        app.markers.append("Indo-Pakistani Talks")
        app.output_to_history("Indo-Pakistani Talks in Play.", False)
        app.get_country('Pakistan').make_ally()
        app.output_to_history("Pakistan now Ally", False)
        posture = app.get_posture_from_user("Select India's Posture (hard or soft): ")
        app.set_posture("India", posture)
        app.output_to_history(app.get_country("Pakistan").summary(), False)
        app.output_to_history(app.get_country("India").summary(), True)
