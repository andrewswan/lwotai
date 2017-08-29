import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card110(UnassociatedCard):

    def __init__(self):
        super(Card110, self).__init__(110, "Zarqawi", 2, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").troops() > 0 or app.get_country("Syria").troops() > 0 or \
               app.get_country("Lebanon").troops() > 0 or app.get_country("Jordan").troops() > 0

    def do_play_event(self, side, app):
        if side == "US":
            app.change_prestige(3)
            app.output_to_history("Remove card from game.", False)
        else:
            possibles = []
            for country in ["Iraq", "Syria", "Lebanon", "Jordan"]:
                if app.get_country(country).troops() > 0:
                    possibles.append(country)
            target_name = random.choice(possibles)
            app.place_cells(target_name, 3)
            app.get_country(target_name).plots += 1
            app.output_to_history("Add a Plot 2 to %s." % target_name, False)
            app.output_to_history(app.get_country(target_name).summary())
