import random

from lwotai.governance import POOR, ISLAMIST_RULE
from lwotai.postures.posture import SOFT


class Card(object):
    """A card in the game"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing):
        self.number = number
        self.name = name
        self.type = card_type
        self.ops = ops
        self.remove = remove
        self.mark = mark
        self.lapsing = lapsing

    def playable(self, side, app, ignore_itjihad):
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 18:  # Intel Community
                return True
            elif self.number <= 47:  # The door of Itjihad was closed
                raise Exception("Has subclass")
            else:
                raise Exception("Invalid US card %d" % self.number)
        elif self.type == "Jihadist" and side == "Jihadist":
            if "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            elif self.number <= 68:  # Jemaah Islamiya
                raise Exception("Has subclass")
            elif self.number == 69:  # Kazakh Strain
                central_asia = app.get_country("Central Asia")
                return central_asia.total_cells() > 0 and "CTR" not in central_asia.markers
            elif self.number == 70:  # Lashkar-e-Tayyiba
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number == 71:  # Loose Nuke
                return app.get_country("Russia").total_cells() > 0 and "CTR" not in app.get_country("Russia").markers
            elif self.number == 72:  # Opium
                return app.get_country("Afghanistan").total_cells() > 0
            elif self.number == 73:  # Pirates
                return app.get_country("Somalia").is_islamist_rule() or app.get_country("Yemen").is_islamist_rule()
            elif self.number == 74:  # Schengen Visas
                return True
            elif self.number == 75:  # Schroeder & Chirac
                return app.us().is_hard()
            elif self.number == 76:  # Abu Ghurayb
                return app.contains_country(lambda c: c.is_regime_change() and c.total_cells(True) > 0)
            elif self.number == 77:  # Al Jazeera
                if app.get_country("Saudi Arabia").troops() > 0:
                    return True
                return app.contains_country(lambda c: app.is_adjacent("Saudi Arabia", c.name) and c.troops() > 0)
            elif self.number == 78:  # Axis of Evil
                return True
            elif self.number == 79:  # Clean Operatives
                return True
            elif self.number == 80:  # FATA
                return True
            elif self.number == 81:  # Foreign Fighters
                return app.num_regime_change() > 0
            elif self.number == 82:  # Jihadist Videos
                return True
            elif self.number == 83:  # Kashmir
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number in [84, 85]:  # Leak
                return ("Enhanced Measures" in app.markers) or ("Renditions" in app.markers) or ("Wiretapping" in
                                                                                                 app.markers)
            elif self.number == 86:  # Lebanon War
                return True
            elif self.number in [87, 88, 89]:  # Martyrdom Operation
                return app.contains_country(lambda c: not c.is_islamist_rule() and c.total_cells(True) > 0)
            elif self.number == 90:  # Quagmire
                valid_target = app.contains_country(lambda c: c.is_regime_change() and c.total_cells(True) > 0)
                return valid_target and app.prestige < 7
            elif self.number == 91:  # Regional al-Qaeda
                targets = app.find_countries(lambda c: c.is_muslim() and c.is_ungoverned())
                return len(targets) >= 2
            elif self.number == 92:  # Saddam
                iraq = app.get_country("Iraq")
                return "Saddam Captured" not in app.markers and iraq.is_poor() and iraq.is_adversary()
            elif self.number == 93:  # Taliban
                return True
            elif self.number == 94:  # The door of Itjihad was closed
                return app.get_yes_no_from_user(
                    "Was a country tested or improved to Fair or Good this or last Action Phase.? (y/n): ")
            elif self.number == 95:  # Wahhabism
                return True
        else:  # Unassociated Events
            if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 96:  # Danish Cartoons
                return True
            elif self.number == 97:  # Fatwa
                return app.get_yes_no_from_user("Do both sides have cards remaining beyond this one? (y/n): ")
            elif self.number == 98:  # Gaza Withdrawl
                return True
            elif self.number == 99:  # HAMAS Elected
                return True
            elif self.number == 100:  # His Ut-Tahrir
                return True
            elif self.number == 101:  # Kosovo
                return True
            elif self.number == 102:  # Former Soviet Union    #20150312PS
                return True
            elif self.number == 103:  # Hizballah
                return True
            elif self.number == 104 or self.number == 105:  # Iran
                return True
            elif self.number == 106:  # Jaysh al-Mahdi
                return app.contains_country(lambda c: c.is_shia_mix() and c.troops() > 0 and c.total_cells() > 0)
            elif self.number == 107:  # Kurdistan
                return True
            elif self.number == 108:  # Musharraf
                return "Benazir Bhutto" not in app.markers and app.get_country("Pakistan").total_cells() > 0
            elif self.number == 109:  # Tora Bora
                return app.contains_country(lambda c: c.is_regime_change() and c.total_cells() >= 2)
            elif self.number == 110:  # Zarqawi
                return app.get_country("Iraq").troops() > 0 or app.get_country("Syria").troops() > 0 or \
                    app.get_country("Lebanon").troops() > 0 or app.get_country("Jordan").troops() > 0
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    if "FATA" in app.get_country("Pakistan").markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.num_islamist_rule() == 0
                else:
                    return True
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    if "FATA" in app.get_country("Pakistan").markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.num_islamist_rule() == 0
                else:
                    return True
            elif self.number == 113:  # Darfur
                return True
            elif self.number == 114:  # GTMO
                return True
            elif self.number == 115:  # Hambali
                possibles = ["Indonesia/Malaysia"]
                for country in app.get_country("Indonesia/Malaysia").links:
                    possibles.append(country.name)
                for country in possibles:
                    if app.get_country(country).total_cells(True) > 0:
                        if app.get_country(country).is_non_muslim():
                            if app.get_country(country).is_hard():
                                return True
                        else:
                            if app.get_country(country).is_ally():
                                return True
            elif self.number == 116:  # KSM
                if side == "US":
                    return app.contains_country(lambda c: c.plots > 0 and (c.is_non_muslim() or c.is_ally()))
                else:
                    return True
            elif self.number in [117, 118]:  # Oil Price Spike
                return True
            elif self.number == 119:  # Saleh
                return True
            elif self.number == 120:  # US Election
                return True
            return False

    def puts_cell(self):
        """Indicates whether this card places a cell"""
        if self.type == "US":
            return False
        elif self.number <= 68:  # Jemaah Islamiya
            raise Exception("Has subclass")
        elif self.number == 69:  # Kazakh Strain
            return False
        elif self.number == 70:  # Lashkar-e-Tayyiba
            return True
        elif self.number == 71:  # Loose Nuke
            return False
        elif self.number == 72:  # Opium
            return True
        elif self.number == 73:  # Pirates
            return False
        elif self.number == 74:  # Schengen Visas
            return False
        elif self.number == 75:  # Schroeder & Chirac
            return False
        elif self.number == 76:  # Abu Ghurayb
            return False
        elif self.number == 77:  # Al Jazeera
            return False
        elif self.number == 78:  # Axis of Evil
            return False
        elif self.number == 79:  # Clean Operatives
            return False
        elif self.number == 80:  # FATA
            return True
        elif self.number == 81:  # Foreign Fighters
            return True
        elif self.number == 82:  # Jihadist Videos
            return True
        elif self.number == 83:  # Kashmir
            return True
        elif self.number == 84 or self.number == 85:  # Leak
            return False
        elif self.number == 86:  # Lebanon War
            return True
        elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
            return False
        elif self.number == 90:  # Quagmire
            return False
        elif self.number == 91:  # Regional al-Qaeda
            return True
        elif self.number == 92:  # Saddam
            return False
        elif self.number == 93:  # Taliban
            return True
        elif self.number == 94:  # The door of Itjihad was closed
            return False
        elif self.number == 95:  # Wahhabism
            return False
        elif self.number == 96:  # Danish Cartoons
            return False
        elif self.number == 97:  # Fatwa
            return False
        elif self.number == 98:  # Gaza Withdrawl
            return True
        elif self.number == 99:  # HAMAS Elected
            return False
        elif self.number == 100:  # His Ut-Tahrir
            return False
        elif self.number == 101:  # Kosovo
            return False
        elif self.number == 102:  # Former Soviet Union
            return False
        elif self.number == 103:  # Hizballah
            return False
        elif self.number == 104 or self.number == 105:  # Iran
            return False
        elif self.number == 106:  # Jaysh al-Mahdi
            return False
        elif self.number == 107:  # Kurdistan
            return False
        elif self.number == 108:  # Musharraf
            return False
        elif self.number == 109:  # Tora Bora
            return False
        elif self.number == 110:  # Zarqawi
            return True
        elif self.number == 111:  # Zawahiri
            return False
        elif self.number == 112:  # Bin Ladin
            return False
        elif self.number == 113:  # Darfur
            return False
        elif self.number == 114:  # GTMO
            return False
        elif self.number == 115:  # Hambali
            return False
        elif self.number == 116:  # KSM
            return False
        elif self.number == 117 or self.number == 118:  # Oil Price Spike
            return False
        elif self.number == 119:  # Saleh
            return False
        elif self.number == 120:  # US Election
            return False
        return False

    def play_event(self, side, app):
        app.output_to_history("Card played for Event.")
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number <= 17:  # FSB
                raise Exception("Has subclass")
            elif self.number == 18:  # Intel Community
                app.output_to_history("Examine Jihadist hand. Do not change order of cards.", False)
                app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment,"
                                      " regime_change, withdraw, or war_of_ideas).", False)
                app.output_to_history(
                    "You may now interrupt this action phase to play another card (Use the u command).", True)
            elif self.number <= 47:  # The door of Itjihad was closed
                raise Exception("Has subclass")
            else:
                raise Exception("Invalid US card %d", self.number)
        elif self.type == "Jihadist" and side == "Jihadist":
            if self.number <= 68:  # Jemaah Islamiya
                raise Exception("Has subclass")
            elif self.number == 69:  # Kazakh Strain
                roll = random.randint(1, 6)
                app.execute_card_heu("Central Asia", roll)
            elif self.number == 70:  # Lashkar-e-Tayyiba
                app.place_cells("Pakistan", 1)
                if app.cells > 0:
                    app.place_cells("India", 1)
            elif self.number == 71:  # Loose Nuke
                roll = random.randint(1, 6)
                app.execute_card_heu("Russia", roll)
            elif self.number == 72:  # Opium
                cells_to_place = min(app.cells, 3)
                if app.get_country("Afghanistan").is_islamist_rule():
                    cells_to_place = app.cells
                app.place_cells("Afghanistan", cells_to_place)
            elif self.number == 73:  # Pirates
                app.markers.append("Pirates")
                app.output_to_history("Pirates in play.", False)
            elif self.number == 74:  # Schengen Visas
                if app.cells == 15:
                    app.output_to_history("No cells to travel.", False)
                    return
                app.handle_travel(2, False, True)
            elif self.number == 75:  # Schroeder & Chirac
                app.set_posture("Germany", SOFT)
                app.output_to_history("%s Posture now %s" % ("Germany", app.get_posture("Germany")), True)
                app.set_posture("France", SOFT)
                app.output_to_history("%s Posture now %s" % ("France", app.get_posture("France")), True)
                app.change_prestige(-1)
            elif self.number == 76:  # Abu Ghurayb
                app.output_to_history("Draw 2 cards.", False)
                app.change_prestige(-2)
                allies = app.minor_jihad_in_good_fair_choice(1, True)
                if not allies:
                    app.output_to_history("No Allies to shift.", True)
                else:
                    target_name = allies[0][0]
                    app.get_country(target_name).make_neutral()
                    app.output_to_history("%s Alignment shifted to Neutral." % target_name, True)
            elif self.number == 77:  # Al Jazeera
                choices = app.minor_jihad_in_good_fair_choice(1, False, True)
                if not choices:
                    app.output_to_history("No countries to shift.", True)
                else:
                    target = app.get_country(choices[0][0])
                    if target.is_ally():
                        target.make_neutral()
                    elif target.is_neutral():
                        target.make_adversary()
                    app.output_to_history("%s Alignment shifted to %s." % (target.name, target.alignment()))
            elif self.number == 78:  # Axis of Evil
                app.output_to_history("US discards any Iran, Hizballah, or Jaysh al-Mahdi cards from hand.", False)
                if app.us().is_soft():
                    app.us().make_hard()
                    app.output_to_history("US Posture now Hard.", False)
                prestige_rolls = []
                for i in range(3):
                    prestige_rolls.append(random.randint(1, 6))
                prestige_multiplier = 1
                if prestige_rolls[0] <= 4:
                    prestige_multiplier = -1
                app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
            elif self.number == 79:  # Clean Operatives
                app.handle_travel(2, False, False, True)
            elif self.number == 80:  # FATA
                app.test_country("Pakistan")
                if app.get_country("Pakistan").markers.count("FATA") == 0:
                    app.get_country("Pakistan").markers.append("FATA")
                    app.output_to_history("FATA marker added in Pakistan", True)
                app.place_cells("Pakistan", 1)
            elif self.number == 81:  # Foreign Fighters
                possibles = app.find_countries(lambda c: c.is_regime_change())
                if not possibles:
                    return False
                target = random.choice(possibles)
                app.place_cells(target.name, 5)
                if target.get_aid() > 0:
                    target.reduce_aid_by(1)
                    app.output_to_history("One Aid removed from %s" % target.name, False)
                else:
                    target.make_besieged()
                    app.output_to_history("%s to Besieged Regime" % target.name, False)
                app.output_to_history(target.summary())
            elif self.number == 82:  # Jihadist Videos
                possibles = app.find_countries(lambda c: c.total_cells() == 0)
                random.shuffle(possibles)
                for i in range(3):
                    app.test_country(possibles[i].name)
                    # number of available cells does not matter for Jihadist Videos
                    rolls = [random.randint(1, 6)]
                    app.execute_recruit(possibles[i].name, 1, rolls, False, True)
            elif self.number == 83:  # Kashmir
                app.place_cells("Pakistan", 1)
                pakistan = app.get_country("Pakistan")
                if pakistan.is_ally():
                    pakistan.make_neutral()
                elif pakistan.is_neutral():
                    pakistan.make_adversary()
                app.output_to_history("%s Alignment shifted to %s." % ("Pakistan", pakistan.alignment()), True)
                app.output_to_history(pakistan.summary(), True)
            elif self.number == 84 or self.number == 85:  # Leak
                possibles = []
                if "Enhanced Measures" in app.markers:
                    possibles.append("Enhanced Measures")
                if "Renditions" in app.markers:
                    possibles.append("Renditions")
                if "Wiretapping" in app.markers:
                    possibles.append("Wiretapping")
                target_name = random.choice(possibles)
                app.markers.remove(target_name)
                app.markers.append("Leak-"+target_name)
                app.output_to_history("%s removed and can no longer be played." % target_name, False)
                us_prestige_rolls = []
                for _ in range(3):
                    us_prestige_rolls.append(random.randint(1, 6))
                posture_roll = random.randint(1, 6)
                prestige_multiplier = 1
                if us_prestige_rolls[0] <= 4:
                    prestige_multiplier = -1
                app.change_prestige(min(us_prestige_rolls[1], us_prestige_rolls[2]) * prestige_multiplier, False)
                if posture_roll <= 4:
                    app.us().make_soft()
                else:
                    app.us().make_hard()
                app.output_to_history("US Posture now %s" % app.us_posture(), True)
                allies = app.minor_jihad_in_good_fair_choice(1, True)
                if not allies:
                    app.output_to_history("No Allies to shift.", True)
                else:
                    target_name = allies[0][0]
                    app.get_country(target_name).make_neutral()
                    app.output_to_history("%s Alignment shifted to Neutral." % target_name, True)
            elif self.number == 86:  # Lebanon War
                app.output_to_history("US discards a random card.", False)
                app.change_prestige(-1, False)
                possibles = app.find_countries(lambda c: c.is_shia_mix())
                target = random.choice(possibles)
                app.place_cells(target.name, 1)
            elif self.number in [87, 88, 89]:  # Martyrdom Operation
                if app.execute_plot(1, False, [1], True) == 1:
                    app.output_to_history("No plots could be placed.")
                    app.handle_radicalization(app.card(self.number).ops)
            elif self.number == 90:  # Quagmire
                app.set_posture("United States", SOFT)
                app.output_to_history("US Posture now Soft.", False)
                app.output_to_history("US randomly discards two cards and Jihadist plays them.", False)
                app.output_to_history("Do this using the 'jihadist_card' command for each card.", True)
            elif self.number == 91:  # Regional al-Qaeda
                possibles = app.find_countries(lambda c: c.is_muslim() and c.is_ungoverned())
                random.shuffle(possibles)
                if app.num_islamist_rule() > 0:
                    app.place_cells(possibles[0].name, 2)
                    app.place_cells(possibles[1].name, 2)
                else:
                    app.place_cells(possibles[0].name, 1)
                    app.place_cells(possibles[1].name, 1)
            elif self.number == 92:  # Saddam
                app.funding = 9
                app.output_to_history("Jihadist Funding now 9.")
            elif self.number == 93:  # Taliban
                app.test_country("Afghanistan")
                app.get_country("Afghanistan").make_besieged()
                app.output_to_history("Afghanistan is now a Besieged Regime.", False)
                app.place_cells("Afghanistan", 1)
                app.place_cells("Pakistan", 1)
                if app.get_country("Afghanistan").is_islamist_rule() or app.get_country("Pakistan").is_islamist_rule():
                    app.change_prestige(-3)
                else:
                    app.change_prestige(-1)
            elif self.number == 94:  # The door of Itjihad was closed
                target_country = None
                while not target_country:
                    country_name = app.get_country_from_user(
                        "Choose a country tested or improved to Fair or Good this or last Action Phase: ", "XXX", None)
                    if country_name == "":
                        print ""
                    elif app.get_country(country_name).is_fair() or app.get_country(country_name).is_good():
                        target_country = app.get_country(country_name)
                    else:
                        print "%s is neither Fair nor Good."
                app.worsen_governance(target_country.name)
                app.output_to_history("%s Governance worsened." % target_country.name, False)
                app.output_to_history(target_country.summary())
            elif self.number == 95:  # Wahhabism
                if app.get_country("Saudi Arabia").is_islamist_rule():
                    app.change_funding(9)
                else:
                    app.change_funding(app.get_country("Saudi Arabia").governance_as_funding())
        else:
            if self.number == 96:  # Danish Cartoons
                posture = app.get_posture_from_user("Select Scandinavia's Posture (hard or soft): ")
                app.set_posture("Scandinavia", posture)
                app.output_to_history("Scandinavia posture now %s." % posture, False)
                possibles = app.find_countries(lambda c: c.is_muslim() and not c.is_islamist_rule())
                target = random.choice(possibles)
                app.test_country(target.name)
                if app.num_islamist_rule() > 0:
                    app.output_to_history("Place any available plot in %s." % target.name, False)
                else:
                    app.output_to_history("Place a Plot 1 in %s." % target.name, False)
                target.plots += 1
            elif self.number == 97:  # Fatwa
                app.output_to_history("Trade random cards.", False)
                if side == "US":
                    app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt,"
                                          " reassessment, regime, withdraw, or woi).", False)
                else:
                    app.ai_flow_chart_major_jihad(97)
            elif self.number == 98:  # Gaza Withdrawl
                if side == "US":
                    app.change_funding(-1)
                else:
                    app.place_cells("Israel", 1)
            elif self.number == 99:  # HAMAS Elected
                app.output_to_history("US selects and discards one card.", False)
                app.change_prestige(-1)
                app.change_funding(-1)
            elif self.number == 100:  # His Ut-Tahrir
                if app.troops >= 10:
                    app.change_funding(-2)
                elif app.troops < 5:
                    app.change_funding(2)
            elif self.number == 101:  # Kosovo
                app.change_prestige(1)
                app.test_country("Serbia")
                serbia = app.get_country("Serbia")
                if app.us().is_soft():
                    serbia.make_hard()
                else:
                    serbia.make_soft()
                app.output_to_history("Serbia Posture now %s." % app.get_posture("Serbia"), True)
            elif self.number == 102:  # Former Soviet Union
                test_roll = random.randint(1, 6)
                if test_roll <= 4:
                    app.get_country("Central Asia").make_poor()
                else:
                    app.get_country("Central Asia").make_fair()
                app.get_country("Central Asia").make_neutral()
                app.output_to_history("%s tested, governance %s" %
                                      ("Central Asia", app.get_country("Central Asia").governance_str()), False)
            elif self.number == 103:  # Hizballah
                if side == "US":
                    one_away = []
                    two_away = []
                    three_away = []
                    for countryObj in app.get_country("Lebanon").links:
                        one_away.append(countryObj.name)
                    for country in one_away:
                        for subCountryObj in app.get_country(country).links:
                            if subCountryObj.name not in two_away and subCountryObj.name not in one_away and subCountryObj.name != "Lebanon":
                                two_away.append(subCountryObj.name)
                    for country in two_away:
                        for subCountryObj in app.get_country(country).links:
                            if subCountryObj.name not in three_away and subCountryObj.name not in two_away and subCountryObj.name not in one_away and subCountryObj.name != "Lebanon":
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
            elif self.number == 104 or self.number == 105:  # Iran
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

            elif self.number == 106:  # Jaysh al-Mahdi
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
            elif self.number == 107:  # Kurdistan
                if side == "US":
                    app.test_country("Iraq")
                    app.get_country("Iraq").add_aid(1)
                    app.output_to_history("Aid added to Iraq.", False)
                    app.output_to_history(app.get_country("Iraq").summary(), True)
                else:
                    app.test_country("Turkey")
                    possibles = []
                    if app.get_country("Turkey").governance_is_better_than(POOR):
                        possibles.append("Turkey")
                    iraq = app.get_country("Iraq")
                    if iraq.is_governed() and iraq.governance_is_better_than(POOR):
                        possibles.append("Iraq")
                    if len(possibles) == 0:
                        app.output_to_history("Iraq and Turkey cannot have governance worsened.", True)
                        return
                    elif len(possibles) == 0:
                        target_name = possibles[0]
                    else:
                        country_scores = {}
                        for country in possibles:
                            country_scores[country] = 0
                            if app.get_country(country).get_aid() > 0:
                                country_scores[country] += 10000
                            if app.get_country(country).is_besieged():
                                country_scores[country] += 1000
                            country_scores[country] += (app.country_resources_by_name(country) * 100)
                            country_scores[country] += random.randint(1, 99)
                        country_order = []
                        for country in country_scores:
                            country_order.append(
                                (country_scores[country], (app.get_country(country).total_cells(True)), country))
                        country_order.sort()
                        country_order.reverse()
                        target_name = country_order[0][2]
                    app.worsen_governance(target_name)
                    app.output_to_history("Governance worsened in %s." % target_name, False)
                    app.output_to_history(app.get_country(target_name).summary(), True)
            elif self.number == 108:  # Musharraf
                app.remove_cell("Pakistan", side)    # 20150131PS added side
                app.get_country("Pakistan").make_poor()
                app.get_country("Pakistan").make_ally()
                app.output_to_history("Pakistan now Poor Ally.", False)
                app.output_to_history(app.get_country("Pakistan").summary(), True)
            elif self.number == 109:  # Tora Bora
                possibles = [c.name for c in app.get_countries() if c.is_regime_change() and c.total_cells() >= 2]
                target_name = None
                if len(possibles) == 0:
                    return False
                if len(possibles) == 1:
                    target_name = possibles[0]
                else:
                    if side == "US":
                        app.output_to_history("US draws one card.", False)
                        while not target_name:
                            country_name = app.get_country_from_user(
                                "Choose a Regime Change country with at least 2 troops. (? for list)?: ", "XXX",
                                app.list_regime_change_with_two_cells)
                            if country_name == "":
                                print ""
                            else:
                                if country_name not in possibles:
                                    print "%s is not a Regime Change country with at least 2 troops." % country_name
                                    print ""
                                else:
                                    target_name = country_name
                    else:
                        app.output_to_history("Jihadist draws one card.", False)
                        target_name = random.choice(possibles)
                app.remove_cell(target_name, side)    # 20150131PS added side
                app.remove_cell(target_name, side)    # 20150131PS added side
                prestige_rolls = []
                for i in range(3):
                    prestige_rolls.append(random.randint(1, 6))
                prestige_multiplier = 1
                if prestige_rolls[0] <= 4:
                    prestige_multiplier = -1
                app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
            elif self.number == 110:  # Zarqawi
                if side == "US":
                    app.change_prestige(3)
                    app.output_to_history("Remove card from game.", False)
                else:
                    possibles = []
                    for country in ["Iraq", "Syria", "Lebanon", "Jordan"]:
                        if app.get_country(country).troops() > 0:
                            possibles.append(country)
                    target_name = random.choice(possibles)
                    app.place_cells(target_name, 3)
                    app.get_country(target_name).plots += 1
                    app.output_to_history("Add a Plot 2 to %s." % target_name, False)
                    app.output_to_history(app.get_country(target_name).summary(), True)
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    app.change_funding(-2)
                else:
                    if app.num_islamist_rule() > 0:
                        app.change_prestige(-3)
                    else:
                        app.change_prestige(-1)
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    app.change_funding(-4)
                    app.change_prestige(1)
                    app.output_to_history("Remove card from game.", False)
                else:
                    if app.num_islamist_rule() > 0:
                        app.change_prestige(-4)
                    else:
                        app.change_prestige(-2)
            elif self.number == 113:  # Darfur
                app.test_country("Sudan")
                if app.prestige >= 7:
                    app.get_country("Sudan").add_aid(1)
                    app.output_to_history("Aid added to Sudan.", False)
                    if app.get_country("Sudan").is_adversary():
                        app.get_country("Sudan").make_neutral()
                        app.output_to_history("Sudan alignment improved.", False)
                    elif app.get_country("Sudan").is_neutral():
                        app.get_country("Sudan").make_ally()
                        app.output_to_history("Sudan alignment improved.", False)
                else:
                    app.get_country("Sudan").make_besieged()
                    app.output_to_history("Sudan now Besieged Regime.", False)
                    if app.get_country("Sudan").is_ally():
                        app.get_country("Sudan").make_neutral()
                        app.output_to_history("Sudan alignment worsened.", False)
                    elif app.get_country("Sudan").is_neutral():
                        app.get_country("Sudan").make_adversary()
                        app.output_to_history("Sudan alignment worsened.", False)
                app.output_to_history(app.get_country("Sudan").summary(), True)
            elif self.number == 114:  # GTMO
                app.lapsing.append("GTMO")
                app.output_to_history(
                    "GTMO in play. No recruit operations or Detainee Release the rest of this turn.", False)
                prestige_rolls = []
                for i in range(3):
                    prestige_rolls.append(random.randint(1, 6))
                prestige_multiplier = 1
                if prestige_rolls[0] <= 4:
                    prestige_multiplier = -1
                app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
            elif self.number == 115:  # Hambali
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
            elif self.number == 116:  # KSM
                if side == "US":
                    for country in app.get_countries():
                        if country.plots > 0:
                            if country.is_ally() or country.is_non_muslim():
                                num_plots = country.plots
                                country.plots = 0
                                app.output_to_history("%d Plots removed from %s." % (num_plots, country.name), False)
                    app.output_to_history("US draws 2 cards.", True)
                else:
                    if app.execute_plot(1, False, [1], False, False, True) == 1:
                        app.output_to_history("No plots could be placed.", True)
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                app.lapsing.append("Oil Price Spike")
                app.output_to_history(
                    "Oil Price Spike in play. Add +1 to the resources of each Oil Exporter country for the turn.",
                    False)
                if side == "US":
                    app.output_to_history(
                        "Select, reveal, and draw a card other than Oil Price Spike from the discard pile or a box.")
                else:
                    if app.get_yes_no_from_user("Are there any Jihadist event cards in the discard pile? "):
                        app.output_to_history("Draw from the Discard Pile randomly among the highest-value"
                                              " Jihadist-associated event cards. Put the card on top of the Jihadist"
                                              " hand.")
            elif self.number == 119:  # Saleh
                app.test_country("Yemen")
                if side == "US":
                    if not app.get_country("Yemen").is_islamist_rule():
                        if app.get_country("Yemen").is_adversary():
                            app.get_country("Yemen").make_neutral()
                        elif app.get_country("Yemen").is_neutral():
                            app.get_country("Yemen").make_ally()
                        app.output_to_history(
                            "Yemen Alignment improved to %s." % app.get_country("Yemen").alignment(), False)
                        app.get_country("Yemen").add_aid(1)
                        app.output_to_history("Aid added to Yemen.", True)
                else:
                    if app.get_country("Yemen").is_ally():
                        app.get_country("Yemen").make_neutral()
                    elif app.get_country("Yemen").is_neutral():
                        app.get_country("Yemen").make_adversary()
                    app.output_to_history(
                        "Yemen Alignment worsened to %s." % app.get_country("Yemen").alignment(), False)
                    app.get_country("Yemen").make_besieged()
                    app.output_to_history("Yemen now Besieged Regime.", True)
            elif self.number == 120:  # US Election
                app.execute_card_us_election(random.randint(1, 6))
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)
