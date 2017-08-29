from lwotai.cards.us.us_card import USCard


class Card21(USCard):

    def __init__(self):
        super(Card21, self).__init__(21, "Let's Roll", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.plots > 0 and (c.is_ally() or c.is_good()))

    def play_as_us(self, app):
        while True:
            plot_country_name = app.get_country_from_user(
                "Draw a card. Choose an Ally or Good country to remove a plot from (? for list): ", "XXX",
                app.list_good_ally_plot_countries)
            if plot_country_name == "":
                print ""
                return
            else:
                plot_country = app.get_country(plot_country_name)
                if not plot_country.is_good() and not plot_country.is_ally():
                    print "%s is neither Good nor an Ally." % plot_country.name
                    print ""
                elif plot_country.plots <= 0:
                    print "%s has no plots." % plot_country.name
                    print ""
                else:
                    while True:
                        posture_country = app.get_country_from_user(
                            "Now choose a non-US country to set its Posture: ", "XXX", None)
                        if posture_country == "":
                            print ""
                            return
                        else:
                            if posture_country == "United States":
                                print "Choose a non-US country."
                                print ""
                            else:
                                new_posture = app.get_posture_from_user(
                                    "What Posture should %s have (h or s)? " % posture_country)
                                app.execute_card_lets_roll(plot_country_name, posture_country, new_posture)
                                return
