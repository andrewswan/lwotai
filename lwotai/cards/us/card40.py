from lwotai.cards.us.us_card import USCard


class Card40(USCard):

    def __init__(self):
        super(Card40, self).__init__(40, "Mass Turnout", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.num_regime_change() > 0

    def play_event(self, side, app):
        num_regime_change = app.num_regime_change()
        if num_regime_change <= 0:
            return False
        elif num_regime_change == 1:
            target_country = app.find_countries(lambda c: c.is_regime_change())[0]
        else:
            while True:
                country_name = app.get_country_from_user(
                    "Choose a Regime Change Country to improve governance (? for list): ", "XXX",
                    app.list_regime_change_countries)
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
        app.improve_governance(target_country.name)
        app.output_to_history("%s Governance improved." % target_country.name, False)
        app.output_to_history(target_country.summary())
