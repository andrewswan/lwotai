from lwotai.cards.us.us_card import USCard


class Card23and24and25(USCard):

    def __init__(self, number):
        super(Card23and24and25, self).__init__(number, "Predator", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.total_cells(True) > 0 and c.is_muslim())

    def play_as_us(self, app):
        while True:
            country_name = app.get_country_from_user(
                "Choose non-Iran Muslim Country to remove a cell from (? for list): ", "XXX",
                app.list_muslim_countries_with_cells)
            if country_name == "":
                print ""
                return
            else:
                country = app.get_country(country_name)
                if country.total_cells(True) == 0:
                    print "%s has no cells." % country_name
                    print ""
                elif country.is_iran():
                    print "Iran is not allowed."
                    print ""
                elif country.is_non_muslim():
                    print "Choose a Muslim country."
                    print ""
                else:
                    app.remove_cell(country.name, "US")    # 20150131PS added side
                    app.output_to_history(country.summary())
                    break
