from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card103(UnassociatedCard):

    def __init__(self):
        super(Card103, self).__init__(103, "Hizballah", 2, False, False, False, False)

    def do_play_event(self, side, app):
        if side == "US":
            one_away = []
            two_away = []
            three_away = []
            for countryObj in app.get_country("Lebanon").links:
                one_away.append(countryObj.name)
            for country in one_away:
                for subCountryObj in app.get_country(country).links:
                    if subCountryObj.name not in two_away and subCountryObj.name not in one_away and\
                                    subCountryObj.name != "Lebanon":
                        two_away.append(subCountryObj.name)
            for country in two_away:
                for subCountryObj in app.get_country(country).links:
                    if subCountryObj.name not in three_away and subCountryObj.name not in two_away and\
                                    subCountryObj.name not in one_away and subCountryObj.name != "Lebanon":
                        three_away.append(subCountryObj.name)
            possibles = []
            for country_name in one_away:
                country = app.get_country(country_name)
                if country_name not in possibles and country.total_cells(True) > 0 and country.is_shia_mix():
                    possibles.append(country_name)
            for country_name in two_away:
                country = app.get_country(country_name)
                if country_name not in possibles and country.total_cells(True) > 0 and country.is_shia_mix():
                    possibles.append(country_name)
            for country_name in three_away:
                country = app.get_country(country_name)
                if country_name not in possibles and country.total_cells(True) > 0 and country.is_shia_mix():
                    possibles.append(country_name)
            if len(possibles) <= 0:
                app.output_to_history("No Shia-Mix countries with cells within 3 countries of Lebanon.", True)
                target_name = None
            elif len(possibles) == 1:
                target_name = possibles[0]
            else:
                target_name = None
                while not target_name:
                    country_name = app.get_country_from_user(
                        "Remove a cell from what Shia-Mix country within 3 countries of Lebanon (? for list): ",
                        "XXX", app.list_countries_in_param, possibles)
                    if country_name == "":
                        print ""
                    else:
                        if app.get_country(country_name).total_cells(True) <= 0:
                            print "There are no cells in %s" % country_name
                            print ""
                        elif country_name not in possibles:
                            print "%s not a Shia-Mix country within 3 countries of Lebanon." % country_name
                            print ""
                        else:
                            target_name = country_name
            if target_name:
                app.remove_cell(target_name, side)    # 20150131PS added side
                app.output_to_history(app.get_country(target_name).summary(), True)
        else:
            app.test_country("Lebanon")
            app.get_country("Lebanon").make_poor()
            app.output_to_history("Lebanon governance now Poor.", False)
            app.get_country("Lebanon").make_neutral()
            app.output_to_history("Lebanon alignment now Neutral.", True)
