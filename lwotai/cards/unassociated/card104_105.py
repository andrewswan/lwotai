import random

from lwotai.governance import POOR

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card104and105(UnassociatedCard):

    def __init__(self, number):
        super(Card104and105, self).__init__(number, "Iran", 2, False, False, False, False)

    def do_play_event(self, side, app):
        if side == "US":
            target_name = None
            while not target_name:
                country_name = app.get_country_from_user("Choose a Shia-Mix country to test. You can then"
                                                         " remove a cell from there or Iran (? for list)?: ",
                                                         "XXX", app.list_shia_mix_countries)
                if country_name == "":
                    print ""
                else:
                    if app.get_country(country_name).is_shia_mix():
                        target_name = country_name
                    else:
                        print "%s is not a Shia-Mix country." % country_name
                        print ""
            picked = target_name
            app.test_country(picked)
            if app.get_country("Iran").total_cells(True) > 0:
                target_name = None
                while not target_name:
                    country_name = app.get_country_from_user(
                        "Remove a cell from %s or %s: " % (picked, "Iran"), "XXX", None)
                    if country_name == "":
                        print ""
                    else:
                        if country_name != picked and country_name != "Iran":
                            print "Remove a cell from %s or %s: " % (picked, "Iran")
                            print ""
                        else:
                            target_name = country_name
            else:
                target_name = picked
            app.remove_cell(target_name, side)    # 20150131PS added side
            app.output_to_history(app.get_country(target_name).summary(), True)
        else:
            possibles = [country.name for country in app.get_countries() if country.is_shia_mix()]
            target_name = random.choice(possibles)
            app.test_country(target_name)
            tested = target_name
            good_countries = [country.name for country in app.map.countries() if
                              country.is_muslim() and country.is_good()]
            if len(good_countries) > 1:
                distances = []
                for country in good_countries:
                    distances.append((app.country_distance(tested, country), country))
                distances.sort()
                target_name = distances[0][1]
            elif len(good_countries) == 1:
                target_name = good_countries[0]
            else:
                fair_countries = [country.name for country in app.map.countries() if
                                  country.is_muslim() and country.is_fair()]
                if len(fair_countries) > 1:
                    distances = []
                    for country in fair_countries:
                        distances.append((app.country_distance(tested, country), country))
                    distances.sort()
                    target_name = distances[0][1]
                elif len(fair_countries) == 1:
                    target_name = fair_countries[0]
                else:
                    app.output_to_history("No Good or Fair countries to Jihad in.", True)
                    return
            app.output_to_history("%s selected for jihad rolls." % target_name, False)
            for i in range(2):
                roll = random.randint(1, 6)
                app.output_to_history("Rolled: " + str(roll), False)
                if app.get_country(target_name).is_non_recruit_success(roll):
                    if app.get_country(target_name).governance_is_better_than(POOR):
                        app.worsen_governance(target_name)
                        app.output_to_history("Governance worsened in %s." % target_name, False)
                        app.output_to_history(app.get_country(target_name).summary(), True)
                else:
                    app.output_to_history("Roll failed.  No change to governance in %s." % target_name, False)
