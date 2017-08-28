from lwotai.cards.us_card import USCard


class Card38(USCard):

    def __init__(self):
        super(Card38, self).__init__(38, "Libyan Deal", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Libya").is_poor() and\
            (app.get_country("Iraq").is_ally() or app.get_country("Syria").is_ally())

    def play_event(self, side, app):
        app.markers.append("Libyan Deal")
        app.output_to_history("Libyan Deal in Play.", False)
        app.get_country("Libya").make_ally()
        app.output_to_history("Libya now Ally", False)
        app.change_prestige(1)
        print "Select the Posture of 2 Schengen countries."
        for _ in range(2):
            target_country = None
            while not target_country:
                country_name = app.get_country_from_user(
                    "Choose Schengen country (? for list)?: ", "XXX", app.list_schengen_countries)
                if country_name == "":
                    print ""
                else:
                    target_country = app.get_country(country_name)
                    if not target_country.schengen:
                        print "%s is not a Schengen country." % country_name
                        print ""
                        return
                    else:
                        posture = app.get_posture_from_user(
                            "Select %s's Posture (hard or soft): " % country_name)
                        app.set_posture(country_name, posture)
                        app.output_to_history(target_country.summary(), False)
        app.output_to_history("", False)
