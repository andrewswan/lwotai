from lwotai.cards.us.us_card import USCard


class Card8and9and10(USCard):

    def __init__(self, number):
        super(Card8and9and10, self).__init__(number, "Special Forces", 1, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        for country in app.get_countries():
            if country.total_cells(True) > 0:
                for subCountry in app.get_countries():
                    if country.name == subCountry.name or app.is_adjacent(subCountry.name, country.name):
                        if subCountry.troops() > 0:
                            return True
        return False

    def play_as_us(self, app):
        while True:
            target_country_name = app.get_country_from_user(
                "Remove a cell from which country that has troops or is adjacent to a country with troops"
                " (? for list)?: ", "XXX", app.list_countries_with_cell_and_adjacent_troops)
            if target_country_name == "":
                print ""
                return
            else:
                target_country = app.get_country(target_country_name)
                if target_country.total_cells(True) <= 0:
                    print "There are no cells in %s" % target_country_name
                    print ""
                else:
                    found_troops = False
                    for other_country_name in app.map.country_names():
                        if other_country_name == target_country.name or \
                                app.is_adjacent(target_country_name, other_country_name):
                            if app.get_country(other_country_name).troops() > 0:
                                found_troops = True
                                break
                    if found_troops:
                        app.remove_cell(target_country_name, "US")    # 20150131PS added side
                        app.output_to_history(target_country.summary(), True)
                        break
                    else:
                        print "Neither this or any adjacent country has troops."
                        print ""
