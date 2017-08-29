import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card115(UnassociatedCard):

    def __init__(self):
        super(Card115, self).__init__(115, "Hambali", 3, False, False, False, False)

    def _really_playable(self, side, app, _ignore_itjihad):
        possibles = ["Indonesia/Malaysia"]
        for country_name in app.get_country("Indonesia/Malaysia").links:
            possibles.append(country_name.name)
        for country_name in possibles:
            country = app.get_country(country_name)
            if country.total_cells(True) > 0:
                if country.is_non_muslim():
                    if country.is_hard():
                        return True
                else:
                    if country.is_ally():
                        return True

    def do_play_event(self, side, app):
        if side == "US":
            possibles = ["Indonesia/Malaysia"]
            targets = []
            target_name = None
            for countryObj in app.get_country("Indonesia/Malaysia").links:
                possibles.append(countryObj.name)
            for country in possibles:
                if app.get_country(country).total_cells(True) > 0:
                    if app.get_country(country).is_non_muslim():
                        if app.get_country(country).is_hard():
                            targets.append(country)
                    else:
                        if app.get_country(country).is_ally():
                            targets.append(country)
            if len(targets) == 1:
                target_name = targets[0]
            else:
                while not target_name:
                    country_name = app.get_country_from_user("Choose Indonesia or an adjacent country that "
                                                             "has a cell and is Ally or Hard. (? for list)?: ",
                                                             "XXX", app.list_hambali)
                    if country_name == "":
                        print ""
                    else:
                        if country_name not in targets:
                            print "%s is not Indonesia or an adjacent country that has a cell and is Ally or" \
                                  " Hard." % country_name
                            print ""
                        else:
                            target_name = country_name
            app.remove_cell(target_name, side)    # 20150131PS added side
            app.output_to_history("US draw 2 cards.", False)
        else:
            possibles = ["Indonesia/Malaysia"]
            targets = []
            for countryObj in app.get_country("Indonesia/Malaysia").links:
                possibles.append(countryObj.name)
            for country in possibles:
                if app.get_country(country).total_cells(True) > 0:
                    if app.get_country(country).is_non_muslim():
                        if app.get_country(country).is_hard():
                            targets.append(country)
                    else:
                        if app.get_country(country).is_ally():
                            targets.append(country)
            target_name = random.choice(targets)
            app.get_country(target_name).plots += 1
            app.output_to_history("Place an plot in %s." % target_name, True)
