from lwotai.cards.us_card import USCard


class Card46(USCard):

    def __init__(self):
        super(Card46, self).__init__(46, "Sistani", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        for country in app.get_countries():
            if country.is_shia_mix() and country.is_regime_change() and country.total_cells(True) > 0:
                return True
        return False

    def play_event(self, side, app):
        target_countries = [c.name for c in app.get_countries() if
                            c.is_shia_mix() and c.is_regime_change() and c.total_cells(True) > 0]
        target_name = None
        if len(target_countries) == 1:
            target_name = target_countries[0]
        else:
            while not target_name:
                country_name = app.get_country_from_user(
                    "Choose a Shia-Mix Regime Change Country with a cell to improve governance (? for list): ",
                    "XXX", app.list_shia_mix_regime_change_countries_with_cells)
                if country_name == "":
                    print ""
                else:
                    if country_name not in target_countries:
                        print "%s is not a Shia-Mix Regime Change Country with a cell." % country_name
                        print ""
                    else:
                        target_name = country_name
                        break
        app.improve_governance(target_name)
        app.output_to_history("%s Governance improved." % target_name, False)
        app.output_to_history(app.get_country(target_name).summary())
