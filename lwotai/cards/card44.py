from lwotai.cards.abstract_card import AbstractCard


class Card44(AbstractCard):

    def __init__(self):
        super(Card44, self).__init__(44, "US", "Renditions", 3, False, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.us().is_hard() and "Leak-Renditions" not in app.markers

    def play_event(self, side, app):
        app.markers.append("Renditions")
        app.output_to_history("Renditions in Play.", False)
        app.output_to_history("Discard a random card from the Jihadist hand.", False)
        if app.num_disruptable() > 0:
            app.disrupt_cells_or_cadre()
        app.output_to_history("", False)
