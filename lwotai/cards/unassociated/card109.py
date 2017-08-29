import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card109(UnassociatedCard):

    def __init__(self):
        super(Card109, self).__init__(109, "Tora Bora", 2, True, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_regime_change() and c.total_cells() >= 2)

    def do_play_event(self, side, app):
        possibles = [c.name for c in app.get_countries() if c.is_regime_change() and c.total_cells() >= 2]
        target_name = None
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            target_name = possibles[0]
        else:
            if side == "US":
                app.output_to_history("US draws one card.", False)
                while not target_name:
                    country_name = app.get_country_from_user(
                        "Choose a Regime Change country with at least 2 troops. (? for list)?: ", "XXX",
                        app.list_regime_change_with_two_cells)
                    if country_name == "":
                        print ""
                    else:
                        if country_name not in possibles:
                            print "%s is not a Regime Change country with at least 2 troops." % country_name
                            print ""
                        else:
                            target_name = country_name
            else:
                app.output_to_history("Jihadist draws one card.", False)
                target_name = random.choice(possibles)
        app.remove_cell(target_name, side)    # 20150131PS added side
        app.remove_cell(target_name, side)    # 20150131PS added side
        prestige_rolls = []
        for i in range(3):
            prestige_rolls.append(random.randint(1, 6))
        prestige_multiplier = 1
        if prestige_rolls[0] <= 4:
            prestige_multiplier = -1
        app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
