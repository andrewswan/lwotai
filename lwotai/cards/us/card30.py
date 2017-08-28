from lwotai.cards.us.us_card import USCard


class Card30(USCard):

    def __init__(self):
        super(Card30, self).__init__(30, "UN Nation Building", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.num_regime_change() > 0 and "Vieira de Mello Slain" not in app.markers

    def play_event(self, side, app):
        num_regime_change = app.num_regime_change()
        if num_regime_change <= 0 or "Vieira de Mello Slain" in app.markers:
            return False
        target_country = None
        if num_regime_change == 1:
            for country in app.get_countries():
                if country.is_regime_change():
                    target_country = country
                    break
        else:
            while True:
                country_name = app.get_country_from_user(
                    "Choose a Regime Change country (? for list): ", "XXX", app.list_regime_change_countries)
                if country_name == "":
                    print ""
                    return
                else:
                    target_country = app.get_country(country_name)
                    if target_country.is_regime_change():
                        break
                    else:
                        print "%s is not a Regime Change country." % country_name
                        print ""
        target_country.add_aid(1)
        app.output_to_history("Aid added to %s." % target_country.name, False)
        woi_roll = app.get_roll("WoI")
        modified_woi_roll = app.modified_woi_roll(woi_roll, target_country.name, False)
        app.handle_muslim_woi(modified_woi_roll, target_country.name)
