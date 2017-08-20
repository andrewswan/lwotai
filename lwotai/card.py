import random

from lwotai.governance import GOOD, POOR, ISLAMIST_RULE


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
            if self.number == 1:  # Backlash
                return app.contains_country(lambda c: c.type != "Non-Muslim" and c.plots > 0)
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 3:  # CTR
                return app.us().is_soft()
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 4:  # Moro Talks
                return True
            elif self.number == 5:  # NEST
                return True
            elif self.number in [6, 7]:  # Sanctions
                return "Patriot Act" in app.markers
            elif self.number in [8, 9, 10]:  # Special Forces
                for country in app.get_countries():
                    if country.total_cells(True) > 0:
                        for subCountry in app.get_countries():
                            if country.name == subCountry.name or app.is_adjacent(subCountry.name, country.name):
                                if subCountry.troops() > 0:
                                    return True
                return False
            elif self.number == 11:  # Abbas
                return True
            elif self.number == 12:  # Al-Azhar
                return True
            elif self.number == 13:  # Anbar Awakening
                return (app.get_country("Iraq").troops() > 0) or (app.get_country("Syria").troops() > 0)
            elif self.number == 14:  # Covert Action
                return app.contains_country(lambda c: c.is_adversary())
            elif self.number == 15:  # Ethiopia Strikes
                return (app.get_country("Somalia").is_islamist_rule()) or (app.get_country("Sudan").is_islamist_rule())
            elif self.number == 16:  # Euro-Islam
                return True
            elif self.number == 17:  # FSB
                return True
            elif self.number == 18:  # Intel Community
                return True
            elif self.number == 19:  # Kemalist Republic
                return True
            elif self.number == 20:  # King Abdullah
                return True
            elif self.number == 21:  # Let's Roll
                return app.contains_country(lambda c: c.plots > 0 and (c.is_ally() or c.is_good()))
            elif self.number == 22:  # Mossad and Shin Bet
                target_cells = app.get_country("Israel").total_cells()
                target_cells += app.get_country("Jordan").total_cells()
                target_cells += app.get_country("Lebanon").total_cells()
                return target_cells > 0
            elif self.number in [23, 24, 25]:  # Predator
                return app.contains_country(lambda c: c.total_cells(True) > 0 and c.is_muslim())
            elif self.number == 26:  # Quartet
                if "Abbas" not in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                return not app.contains_country(lambda c: app.is_adjacent(c.name, "Israel") and c.is_islamist_rule())
            elif self.number == 27:  # Saddam Captured
                return app.get_country("Iraq").troops() > 0
            elif self.number == 28:  # Sharia
                return app.num_besieged() > 0
            elif self.number == 29:  # Tony Blair
                return True
            elif self.number == 30:  # UN Nation Building
                return app.num_regime_change() > 0 and "Vieira de Mello Slain" not in app.markers
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country_name in ["United States", "United Kingdom", "Canada"]:
                    country = app.get_country(country_name)
                    if country.total_cells() > 0 or country.cadre > 0 or country.plots > 0:
                        return True
                return False
            elif self.number == 32:  # Back Channel
                if app.us().is_hard():
                    return False
                if app.num_adversary() <= 0:
                    return False
                app.list_adversary_countries()
                return app.get_yes_no_from_user(
                    "Do you have a card with a value that exactly matches an Adversary's Resources? (y/n): ")
            elif self.number == 33:  # Benazir Bhutto
                if "Bhutto Shot" in app.markers:
                    return False
                if app.get_country("Pakistan").is_islamist_rule():
                    return False
                for country in app.get_country("Pakistan").links:
                    if country.is_islamist_rule():
                        return False
                return True
            elif self.number == 34:  # Enhanced Measures
                if "Leak-Enhanced Measures" in app.markers or app.us_posture() == "Soft":
                    return False
                return app.num_disruptable() > 0
            elif self.number == 35:  # Hajib
                return app.num_islamist_rule() == 0
            elif self.number == 36:  # Indo-Pakistani Talks
                pakistan = app.get_country('Pakistan')
                return pakistan.is_good() or pakistan.is_fair()
            elif self.number == 37:  # Iraqi WMD
                return app.us().is_hard() and app.get_country("Iraq").is_adversary()
            elif self.number == 38:  # Libyan Deal
                if app.get_country("Libya").is_poor():
                    if app.get_country("Iraq").is_ally() or app.get_country("Syria").is_ally():
                        return True
                return False
            elif self.number == 39:  # Libyan WMD
                return app.us().is_hard() and app.get_country("Libya").is_adversary() and\
                       "Libyan Deal" not in app.markers
            elif self.number == 40:  # Mass Turnout
                return app.num_regime_change() > 0
            elif self.number == 41:  # NATO
                return (app.num_regime_change() > 0) and (app.gwot_penalty() >= 0)
            elif self.number == 42:  # Pakistani Offensive
                return (app.get_country("Pakistan").is_ally()) and ("FATA" in app.get_country("Pakistan").markers)
            elif self.number == 43:  # Patriot Act
                return True
            elif self.number == 44:  # Renditions
                return app.us().is_hard() and "Leak-Renditions" not in app.markers
            elif self.number == 45:  # Safer Now
                if app.num_islamist_rule() > 0:
                    return False
                for country in app.get_countries():
                    if country.is_good() and (country.total_cells(True) > 0 or country.plots > 0):
                        return False
                return True
            elif self.number == 46:  # Sistani
                for country in app.get_countries():
                    if country.type == "Shia-Mix" and country.regimeChange > 0 and country.total_cells(True) > 0:
                        return True
                return False
            elif self.number == 47:  # The door of Itjihad was closed
                return True
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 48:  # Adam Gadahn
                if app.num_cells_available() <= 0:
                    return False
                return app.get_yes_no_from_user("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 49:  # Al-Ittihad al-Islami
                return True
            elif self.number == 50:  # Ansar al-Islam
                return app.get_country("Iraq").governance_is_worse_than(GOOD)
            elif self.number == 51:  # FREs
                return app.get_country("Iraq").troops() > 0
            elif self.number == 52:  # IDEs
                return app.contains_country(lambda c: c.regimeChange > 0 and c.total_cells(True) > 0)
            elif self.number == 53:  # Madrassas
                return app.get_yes_no_from_user("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 54:  # Moqtada al-Sadr
                return app.get_country("Iraq").troops() > 0
            elif self.number == 55:  # Uyghur Jihad
                return True
            elif self.number == 56:  # Vieira de Mello Slain
                return app.contains_country(lambda c: c.regimeChange > 0 and c.total_cells() > 0)
            elif self.number == 57:  # Abu Sayyaf
                return "Moro Talks" not in app.markers
            elif self.number == 58:  # Al-Anbar
                return "Anbar Awakening" not in app.markers
            elif self.number == 59:  # Amerithrax
                return True
            elif self.number == 60:  # Bhutto Shot
                return app.get_country("Pakistan").total_cells() > 0
            elif self.number == 61:  # Detainee Release
                if "GTMO" in app.lapsing or "Renditions" in app.markers:
                    return False
                return app.get_yes_no_from_user("Did the US Disrupt during this or the last Action Phase? (y/n): ")
            elif self.number == 62:  # Ex-KGB
                return True
            elif self.number == 63:  # Gaza War
                return True
            elif self.number == 64:  # Hariri Killed
                return True
            elif self.number == 65:  # HEU
                possibles = 0
                if app.get_country("Russia").total_cells() > 0 and "CTR" not in app.get_country("Russia").markers:
                    possibles += 1
                if app.get_country("Central Asia").total_cells() > 0 and "CTR" not in app.get_country("Central Asia").markers:
                    possibles += 1
                return possibles > 0
            elif self.number == 66:  # Homegrown
                return True
            elif self.number == 67:  # Islamic Jihad Union
                return True
            elif self.number == 68:  # Jemaah Islamiya
                return True
            elif self.number == 69:  # Kazakh Strain
                return app.get_country("Central Asia").total_cells() > 0 and "CTR" not in app.get_country("Central Asia").markers
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
                return app.contains_country(lambda c: c.regimeChange > 0 and c.total_cells(True) > 0)
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
                return ("Enhanced Measures" in app.markers) or ("Renditions" in app.markers) or ("Wiretapping" in app.markers)
            elif self.number == 86:  # Lebanon War
                return True
            elif self.number in [87, 88, 89]:  # Martyrdom Operation
                return app.contains_country(lambda c: not c.is_islamist_rule() and c.total_cells(True) > 0)
            elif self.number == 90:  # Quagmire
                valid_target = app.contains_country(lambda c: c.regimeChange > 0 and c.total_cells(True) > 0)
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
                return app.contains_country(lambda c: c.type == "Shia-Mix" and c.troops() > 0 and c.total_cells() > 0)
            elif self.number == 107:  # Kurdistan
                return True
            elif self.number == 108:  # Musharraf
                return "Benazir Bhutto" not in app.markers and app.get_country("Pakistan").total_cells() > 0
            elif self.number == 109:  # Tora Bora
                return app.contains_country(lambda c: c.regimeChange > 0 and c.total_cells() >= 2)
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
                        if app.get_country(country).type == "Non-Muslim":
                            if app.get_country(country).is_hard():
                                return True
                        else:
                            if app.get_country(country).is_ally():
                                return True
            elif self.number == 116:  # KSM
                if side == "US":
                    return app.contains_country(lambda c: c.plots > 0 and (c.type == "Non-Muslim" or c.is_ally()))
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
        if self.number == 48:  # Adam Gadahn
            return True
        elif self.number == 49:  # Al-Ittihad al-Islami
            return True
        elif self.number == 50:  # Ansar al-Islam
            return True
        elif self.number == 51:  # FREs
            return True
        elif self.number == 52:  # IDEs
            return False
        elif self.number == 53:  # Madrassas
            return True
        elif self.number == 54:  # Moqtada al-Sadr
            return False
        elif self.number == 55:  # Uyghur Jihad
            return True
        elif self.number == 56:  # Vieira de Mello Slain
            return False
        elif self.number == 57:  # Abu Sayyaf
            return True
        elif self.number == 58:  # Al-Anbar
            return True
        elif self.number == 59:  # Amerithrax
            return False
        elif self.number == 60:  # Bhutto Shot
            return False
        elif self.number == 61:  # Detainee Release
            return True
        elif self.number == 62:  # Ex-KGB
            return False
        elif self.number == 63:  # Gaza War
            return False
        elif self.number == 64:  # Hariri Killed
            return False
        elif self.number == 65:  # HEU
            return False
        elif self.number == 66:  # Homegrown
            return True
        elif self.number == 67:  # Islamic Jihad Union
            return True
        elif self.number == 68:  # Jemaah Islamiya
            return True
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

    def playEvent(self, side, app):
        app.output_to_history("Card played for Event.", True)
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 1:  # Backlash
                for country in app.get_countries():
                    if country.type != "Non-Muslim" and country.plots > 0:
                        app.output_to_history("Plot in Muslim country found. Select the plot during plot phase. Backlash in play")
                        app.backlashInPlay = True
                        return True
                return False
            elif self.number == 2:  # Biometrics
                app.lapsing.append("Biometrics")
                app.output_to_history("Biometrics in play. This turn, travel to adjacent Good countries must roll to"
                                      " succeed and no non-adjacent travel.", True)
            elif self.number == 3:  # CTR    20150616PS
                app.get_country("Russia").markers.append("CTR")    # 20150616PS
                app.output_to_history("CTR Marker added Russia", True)    # 20150616PS
                if (app.get_country("Central Asia").is_ally()) or (app.get_country("Central Asia").is_neutral()):
                    app.get_country("Central Asia").markers.append("CTR")    # 20150616PS
                    app.output_to_history("CTR Marker added in Central Asia", True)    # 20150616PS
            elif self.number == 4:  # Moro Talks
                app.markers.append("Moro Talks")
                app.output_to_history("Moro Talks in play.", False)
                app.test_country("Philippines")
                app.change_funding(-1)
            elif self.number == 5:  # NEST
                app.markers.append("NEST")
                app.output_to_history("NEST in play. If jihadists have WMD, all plots in the US placed face up.", True)
            elif self.number in [6, 7]:  # Sanctions
                if "Patriot Act" in app.markers:
                    app.change_funding(-2)
                else:
                    return False
            elif self.number == 8 or self.number == 9 or self.number == 10:  # Special Forces
                while True:
                    country_name = app.get_country_from_user("Remove a cell from which country that has troops or is adjacent" +
                                                   " to a country with troops (? for list)?: ",  "XXX",
                                                             app.list_countries_with_cell_and_adjacent_troops)
                    if country_name == "":
                        print ""
                        return
                    else:
                        if app.map[country_name].total_cells(True) <= 0:
                            print "There are no cells in %s" % country_name
                            print ""
                        else:
                            foundTroops = False
                            for country in app.map:
                                if country == country_name or app.is_adjacent(country_name, country):
                                    if app.get_country(country).troops() > 0:
                                        foundTroops = True
                                        break
                            if not foundTroops:
                                print "Neither this or any adjacent country have troops."
                                print ""
                            else:
                                app.remove_cell(country_name, side)    # 20150131PS added side
                                app.output_to_history(app.map[country_name].summary(), True)
                                break
            elif self.number == 11:  # Abbas
                islamist_rule_adjacent_to_israel =\
                    app.contains_country(lambda c: app.is_adjacent(c.name, "Israel") and c.is_islamist_rule())
                app.markers.append("Abbas")
                app.output_to_history("Abbas in play.", False)
                if app.troops >= 5 and not islamist_rule_adjacent_to_israel:
                    app.change_prestige(1, False)
                    app.change_funding(-2, True)
            elif self.number == 12:  # Al-Azhar
                app.test_country("Egypt")
                numIR = app.num_islamist_rule()
                if numIR <= 0:
                    app.change_funding(-4, True)
                else:
                    app.change_funding(-2, True)
            elif self.number == 13:  # Anbar Awakening
                if (app.get_country("Iraq").troops() > 0) or (app.get_country("Syria").troops() > 0):
                    app.markers.append("Anbar Awakening")
                    app.output_to_history("Anbar Awakening in play.", False)
                    if app.get_country("Iraq").troops() == 0:
                        app.get_country("Syria").aid += 1 #20150131PS changed to add rather than set to 1
                        app.output_to_history("Aid in Syria.", False)
                    elif app.get_country("Syria").troops() == 0:
                        app.get_country("Iraq").aid += 1    #20150131PS changed to add rather than set to 1
                        app.output_to_history("Aid in Iraq.", False)
                    else:
                        print "There are troops in both Iraq and Syria."
                        if app.get_yes_no_from_user("Do you want to add the Aid to Iraq? (y/n): "):
                            app.get_country("Iraq").aid += 1
                            app.output_to_history("Aid in Iraq.", False)
                        else:
                            app.get_country("Syria").aid += 1
                            app.output_to_history("Aid in Syria.", False)
                    app.change_prestige(1, False)
                    print ""
                else:
                    return False
            elif self.number == 14:  # Covert Action
                adversary_names = [country.name for country in app.map.values() if country.is_adversary()]
                target_country = None
                if not adversary_names:
                    return False
                elif len(adversary_names) == 1:
                    target_country = adversary_names[0]
                else:
                    while not target_country:
                        country_name = app.get_country_from_user(
                            "Choose an Adversary country to attempt Covert Action (? for list): ", "XXX",
                            app.list_adversary_countries)
                        if country_name == "":
                            print ""
                            return
                        elif app.map[country_name].is_adversary():
                            target_country = country_name
                        else:
                            print "%s is not an Adversary." % country_name
                            print ""
                action_roll = app.get_roll("covert action")
                if action_roll >= 4:
                    app.map[target_country].make_neutral()
                    app.output_to_history("Covert Action successful, %s now Neutral." % target_country, False)
                    app.output_to_history(app.map[target_country].summary(), True)
                else:
                    app.output_to_history("Covert Action fails.", True)
            elif self.number == 15:  # Ethiopia Strikes
                if (app.get_country("Somalia").is_islamist_rule()) or (app.get_country("Sudan").is_islamist_rule()):
                    if not app.get_country("Somalia").is_islamist_rule():
                        app.get_country("Sudan").make_poor()
                        app.get_country("Sudan").make_neutral()
                        app.output_to_history("Sudan now Poor Neutral.", False)
                        app.output_to_history(app.get_country("Sudan").summary(), True)
                    elif not app.get_country("Sudan").is_islamist_rule():
                        app.get_country("Somalia").make_poor()
                        app.get_country("Somalia").make_neutral()
                        app.output_to_history("Somalia now Poor Neutral.", False)
                        app.output_to_history(app.get_country("Somalia").summary(), True)
                    else:
                        print "Both Somalia and Sudan are under Islamist Rule."
                        if app.get_yes_no_from_user("Do you want Somalia to be set to Poor Neutral? (y/n): "):
                            app.get_country("Somalia").make_poor()
                            app.get_country("Somalia").make_neutral()
                            app.output_to_history("Somalia now Poor Neutral.", False)
                            app.output_to_history(app.get_country("Somalia").summary(), True)
                        else:
                            app.get_country("Sudan").make_poor()
                            app.get_country("Sudan").make_neutral()
                            app.output_to_history("Sudan now Poor Neutral.", False)
                            app.output_to_history(app.get_country("Sudan").summary(), True)
                    print ""
                else:
                    return False
            elif self.number == 16:  # Euro-Islam
                posture = app.get_posture_from_user("Select Benelux's Posture (hard or soft): ")
                app.execute_card_euro_islam(posture)
            elif self.number == 17:  # FSB
                app.output_to_history("Examine Jihadist hand for Loose Nukes, HEU, or Kazakh Strain.", False)
                hasThem = app.get_yes_no_from_user("Does the Jihadist hand have Loose Nukes, HEU, or Kazakh Strain? (y/n): ")
                if hasThem:
                    app.output_to_history("Discard Loose Nukes, HEU, or Kazakh Strain from the Jihadist hand.", False)
                else:
                    russiaCells = app.get_country("Russia").total_cells(True)
                    cenAsiaCells = app.get_country("Central Asia").total_cells(True)
                    if russiaCells > 0 or cenAsiaCells > 0:
                        if russiaCells == 0:
                            app.remove_cell("Central Asia", side)    # 20150131PS added side
                            app.output_to_history(app.get_country("Central Asia").summary(), True)
                        elif cenAsiaCells == 0:
                            app.remove_cell("Russia", side)    # 20150131PS added side
                            app.output_to_history(app.get_country("Russia").summary(), True)
                        else:
                            isRussia = app.get_yes_no_from_user("There are cells in both Russia and Central Asia. Do you want to remove a cell in Russia? (y/n): ")
                            if isRussia:
                                app.remove_cell("Russia", side)    # 20150131PS added side
                                app.output_to_history(app.get_country("Russia").summary(), True)
                            else:
                                app.remove_cell("Central Asia", side)    # 20150131PS added side
                                app.output_to_history(app.get_country("Central Asia").summary(), False)
                    else:
                        app.output_to_history("There are no cells in Russia or Central Asia.", False)
                app.output_to_history("Shuffle Jihadist hand.", True)
            elif self.number == 18:  # Intel Community
                app.output_to_history("Examine Jihadist hand. Do not change order of cards.", False)
                app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime_change, withdraw, or war_of_ideas).", False)
                app.output_to_history("You may now interrupt this action phase to play another card (Use the u command).", True)
            elif self.number == 19:  # Kemalist Republic
                app.output_to_history("Turkey now a Fair Ally.", False)
                app.get_country("Turkey").make_fair()
                app.get_country("Turkey").make_ally()
                app.output_to_history(app.get_country("Turkey").summary(), True)
            elif self.number == 20:  # King Abdullah
                app.output_to_history("Jordan now a Fair Ally.", False)
                app.get_country("Jordan").make_fair()
                app.get_country("Jordan").make_ally()
                app.output_to_history(app.get_country("Jordan").summary(), True)
                app.change_prestige(1)
                app.change_funding(-1)
            elif self.number == 21:  # Let's Roll
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
            elif self.number == 22:  # Mossad and Shin Bet
                app.remove_all_cells_from_country("Israel")
                app.remove_all_cells_from_country("Jordan")
                app.remove_all_cells_from_country("Lebanon")
                app.output_to_history("", False)
            elif self.number in [23, 24, 25]:  # Predator
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
                        elif country.type == "Iran":
                            print "Iran is not allowed."
                            print ""
                        elif country.type == "Non-Muslim":
                            print "Choose a Muslim country."
                            print ""
                        else:
                            app.remove_cell(country.name, side)    # 20150131PS added side
                            app.output_to_history(country.summary())
                            break
            elif self.number == 26:  # Quartet
                if "Abbas" not in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                for country in app.get_countries():
                    if app.is_adjacent(country.name, "Israel") and country.is_islamist_rule():
                        return False
                app.change_prestige(2)
                app.change_funding(-3)
                app.output_to_history("", False)
            elif self.number == 27:  # Saddam Captured
                if app.get_country("Iraq").troops() == 0:
                    return False
                app.markers.append("Saddam Captured")
                app.get_country("Iraq").aid += 1
                app.output_to_history("Aid added in Iraq", False)
                app.change_prestige(1)
                app.output_to_history(app.get_country("Iraq").summary(), True)
            elif self.number == 28:  # Sharia
                num_besieged = app.num_besieged()
                if num_besieged <= 0:
                    return False
                elif num_besieged == 1:
                    target_country = app.find_countries(lambda c: c.besieged > 0)[0]
                else:
                    while True:
                        country_name = app.get_country_from_user(
                            "Choose a country with a Besieged Regime marker to remove (? for list): ", "XXX",
                            app.list_besieged_countries)
                        if country_name == "":
                            print ""
                            return
                        else:
                            target_country = app.get_country(country_name)
                            if target_country.besieged <= 0:
                                print "%s is not a Besieged Regime." % country_name
                                print ""
                            else:
                                break
                target_country.besieged = 0
                app.output_to_history("%s is no longer a Besieged Regime." % target_country.name, False)
                app.output_to_history(target_country.summary())
            elif self.number == 29:  # Tony Blair
                app.set_posture("United Kingdom", app.us_posture())
                app.output_to_history("United Kingdom posture now %s" % app.get_posture("United Kingdom"), False)
                print "You may roll War of Ideas in up to 3 Schengen countries."
                for i in range(3):
                    target_name = ""
                    finished_picking = False
                    while not target_name:
                        country_name = app.get_country_from_user(
                            "Choose Schengen country to make a WoI roll (done to stop rolling) (? for list)?: ", "done",
                            app.list_schengen_countries)
                        if country_name == "":
                            print ""
                            return
                        elif country_name == "done":
                            finished_picking = True
                            break
                        else:
                            if not app.map[country_name].schengen:
                                print "%s is not a Schengen country." % country_name
                                print ""
                                return
                            else:
                                target_name = country_name
                                posture_roll = app.get_roll("posture")
                                app.execute_non_muslim_woi(target_name, posture_roll)
                    if finished_picking:
                        break
                app.output_to_history("", False)
            elif self.number == 30:  # UN Nation Building
                num_regime_change = app.num_regime_change()
                if num_regime_change <= 0 or "Vieira de Mello Slain" in app.markers:
                    return False
                target_country = None
                if num_regime_change == 1:
                    for country in app.get_countries():
                        if country.regimeChange > 0:
                            target_country = country
                            break
                else:
                    while True:
                        country_name = app.get_country_from_user(
                            "Choose a Regime Change country (? for list): ", "XXX", app.list_regime_change_countries)
                        if country_name == "":
                            print ""
                            return
                        else:
                            target_country = app.get_country(country_name)
                            if target_country.regimeChange <= 0:
                                print "%s is not a Regime Change country." % country_name
                                print ""
                            else:
                                break
                target_country.aid += 1
                app.output_to_history("Aid added to %s." % target_country.name, False)
                woi_roll = app.get_roll("WoI")
                modified_woi_roll = app.modified_woi_roll(woi_roll, target_country.name, False)
                app.handle_muslim_woi(modified_woi_roll, target_country.name)
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country in ["United States", "United Kingdom", "Canada"]:
                    if app.get_country(country).activeCells > 0:
                        num = app.get_country(country).activeCells
                        if num > 0:
                            app.get_country(country).activeCells -= num
                            app.cells += num
                            app.output_to_history("%d Active Cell(s) removed from %s." % (num, country), False)
                    if app.get_country(country).sleeperCells > 0:
                        num = app.get_country(country).sleeperCells
                        if num > 0:
                            app.get_country(country).sleeperCells -= num
                            app.cells += num
                            app.output_to_history("%d Sleeper Cell(s) removed from %s." % (num, country), False)
                    if app.get_country(country).cadre > 0:
                        num = app.get_country(country).cadre
                        if num > 0:
                            app.get_country(country).cadre = 0
                            app.output_to_history("Cadre removed from %s." % country, False)
                    if app.get_country(country).plots > 0:
                        num = app.get_country(country).plots
                        if num > 0:
                            app.get_country(country).plots -= num
                            app.output_to_history("%d Plots remove(d) from %s." % (num, country), False)
                app.markers.append("Wiretapping")
                app.output_to_history("Draw a card.")
                app.output_to_history("Wiretapping in Play.")
            elif self.number == 32:  # Back Channel
                if app.us().is_hard():
                    return False
                num_adversaries = app.num_adversary()
                if num_adversaries <= 0:
                    return False
                if app.get_yes_no_from_user("Do you want to discard a card with a value that exactly matches"
                                            " an Adversary's Resources? (y/n): "):
                    while True:
                        country_name = app.get_country_from_user(
                            "Choose an Adversary country (? for list): ", "XXX", app.list_adversary_countries)
                        if country_name == "":
                            print ""
                            return False
                        else:
                            adversary = app.get_country(country_name)
                            if not adversary.is_adversary():
                                print "%s is not an Adversary country." % country_name
                                print ""
                            else:
                                adversary.make_neutral()
                                app.output_to_history("%s now Neutral" % country_name, False)
                                adversary.aid += 1
                                app.output_to_history("Aid added to %s." % country_name, False)
                                app.output_to_history(adversary.summary())
                                break
            elif self.number == 33:  # Benazir Bhutto
                app.markers.append("Benazir Bhutto")
                app.output_to_history("Benazir Bhutto in Play.", False)
                if app.get_country("Pakistan").is_poor():
                    app.get_country("Pakistan").make_fair()
                    app.output_to_history("Pakistan now Fair governance.", False)
                app.output_to_history("No Jihads in Pakistan.", False)
                app.output_to_history(app.get_country("Pakistan").summary(), True)
            elif self.number == 34:  # Enhanced Measures
                app.markers.append("Enhanced Measures")
                app.output_to_history("Enhanced Measures in Play.", False)
                app.output_to_history("Take a random card from the Jihadist hand.", False)
                app.disrupt_cells_or_cadre()
                app.output_to_history("", False)
            elif self.number == 35:  # Hajib
                app.test_country("Turkey")
                app.get_country("Turkey").improve_governance()
                app.output_to_history("Turkey Governance now %s." % app.get_country("Turkey").governance_str(), False)
                app.change_funding(-2)
                posture = app.get_posture_from_user("Select Frances's Posture (hard or soft): ")
                app.set_posture("France", posture)
                app.output_to_history(app.get_country("Turkey").summary(), False)
                app.output_to_history(app.get_country("France").summary(), True)
            elif self.number == 36:  # Indo-Pakistani Talks
                app.markers.append("Indo-Pakistani Talks")
                app.output_to_history("Indo-Pakistani Talks in Play.", False)
                app.get_country('Pakistan').make_ally()
                app.output_to_history("Pakistan now Ally", False)
                posture = app.get_posture_from_user("Select India's Posture (hard or soft): ")
                app.set_posture("India", posture)
                app.output_to_history(app.get_country("Pakistan").summary(), False)
                app.output_to_history(app.get_country("India").summary(), True)
            elif self.number == 37:  # Iraqi WMD
                app.markers.append("Iraqi WMD")
                app.output_to_history("Iraqi WMD in Play.", False)
                app.output_to_history("Use this or a later card for Regime Change in Iraq at any Governance.", True)
            elif self.number == 38:  # Libyan Deal
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
            elif self.number == 39:  # Libyan WMD
                app.markers.append("Libyan WMD")
                app.output_to_history("Libyan WMD in Play.", False)
                app.output_to_history("Use this or a later card for Regime Change in Libya at any Governance.", True)
            elif self.number == 40:  # Mass Turnout
                target_country = None
                num_regime_change = app.num_regime_change()
                if num_regime_change <= 0:
                    return False
                elif num_regime_change == 1:
                    target_country = app.find_countries(lambda c: c.regimeChange > 0)[0]
                else:
                    while True:
                        country_name = app.get_country_from_user(
                            "Choose a Regime Change Country to improve governance (? for list): ", "XXX",
                            app.list_regime_change_countries)
                        if country_name == "":
                            print ""
                            return
                        else:
                            target_country = app.get_country(country_name)
                            if target_country.regimeChange <= 0:
                                print "%s is not a Regime Change country." % country_name
                                print ""
                            else:
                                break
                app.improve_governance(target_country.name)
                app.output_to_history("%s Governance improved." % target_country.name, False)
                app.output_to_history(target_country.summary())
            elif self.number == 41:  # NATO
                num_regime_change = app.num_regime_change()
                if num_regime_change <= 0:
                    return False
                elif num_regime_change == 1:
                    target_country = app.find_countries(lambda c: c.regimeChange > 0)[0]
                else:
                    while True:
                        country_name = app.get_country_from_user(
                            "Choose a Regime Change Country to land NATO troops (? for list): ", "XXX",
                            app.list_regime_change_countries)
                        if country_name == "":
                            print ""
                            return
                        else:
                            target_country = app.get_country(country_name)
                            if target_country.regimeChange <= 0:
                                print "%s is not a Regime Change country." % country_name
                                print ""
                            else:
                                break
                target_country.markers.append("NATO")
                app.output_to_history("NATO added in %s" % target_country.name, False)
                target_country.aid += 1
                app.output_to_history("Aid added in %s" % target_country.name, False)
                app.output_to_history(target_country.summary())
            elif self.number == 42:  # Pakistani Offensive
                if "FATA" in app.get_country("Pakistan").markers:
                    app.get_country("Pakistan").markers.remove("FATA")
                    app.output_to_history("FATA removed from Pakistan", True)
            elif self.number == 43:  # Patriot Act
                app.markers.append("Patriot Act")
            elif self.number == 44:  # Renditions
                app.markers.append("Renditions")
                app.output_to_history("Renditions in Play.", False)
                app.output_to_history("Discard a random card from the Jihadist hand.", False)
                if app.num_disruptable() > 0:
                    app.disrupt_cells_or_cadre()
                app.output_to_history("", False)
            elif self.number == 45:  # Safer Now
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
            elif self.number == 46:  # Sistani
                target_countries = [c.name for c in app.get_countries() if
                                    c.type == "Shia-Mix" and c.regimeChange > 0 and c.total_cells(True) > 0]
                target_name = None
                if len(target_countries) == 1:
                    target_name = target_countries[0]
                else:
                    while not target_name:
                        country_name = app.get_country_from_user(
                            "Choose a Shia-Mix Regime Change Country with a cell to improve governance (? for list): ",
                            "XXX", app.list_shia_mix_regime_change_countries_with_cells)
                        if country_name == "":
                            print ""
                        else:
                            if country_name not in target_countries:
                                print "%s is not a Shia-Mix Regime Change Country with a cell." % country_name
                                print ""
                            else:
                                target_name = country_name
                                break
                app.improve_governance(target_name)
                app.output_to_history("%s Governance improved." % target_name, False)
                app.output_to_history(app.get_country(target_name).summary())
            elif self.number == 47:  # The door of Itjihad was closed
                app.lapsing.append("The door of Itjihad was closed")
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if self.number == 48:  # Adam Gadahn
                card_num = app.get_card_num_from_user(
                    "Enter the number of the next Jihadist card or none if there are none left: ")
                if card_num == "none":
                    app.output_to_history("No cards left to recruit to US.", True)
                    return
                ops = app.deck.get(card_num).ops
                rolls = app.randomizer.roll_d6(ops)
                app.execute_recruit("United States", ops, rolls, 2)
            elif self.number == 49:  # Al-Ittihad al-Islami
                app.place_cells("Somalia", 1)
            elif self.number == 50:  # Ansar al-Islam
                possible = ["Iraq", "Iran"]
                target_name = random.choice(possible)
                app.place_cells(target_name, 1)
            elif self.number == 51:  # FREs
                if "Saddam Captured" in app.markers:
                    cells_to_move = 2
                else:
                    cells_to_move = 4
                cells_to_move = min(cells_to_move, app.cells)
                app.place_cells("Iraq", cells_to_move)
            elif self.number == 52:  # IDEs
                app.output_to_history("US randomly discards one card.", True)
            elif self.number == 53:  # Madrassas
                app.handle_recruit(1, True)
                card_num = app.get_card_num_from_user(
                    "Enter the number of the next Jihadist card or none if there are none left: ")
                if card_num == "none":
                    app.output_to_history("No cards left to recruit.", True)
                    return
                ops = app.deck.get(card_num).ops
                app.handle_recruit(ops, True)
            elif self.number == 54:  # Moqtada al-Sadr
                app.get_country("Iraq").markers.append("Sadr")
                app.output_to_history("Sadr Marker added in Iraq", True)
            elif self.number == 55:  # Uyghur Jihad
                app.test_country("China")
                if app.cells > 0:
                    if app.get_posture("China") == "Soft":
                        app.place_cell("China")
                    else:
                        app.place_cell("Central Asia")
                else:
                    app.output_to_history("No cells to place.", True)
            elif self.number == 56:  # Vieira de Mello Slain
                app.markers.append("Vieira de Mello Slain")
                app.output_to_history("Vieira de Mello Slain in play.", False)
                app.change_prestige(-1)
            elif self.number == 57:  # Abu Sayyaf
                app.place_cells("Philippines", 1)
                app.markers.append("Abu Sayyaf")
            elif self.number == 58:  # Al-Anbar
                app.markers.append("Al-Anbar")
                app.output_to_history("Al-Anbar in play.", True)
                app.test_country("Iraq")
                if app.cells > 0:
                    app.place_cell("Iraq")
            elif self.number == 59:  # Amerithrax
                app.output_to_history("US side discards its highest-value US-associated event card, if it has any.")
            elif self.number == 60:  # Bhutto Shot
                app.markers.append("Bhutto Shot")
                app.output_to_history("Bhutto Shot in play.", True)
            elif self.number == 61:  # Detainee Release
                if app.cells > 0:
                    target_name = None
                    while not target_name:
                        country_name = app.get_country_from_user(
                            "Choose a country where Disrupt occured this or last Action Phase: ", "XXX", None)
                        if country_name == "":
                            print ""
                            return
                        else:
                            target_name = country_name
                            break
                    app.place_cell(target_name)
                app.output_to_history("Draw a card for the Jihadist and put it on the top of their hand.", True)
            elif self.number == 62:  # Ex-KGB
                if "CTR" in app.get_country("Russia").markers:
                    app.get_country("Russia").markers.remove("CTR")
                    app.output_to_history("CTR removed from Russia.", True)
                else:
                    target_caucasus = False
                    if app.get_posture("Caucasus") in [None, "", app.us_posture()]:
                        if app.gwot_penalty() == 0:
                            caucasus_posture = app.get_posture("Caucasus")
                            if app.us().is_hard():
                                app.set_posture("Caucasus", "Soft")
                            else:
                                app.set_posture("Caucasus", "Hard")
                            if app.gwot_penalty() < 0:
                                target_caucasus = True
                            app.set_posture("Caucasus", caucasus_posture)
                    if target_caucasus:
                        if app.us().is_hard():
                            app.set_posture("Caucasus", "Soft")
                        else:
                            app.set_posture("Caucasus", "Hard")
                        app.output_to_history("Caucasus posture now %s" % app.get_posture("Caucasus"), False)
                        app.output_to_history(app.get_country("Caucasus").summary(), True)
                    else:
                        app.test_country("Central Asia")
                        if app.get_country("Central Asia").is_ally():
                            app.get_country("Central Asia").make_neutral()
                            app.output_to_history("Central Asia now Neutral.", True)
                        elif app.get_country("Central Asia").is_neutral():
                            app.get_country("Central Asia").make_adversary()
                            app.output_to_history("Central Asia now Adversary.", True)
                        app.output_to_history(app.get_country("Central Asia").summary(), True)
            elif self.number == 63:  # Gaza War
                app.change_funding(1)
                app.change_prestige(-1)
                app.output_to_history("US discards a random card.", True)
            elif self.number == 64:  # Hariri Killed
                app.test_country("Lebanon")
                app.test_country("Syria")
                app.get_country("Syria").make_adversary()
                app.output_to_history("Syria now Adversary.", False)
                if app.get_country("Syria").governance_is_better_than(POOR):
                    app.worsen_governance("Syria")
                    app.output_to_history("Governance in Syria worsened.", False)
                    app.output_to_history(app.get_country("Syria").summary(), True)
                app.output_to_history(app.get_country("Lebanon").summary(), True)
            elif self.number == 65:  # HEU
                possibles = []
                if app.get_country("Russia").total_cells() > 0 and "CTR" not in app.get_country("Russia").markers:
                    possibles.append("Russia")
                central_asia = app.get_country("Central Asia")
                if central_asia.total_cells() > 0 and "CTR" not in central_asia.markers:
                    possibles.append("Central Asia")
                target_name = random.choice(possibles)
                roll = random.randint(1, 6)
                app.execute_card_heu(target_name, roll)
            elif self.number == 66:  # Homegrown
                app.place_cells("United Kingdom", 1)
            elif self.number == 67:  # Islamic Jihad Union
                app.place_cells("Central Asia", 1)
                if app.cells > 0:
                    app.place_cells("Afghanistan", 1)
            elif self.number == 68:  # Jemaah Islamiya
                app.place_cells("Indonesia/Malaysia", 2)
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
                app.set_posture("Germany", "Soft")
                app.output_to_history("%s Posture now %s" % ("Germany", app.get_posture("Germany")), True)
                app.set_posture("France", "Soft")
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
                    app.set_posture("United States", "Hard")
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
                possibles = app.find_countries(lambda c: c.regimeChange > 0)
                if not possibles:
                    return False
                target = random.choice(possibles)
                app.place_cells(target.name, 5)
                if target.aid > 0:
                    target.aid -= 1
                    app.output_to_history("Aid removed from %s" % target.name, False)
                else:
                    target.besieged = 1
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
                    app.set_posture("United States", "Soft")
                else:
                    app.set_posture("United States", "Hard")
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
                possibles = app.find_countries(lambda c: c.type == "Shia-Mix")
                target = random.choice(possibles)
                app.place_cells(target.name, 1)
            elif self.number in [87, 88, 89]:  # Martyrdom Operation
                if app.execute_plot(1, False, [1], True) == 1:
                    app.output_to_history("No plots could be placed.")
                    app.handle_radicalization(app.card(self.number).ops)
            elif self.number == 90:  # Quagmire
                app.set_posture("United States", "Soft")
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
                app.get_country("Afghanistan").besieged = 1
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
                if app.us().is_soft():
                    app.set_posture("Serbia", "Hard")
                else:
                    app.set_posture("Serbia", "Soft")
                app.output_to_history("Serbia Posture now %s." % app.get_posture("Serbia"), True)
            elif self.number == 102:  # Former Soviet Union
                testRoll = random.randint(1, 6)
                if testRoll <= 4:
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
                    for country in one_away:
                        if country not in possibles and app.get_country(country).total_cells(True) > 0 and app.get_country(country).type == "Shia-Mix":
                            possibles.append(country)
                    for country in two_away:
                        if country not in possibles and app.get_country(country).total_cells(True) > 0 and app.get_country(country).type == "Shia-Mix":
                            possibles.append(country)
                    for country in three_away:
                        if country not in possibles and app.get_country(country).total_cells(True) > 0 and app.get_country(country).type == "Shia-Mix":
                            possibles.append(country)
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
                            if app.get_country(country_name).type == "Shia-Mix":
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
                    possibles = [country.name for country in app.get_countries() if country.type == "Shia-Mix"]
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
                                 country.type == "Shia-Mix" and country.troops() > 0 and country.total_cells() > 0]
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
                else:   # jihadist play
                    possibles = [country.name for country in app.get_countries() if country.type == "Shia-Mix"]
                    target_name = random.choice(possibles)
                    app.test_country(target_name)
                    tested = target_name
                    target_name = None
                    good_countries = [c.name for c in app.get_countries() if c.is_muslim() and c.is_good()]
                    if len(good_countries) > 1:
                        distances = []
                        for country in good_countries:
                            distances.append((app.country_distance(tested, country), country))
                        distances.sort()
                        target_name = distances[0][1]
                    elif len(good_countries) == 1:
                        target_name = good_countries[0]
                    else:
                        fair_countries = [c.name for c in app.get_countries() if c.is_muslim() and c.is_fair()]
                        if len(fair_countries) > 1:
                            distances = []
                            for country in fair_countries:
                                distances.append((app.country_distance(tested, country), country))
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
                    app.get_country("Iraq").aid += 1
                    app.output_to_history("Aid added to Iraq.", False)
                    app.output_to_history(app.get_country("Iraq").summary(), True)
                else:
                    app.test_country("Turkey")
                    possibles = []
                    if app.get_country("Turkey").governance_is_better_than(POOR):
                        possibles.append("Turkey")
                    if app.get_country("Iraq").is_governed() and app.get_country("Iraq").governance_is_better_than(POOR):
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
                            if app.get_country(country).aid > 0:
                                country_scores[country] += 10000
                            if app.get_country(country).besieged > 0:
                                country_scores[country] += 1000
                            country_scores[country] += (app.country_resources_by_name(country) * 100)
                            country_scores[country] += random.randint(1, 99)
                        country_order = []
                        for country in country_scores:
                            country_order.append((country_scores[country], (app.get_country(country).total_cells(True)), country))
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
                possibles = [c.name for c in app.get_countries() if c.regimeChange > 0 and c.total_cells() >= 2]
                target_name = None
                if len(possibles) == 0:
                    return False
                if len(possibles) == 1:
                    target_name = possibles[0]
                else:
                    if side == "US":
                        app.output_to_history("US draws one card.", False)
                        while not target_name:
                            country_name = app.get_country_from_user("Choose a Regime Change country with at least 2 troops. (? for list)?: ", "XXX", app.list_regime_change_with_two_cells)
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
                    app.get_country("Sudan").aid += 1
                    app.output_to_history("Aid added to Sudan.", False)
                    if app.get_country("Sudan").is_adversary():
                        app.get_country("Sudan").make_neutral()
                        app.output_to_history("Sudan alignment improved.", False)
                    elif app.get_country("Sudan").is_neutral():
                        app.get_country("Sudan").make_ally()
                        app.output_to_history("Sudan alignment improved.", False)
                else:
                    app.get_country("Sudan").besieged = 1
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
                app.output_to_history("GTMO in play. No recruit operations or Detainee Release the rest of this turn.", False)
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
                            if app.get_country(country).type == "Non-Muslim":
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
                                    print "%s is not Indonesia or an adjacent country that has a cell and is Ally or Hard." % country_name
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
                            if app.get_country(country).type == "Non-Muslim":
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
                            if country.is_ally() or country.type == "Non-Muslim":
                                num_plots = country.plots
                                country.plots = 0
                                app.output_to_history("%d Plots removed from %s." % (num_plots, country.name), False)
                    app.output_to_history("US draws 2 cards.", True)
                else:
                    if app.execute_plot(1, False, [1], False, False, True) == 1:
                        app.output_to_history("No plots could be placed.", True)
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                app.lapsing.append("Oil Price Spike")
                app.output_to_history("Oil Price Spike in play. Add +1 to the resources of each Oil Exporter country for the turn.", False)
                if side == "US":
                    app.output_to_history(
                        "Select, reveal, and draw a card other than Oil Price Spike from the discard pile or a box.")
                else:
                    if app.get_yes_no_from_user("Are there any Jihadist event cards in the discard pile? "):
                        app.output_to_history("Draw from the Discard Pile randomly among the highest-value Jihadist-associated event cards. Put the card on top of the Jihadist hand.", True)
            elif self.number == 119:  # Saleh
                app.test_country("Yemen")
                if side == "US":
                    if not app.get_country("Yemen").is_islamist_rule():
                        if app.get_country("Yemen").is_adversary():
                            app.get_country("Yemen").make_neutral()
                        elif app.get_country("Yemen").is_neutral():
                            app.get_country("Yemen").make_ally()
                        app.output_to_history("Yemen Alignment improved to %s." % app.get_country("Yemen").alignment(), False)
                        app.get_country("Yemen").aid += 1
                        app.output_to_history("Aid added to Yemen.", True)
                else:
                    if app.get_country("Yemen").is_ally():
                        app.get_country("Yemen").make_neutral()
                    elif app.get_country("Yemen").is_neutral():
                        app.get_country("Yemen").make_adversary()
                    app.output_to_history("Yemen Alignment worsened to %s." % app.get_country("Yemen").alignment(), False)
                    app.get_country("Yemen").besieged = 1
                    app.output_to_history("Yemen now Besieged Regime.", True)
            elif self.number == 120:  # US Election
                app.execute_card_us_election(random.randint(1, 6))
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)

