from lwotai.cards.unassociated.unassociated_card import UnassociatedCard
from lwotai.governance import ISLAMIST_RULE


class Card106(UnassociatedCard):

    def __init__(self):
        super(Card106, self).__init__(106, "Jaysh al-Mahdi", 2, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_shia_mix() and c.troops() > 0 and c.total_cells() > 0)

    def do_play_event(self, side, app):
        if side == "US":
            target_name = None
            possibles = [country.name for country in app.map.countries() if
                         country.is_shia_mix() and country.troops() > 0 and country.total_cells() > 0]
            if len(possibles) == 1:
                target_name = possibles[0]
            while not target_name:
                country_name = app.get_country_from_user(
                    "Choose a Shia-Mix country with cells and troops (? for list)?: ", "XXX",
                    app.list_shia_mix_countries_with_cells_troops)
                if country_name == "":
                    print ""
                else:
                    if country_name not in possibles:
                        print "%s is not a Shia-Mix country with cells and troops." % country_name
                        print ""
                    else:
                        target_name = country_name
            app.remove_cell(target_name, side)    # 20150131PS added side
            app.remove_cell(target_name, side)    # 20150131PS added side
            app.output_to_history(app.get_country(target_name).summary(), True)
        else:   # jihadist play (see 9.4.2.1)
            # Test a random Shia-Mix country
            search_origin = app.get_random_shia_mix_country()
            app.test_country(search_origin)
            good_countries = [c.name for c in app.get_countries() if c.is_muslim() and c.is_good() and
                              c.troops() and c.total_cells(True)]
            if len(good_countries) > 1:
                distances = []
                for country in good_countries:
                    distances.append((app.country_distance(search_origin, country), country))
                distances.sort()
                target_name = distances[0][1]
            elif len(good_countries) == 1:
                target_name = good_countries[0]
            else:
                fair_countries = [c.name for c in app.get_countries() if c.is_muslim() and c.is_fair() and
                                  c.troops() and c.total_cells(True)]
                if len(fair_countries) > 1:
                    distances = []
                    for country in fair_countries:
                        distances.append((app.country_distance(search_origin, country), country))
                    distances.sort()
                    target_name = distances[0][1]
                elif len(fair_countries) == 1:
                    target_name = fair_countries[0]
                else:
                    app.output_to_history("No Good or Fair countries to worsen Governance in.", True)
                    return
            if app.get_country(target_name).governance_is_better_than(ISLAMIST_RULE):
                app.worsen_governance(target_name)
                app.output_to_history("Governance worsened in %s." % target_name, False)
                app.output_to_history(app.get_country(target_name).summary(), True)
