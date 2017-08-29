from lwotai.cards.us.us_card import USCard


class Card45(USCard):

    def __init__(self):
        super(Card45, self).__init__(45, "Safer Now", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if app.num_islamist_rule() > 0:
            return False
        for country in app.get_countries():
            if country.is_good() and (country.total_cells(True) > 0 or country.plots > 0):
                return False
        return True

    def play_as_us(self, app):
        app.change_prestige(3)
        posture_roll = app.get_roll("US Posture")
        if posture_roll <= 4:
            app.us().make_soft()
            app.output_to_history("US Posture now Soft.", False)
        else:
            app.us().make_hard()
            app.output_to_history("US Posture now Hard.", False)
        while True:
            posture_country = app.get_country_from_user(
                "Now choose a non-US country to set its Posture: ", "XXX", None)
            if posture_country == "":
                print ""
            else:
                if posture_country == "United States":
                    print "Choose a non-US country."
                    print ""
                else:
                    new_posture = app.get_posture_from_user(
                        "What Posture should %s have (h or s)? " % posture_country)
                    app.output_to_history("%s Posture now %s" % (posture_country, new_posture), False)
                    app.set_posture(posture_country, new_posture)
                    app.output_to_history(app.get_country("United States").summary(), False)
                    app.output_to_history(app.get_country(posture_country).summary())
                    break
