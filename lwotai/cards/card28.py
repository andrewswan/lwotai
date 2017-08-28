from lwotai.cards.us_card import USCard


class Card28(USCard):

    def __init__(self):
        super(Card28, self).__init__(28, "Sharia", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.num_besieged() > 0

    def play_event(self, side, app):
        num_besieged = app.num_besieged()
        if num_besieged <= 0:
            return False
        elif num_besieged == 1:
            target_country = app.find_countries(lambda c: c.is_besieged())[0]
        else:
            while True:
                country_name = app.get_country_from_user(
                    "Choose a country with a Besieged Regime marker to remove (? for list): ", "XXX",
                    app.list_besieged_countries)
                if country_name == "":
                    print ""
                    return
                else:
                    target_country = app.get_country(country_name)
                    if not target_country.is_besieged():
                        print "%s is not a Besieged Regime." % country_name
                        print ""
                    else:
                        break
        target_country.remove_besieged()
        app.output_to_history("%s is no longer a Besieged Regime." % target_country.name, False)
        app.output_to_history(target_country.summary())
