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
                for country in app.map:
                    if (app.map[country].type != "Non-Muslim") and (app.map[country].plots > 0):
                        return True
                return False
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 3:  # CTR    20150616PS
                return app.map["United States"].posture == "Soft"
            elif self.number == 2:  # Biometrics
                return True
            elif self.number == 4:  # Moro Talks
                return True
            elif self.number == 5:  # NEST
                return True
            elif self.number == 6 or self.number == 7 :  # Sanctions
                return "Patriot Act" in app.markers
            elif self.number == 8 or self.number == 9 or self.number == 10:  # Special Forces
                for country in app.map:
                    if app.map[country].totalCells(True) > 0:
                        for subCountry in app.map:
                            if country == subCountry or app.isAdjacent(subCountry, country):
                                if app.map[subCountry].troops() > 0:
                                    return True
                return False
            elif self.number == 11:  # Abbas
                return True
            elif self.number == 12:  # Al-Azhar
                return True
            elif self.number == 13:  # Anbar Awakening
                return (app.map["Iraq"].troops() > 0) or (app.map["Syria"].troops() > 0)
            elif self.number == 14:  # Covert Action
                for country in app.map:
                    if app.map[country].is_adversary():
                        return True
                return False
            elif self.number == 15:  # Ethiopia Strikes
                return (app.map["Somalia"].is_islamist_rule()) or (app.map["Sudan"].is_islamist_rule())
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
                allyGoodPlotCountries = 0
                for country in app.map:
                    if app.map[country].plots > 0:
                        if app.map[country].is_ally() or app.map[country].is_good():
                            allyGoodPlotCountries += 1
                return allyGoodPlotCountries > 0
            elif self.number == 22:  # Mossad and Shin Bet
                targetCells = 0
                targetCells += app.map["Israel"].totalCells()
                targetCells += app.map["Jordan"].totalCells()
                targetCells += app.map["Lebanon"].totalCells()
                return targetCells > 0
            elif self.number == 23 or self.number == 24 or self.number == 25:  # Predator
                numMuslimCellCountries = 0
                for country in app.map:
                    if app.map[country].totalCells(True) > 0:
                        if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                            numMuslimCellCountries += 1
                return numMuslimCellCountries > 0
            elif self.number == 26:  # Quartet
                if not "Abbas" in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            return False
                return True
            elif self.number == 27:  # Saddam Captured
                return app.map["Iraq"].troops() > 0
            elif self.number == 28:  # Sharia
                return app.numBesieged() > 0
            elif self.number == 29:  # Tony Blair
                return True
            elif self.number == 30:  # UN Nation Building
                numRC = app.numRegimeChange()
                return (numRC > 0) and ("Vieira de Mello Slain" not in app.markers)
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country in ["United States", "United Kingdom", "Canada"]:
                    if app.map[country].totalCells() > 0 or app.map[country].cadre > 0 or app.map[country].plots > 0:
                        return True
                return False
            elif self.number == 32:  # Back Channel
                if app.map["United States"].posture == "Hard":
                    return False
                numAdv = app.numAdversary()
                if numAdv <= 0:
                    return False
                app.listAdversaryCountries()
                return app.getYesNoFromUser("Do you have a card with a value that exactly matches an Adversary's Resources? (y/n): ")
            elif self.number == 33:  # Benazir Bhutto
                if "Bhutto Shot" in app.markers:
                    return False
                if app.map["Pakistan"].is_islamist_rule():
                    return False
                for countryObj in app.map["Pakistan"].links:
                    if countryObj.is_islamist_rule():
                        return False
                return True
            elif self.number == 34:  # Enhanced Measures
                if "Leak-Enhanced Measures" in app.markers or app.map["United States"].posture == "Soft":
                    return False
                return app.num_disruptable() > 0
            elif self.number == 35:  # Hajib
                return app.numIslamistRule() == 0
            elif self.number == 36:  # Indo-Pakistani Talks
                if app.map['Pakistan'].is_good() or app.map['Pakistan'].is_fair():
                    return True
                return False
            elif self.number == 37:  # Iraqi WMD
                if app.map["United States"].posture == "Hard" and app.map["Iraq"].is_adversary():
                    return True
                return False
            elif self.number == 38:  # Libyan Deal
                if app.map["Libya"].is_poor():
                    if app.map["Iraq"].is_ally() or app.map["Syria"].is_ally():
                        return True
                return False
            elif self.number == 39:  # Libyan WMD
                if app.map["United States"].posture == "Hard" and app.map["Libya"].is_adversary() and "Libyan Deal" not in app.markers:
                    return True
                return False
            elif self.number == 40:  # Mass Turnout
                return app.numRegimeChange() > 0
            elif self.number == 41:  # NATO
                return (app.numRegimeChange() > 0) and (app.gwotPenalty() >= 0)
            elif self.number == 42:  # Pakistani Offensive
                return (app.map["Pakistan"].is_ally()) and ("FATA" in app.map["Pakistan"].markers)
            elif self.number == 43:  # Patriot Act
                return True
            elif self.number == 44:  # Renditions
                return (app.map["United States"].posture == "Hard") and ("Leak-Renditions" not in app.markers)
            elif self.number == 45:  # Safer Now
                if app.numIslamistRule() > 0:
                    return False
                for country in app.map:
                    if app.map[country].is_good():
                        if app.map[country].totalCells(True) > 0 or app.map[country].plots > 0:
                            return False
                return True
            elif self.number == 46:  # Sistani
                targetCountries = 0
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].regimeChange > 0:
                            if (app.map[country].totalCells(True)) > 0:
                                targetCountries += 1
                return targetCountries > 0
            elif self.number == 47:  # The door of Itjihad was closed
                return True
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 48:  # Adam Gadahn
                if app.numCellsAvailable() <= 0:
                    return False
                return app.getYesNoFromUser("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 49:  # Al-Ittihad al-Islami
                return True
            elif self.number == 50:  # Ansar al-Islam
                return app.map["Iraq"].governance_is_worse_than(GOOD)
            elif self.number == 51:  # FREs
                return app.map["Iraq"].troops() > 0
            elif self.number == 52:  # IDEs
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if (app.map[country].totalCells(True)) > 0:
                            return True
                return False
            elif self.number == 53:  # Madrassas
                return app.getYesNoFromUser("Is this the 1st card of the Jihadist Action Phase? (y/n): ")
            elif self.number == 54:  # Moqtada al-Sadr
                return app.map["Iraq"].troops() > 0
            elif self.number == 55:  # Uyghur Jihad
                return True
            elif self.number == 56:  # Vieira de Mello Slain
                for country in app.map:
                    if app.map[country].regimeChange > 0 and app.map[country].totalCells() > 0:
                        return True
                return False
            elif self.number == 57:  # Abu Sayyaf
                return "Moro Talks" not in app.markers
            elif self.number == 58:  # Al-Anbar
                return "Anbar Awakening" not in app.markers
            elif self.number == 59:  # Amerithrax
                return True
            elif self.number == 60:  # Bhutto Shot
                return app.map["Pakistan"].totalCells() > 0
            elif self.number == 61:  # Detainee Release
                if "GTMO" in app.lapsing or "Renditions" in app.markers:
                    return False
                return app.getYesNoFromUser("Did the US Disrupt during this or the last Action Phase? (y/n): ")
            elif self.number == 62:  # Ex-KGB
                return True
            elif self.number == 63:  # Gaza War
                return True
            elif self.number == 64:  # Hariri Killed
                return True
            elif self.number == 65:  # HEU
                possibles = 0
                if app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers:
                    possibles += 1
                if app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers:
                    possibles += 1
                return possibles > 0
            elif self.number == 66:  # Homegrown
                return True
            elif self.number == 67:  # Islamic Jihad Union
                return True
            elif self.number == 68:  # Jemaah Islamiya
                return True
            elif self.number == 69:  # Kazakh Strain
                return app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers
            elif self.number == 70:  # Lashkar-e-Tayyiba
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number == 71:  # Loose Nuke
                return app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers
            elif self.number == 72:  # Opium
                return app.map["Afghanistan"].totalCells() > 0
            elif self.number == 73:  # Pirates
                return app.map["Somalia"].is_islamist_rule() or app.map["Yemen"].is_islamist_rule()
            elif self.number == 74:  # Schengen Visas
                return True
            elif self.number == 75:  # Schroeder & Chirac
                return app.map["United States"].posture == "Hard"
            elif self.number == 76:  # Abu Ghurayb
                targetCountries = 0
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if (app.map[country].totalCells(True)) > 0:
                            targetCountries += 1
                return targetCountries > 0
            elif self.number == 77:  # Al Jazeera
                if app.map["Saudi Arabia"].troops() > 0:
                    return True
                for country in app.map:
                    if app.isAdjacent("Saudi Arabia", country):
                        if app.map[country].troops() > 0:
                            return True
                return False
            elif self.number == 78:  # Axis of Evil
                return True
            elif self.number == 79:  # Clean Operatives
                return True
            elif self.number == 80:  # FATA
                return True
            elif self.number == 81:  # Foreign Fighters
                return app.numRegimeChange() > 0
            elif self.number == 82:  # Jihadist Videos
                return True
            elif self.number == 83:  # Kashmir
                return "Indo-Pakistani Talks" not in app.markers
            elif self.number == 84 or self.number == 85:  # Leak
                return ("Enhanced Measures" in app.markers) or ("Renditions" in app.markers) or ("Wiretapping" in app.markers)
            elif self.number == 86:  # Lebanon War
                return True
            elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
                for country in app.map:
                    if not app.map[country].is_islamist_rule():
                        if app.map[country].totalCells(True) > 0:
                            return True
                return False
            elif self.number == 90:  # Quagmire
                if app.prestige >= 7:
                    return False
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells(True) > 0:
                            return True
                return False
            elif self.number == 91:  # Regional al-Qaeda
                num = 0
                for country in app.map:
                    if app.map[country].type == "Suni" or app.map[country].type == "Shia-Mix":
                        if app.map[country].is_ungoverned():
                            num += 1
                return num >= 2
            elif self.number == 92:  # Saddam
                if "Saddam Captured" in app.markers:
                    return False
                return (app.map["Iraq"].is_poor()) and (app.map["Iraq"].is_adversary())
            elif self.number == 93:  # Taliban
                return True
            elif self.number == 94:  # The door of Itjihad was closed
                return app.getYesNoFromUser("Was a country tested or improved to Fair or Good this or last Action Phase.? (y/n): ")
            elif self.number == 95:  # Wahhabism
                return True
        else:  # Unassociated Events
            if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 96:  # Danish Cartoons
                return True
            elif self.number == 97:  # Fatwa
                return app.getYesNoFromUser("Do both sides have cards remaining beyond this one? (y/n): ")
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
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].troops() > 0 and app.map[country].totalCells() > 0:
                            return True
                return False
            elif self.number == 107:  # Kurdistan
                return True
            elif self.number == 108:  # Musharraf
                if "Benazir Bhutto" in app.markers:
                    return False
                return app.map["Pakistan"].totalCells() > 0
            elif self.number == 109:  # Tora Bora
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells() >= 2:
                            return True
                return False
            elif self.number == 110:  # Zarqawi
                return app.map["Iraq"].troops() > 0 or app.map["Syria"].troops() > 0 or app.map["Lebanon"].troops() > 0 or app.map["Jordan"].troops() > 0
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    if "FATA" in app.map["Pakistan"].markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.numIslamistRule() == 0
                else:
                    return True
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    if "FATA" in app.map["Pakistan"].markers:
                        return False
                    if "Al-Anbar" in app.markers:
                        return False
                    return app.numIslamistRule() == 0
                else:
                    return True
            elif self.number == 113:  # Darfur
                return True
            elif self.number == 114:  # GTMO
                return True
            elif self.number == 115:  # Hambali
                possibles = ["Indonesia/Malaysia"]
                for countryObj in app.map["Indonesia/Malaysia"].links:
                    possibles.append(countryObj.name)
                for country in possibles:
                    if app.map[country].totalCells(True) > 0:
                        if app.map[country].type == "Non-Muslim":
                            if app.map[country].posture == "Hard":
                                return True
                        else:
                            if app.map[country].is_ally():
                                return True
            elif self.number == 116:  # KSM
                if side == "US":
                    for country in app.map:
                        if app.map[country].plots > 0:
                            if app.map[country].type == "Non-Muslim" or app.map[country].is_ally():
                                return True
                    return False
                else:
                    return True
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                return True
            elif self.number == 119:  # Saleh
                return True
            elif self.number == 120:  # US Election
                return True
            return False

    def putsCell(self, app):
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
        app.outputToHistory("Card played for Event.", True)
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 1:  # Backlash
                for country in app.map:
                    if (app.map[country].type != "Non-Muslim") and (app.map[country].plots > 0):
                        app.outputToHistory("Plot in Muslim country found. Select the plot during plot phase. Backlash in play", True)  #20150131PS
                        app.backlashInPlay = True
                        return True
                return False
            elif self.number == 2:  # Biometrics
                app.lapsing.append("Biometrics")
                app.outputToHistory("Biometrics in play. This turn, travel to adjacent Good countries must roll to succeed and no non-adjacent travel.", True)
            elif self.number == 3:  # CTR    20150616PS
                app.map["Russia"].markers.append("CTR")    # 20150616PS
                app.outputToHistory("CTR Marker added Russia", True)    # 20150616PS
                if (app.map["Central Asia"].is_ally()) or (app.map["Central Asia"].is_neutral()):
                    app.map["Central Asia"].markers.append("CTR")    # 20150616PS
                    app.outputToHistory("CTR Marker added in Central Asia", True)    # 20150616PS
            elif self.number == 4:  # Moro Talks
                app.markers.append("Moro Talks")
                app.outputToHistory("Moro Talks in play.", False)
                app.testCountry("Philippines")
                app.changeFunding(-1)
            elif self.number == 5:  # NEST
                app.markers.append("NEST")
                app.outputToHistory("NEST in play. If jihadists have WMD, all plots in the US placed face up.", True)
            elif self.number == 6 or self.number == 7:  # Sanctions
                if "Patriot Act" in app.markers:
                    app.changeFunding(-2)
                else:
                    return False
            elif self.number == 8 or self.number == 9 or self.number == 10:  # Special Forces
                while True:
                    input = app.getCountryFromUser("Remove a cell from what country that has troops or is adjacent to a country with troops (? for list)?: ",  "XXX", app.listCountriesWithCellAndAdjacentTroops)
                    if input == "":
                        print ""
                        return
                    else:
                        if app.map[input].totalCells(True) <= 0:
                            print "There are no cells in %s" % input
                            print ""
                        else:
                            foundTroops = False
                            for country in app.map:
                                if country == input or app.isAdjacent(input, country):
                                    if app.map[country].troops() > 0:
                                        foundTroops = True
                                        break
                            if not foundTroops:
                                print "Neither this or any adjacent country have troops."
                                print ""
                            else:
                                app.removeCell(input, side)    # 20150131PS added side
                                app.outputToHistory(app.map[input].countryStr(), True)
                                break
            elif self.number == 11:  # Abbas
                numIRIsrael = 0
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            numIRIsrael = 1
                            break
                app.markers.append("Abbas")
                app.outputToHistory("Abbas in play.", False)
                if app.troops >= 5 and numIRIsrael <= 0:
                    app.changePrestige(1, False)
                    app.changeFunding(-2, True)
            elif self.number == 12:  # Al-Azhar
                app.testCountry("Egypt")
                numIR = app.numIslamistRule()
                if numIR <= 0:
                    app.changeFunding(-4, True)
                else:
                    app.changeFunding(-2, True)
            elif self.number == 13:  # Anbar Awakening
                if (app.map["Iraq"].troops() > 0) or (app.map["Syria"].troops() > 0):
                    app.markers.append("Anbar Awakening")
                    app.outputToHistory("Anbar Awakening in play.", False)
                    if app.map["Iraq"].troops() == 0:
                        app.map["Syria"].aid += 1 #20150131PS changed to add rather than set to 1
                        app.outputToHistory("Aid in Syria.", False)
                    elif app.map["Syria"].troops() == 0:
                        app.map["Iraq"].aid += 1    #20150131PS changed to add rather than set to 1
                        app.outputToHistory("Aid in Iraq.", False)
                    else:
                        print "There are troops in both Iraq and Syria."
                        if app.getYesNoFromUser("Do you want to add the Aid to Iraq? (y/n): "):
                            app.map["Iraq"].aid += 1
                            app.outputToHistory("Aid in Iraq.", False)
                        else:
                            app.map["Syria"].aid += 1
                            app.outputToHistory("Aid in Syria.", False)
                    app.changePrestige(1, False)
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
                        country_name = app.getCountryFromUser(
                            "Choose an Adversary country to attempt Covert Action (? for list): ", "XXX",
                            app.listAdversaryCountries)
                        if country_name == "":
                            print ""
                            return
                        elif app.map[country_name].is_adversary():
                            target_country = country_name
                        else:
                            print "%s is not an Adversary." % country_name
                            print ""
                action_roll = app.getRollFromUser("Enter Covert Action roll or r to have program roll: ")
                if action_roll >= 4:
                    app.map[target_country].make_neutral()
                    app.outputToHistory("Covert Action successful, %s now Neutral." % target_country, False)
                    app.outputToHistory(app.map[target_country].countryStr(), True)
                else:
                    app.outputToHistory("Covert Action fails.", True)
            elif self.number == 15:  # Ethiopia Strikes
                if (app.map["Somalia"].is_islamist_rule()) or (app.map["Sudan"].is_islamist_rule()):
                    if not app.map["Somalia"].is_islamist_rule():
                        app.map["Sudan"].make_poor()
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan now Poor Neutral.", False)
                        app.outputToHistory(app.map["Sudan"].countryStr(), True)
                    elif not app.map["Sudan"].is_islamist_rule():
                        app.map["Somalia"].make_poor()
                        app.map["Somalia"].make_neutral()
                        app.outputToHistory("Somalia now Poor Neutral.", False)
                        app.outputToHistory(app.map["Somalia"].countryStr(), True)
                    else:
                        print "Both Somalia and Sudan are under Islamist Rule."
                        if app.getYesNoFromUser("Do you want Somalia to be set to Poor Neutral? (y/n): "):
                            app.map["Somalia"].make_poor()
                            app.map["Somalia"].make_neutral()
                            app.outputToHistory("Somalia now Poor Neutral.", False)
                            app.outputToHistory(app.map["Somalia"].countryStr(), True)
                        else:
                            app.map["Sudan"].make_poor()
                            app.map["Sudan"].make_neutral()
                            app.outputToHistory("Sudan now Poor Neutral.", False)
                            app.outputToHistory(app.map["Sudan"].countryStr(), True)
                    print ""
                else:
                    return False
            elif self.number == 16:  # Euro-Islam
                posture = app.getPostureFromUser("Select Benelux's Posture (hard or soft): ")
                app.executeCardEuroIslam(posture)
            elif self.number == 17:  # FSB
                app.outputToHistory("Examine Jihadist hand for Loose Nukes, HEU, or Kazakh Strain.", False)
                hasThem = app.getYesNoFromUser("Does the Jihadist hand have Loose Nukes, HEU, or Kazakh Strain? (y/n): ")
                if hasThem:
                    app.outputToHistory("Discard Loose Nukes, HEU, or Kazakh Strain from the Jihadist hand.", False)
                else:
                    russiaCells = app.map["Russia"].totalCells(True)
                    cenAsiaCells = app.map["Central Asia"].totalCells(True)
                    if russiaCells > 0 or cenAsiaCells > 0:
                        if russiaCells == 0:
                            app.removeCell("Central Asia", side)    # 20150131PS added side
                            app.outputToHistory(app.map["Central Asia"].countryStr(), True)
                        elif cenAsiaCells == 0:
                            app.removeCell("Russia", side)    # 20150131PS added side
                            app.outputToHistory(app.map["Russia"].countryStr(), True)
                        else:
                            isRussia = app.getYesNoFromUser("There are cells in both Russia and Central Asia. Do you want to remove a cell in Russia? (y/n): ")
                            if isRussia:
                                app.removeCell("Russia", side)    # 20150131PS added side
                                app.outputToHistory(app.map["Russia"].countryStr(), True)
                            else:
                                app.removeCell("Central Asia", side)    # 20150131PS added side
                                app.outputToHistory(app.map["Central Asia"].countryStr(), False)
                    else:
                        app.outputToHistory("There are no cells in Russia or Central Asia.", False)
                app.outputToHistory("Shuffle Jihadist hand.", True)
            elif self.number == 18:  # Intel Community
                app.outputToHistory("Examine Jihadist hand. Do not change order of cards.", False)
                app.outputToHistory("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).", False)
                app.outputToHistory("You may now interrupt this action phase to play another card (Use the u command).", True)
            elif self.number == 19:  # Kemalist Republic
                app.outputToHistory("Turkey now a Fair Ally.", False)
                app.map["Turkey"].make_fair()
                app.map["Turkey"].make_ally()
                app.outputToHistory(app.map["Turkey"].countryStr(), True)
            elif self.number == 20:  # King Abdullah
                app.outputToHistory("Jordan now a Fair Ally.", False)
                app.map["Jordan"].make_fair()
                app.map["Jordan"].make_ally()
                app.outputToHistory(app.map["Jordan"].countryStr(), True)
                app.changePrestige(1)
                app.changeFunding(-1)
            elif self.number == 21:  # Let's Roll
                while True:
                    plotCountry = app.getCountryFromUser("Draw a card.  Choose an Ally or Good country to remove a plot from (? for list): ", "XXX", app.listGoodAllyPlotCountries)
                    if plotCountry == "":
                        print ""
                        return
                    else:
                        if not app.map[plotCountry].is_good() and not app.map[plotCountry].is_ally():
                            print "%s is neither Good nor an Ally." % plotCountry
                            print ""
                        elif app.map[plotCountry].plots <= 0:
                            print "%s has no plots." % plotCountry
                            print ""
                        else:
                            while True:
                                postureCountry = app.getCountryFromUser("Now choose a non-US country to set its Posture: ", "XXX", None)
                                if postureCountry == "":
                                    print ""
                                    return
                                else:
                                    if postureCountry == "United States":
                                        print "Choose a non-US country."
                                        print ""
                                    else:
                                        postureStr = app.getPostureFromUser("What Posture should %s have (h or s)? " % postureCountry)
                                        app.executeCardLetsRoll(plotCountry, postureCountry, postureStr)
                                        return
            elif self.number == 22:  # Mossad and Shin Bet
                app.removeAllCellsFromCountry("Israel")
                app.removeAllCellsFromCountry("Jordan")
                app.removeAllCellsFromCountry("Lebanon")
                app.outputToHistory("", False)
            elif self.number == 23 or self.number == 24 or self.number == 25:  # Predator
                while True:
                    input = app.getCountryFromUser("Choose non-Iran Muslim Country to remove a cell from (? for list): ", "XXX", app.listMuslimCountriesWithCells)
                    if input == "":
                        print ""
                        return
                    else:
                        if app.map[input].totalCells(True) == 0:
                            print "%s has no cells." % input
                            print ""
                        elif app.map[input].type == "Iran":
                            print "Iran is not allowed."
                            print ""
                        elif app.map[input].type == "Non-Muslim":
                            print "Choose a Muslim country."
                            print ""
                        else:
                            app.removeCell(input, side)    # 20150131PS added side
                            app.outputToHistory(app.map[input].countryStr(), True)
                            break
            elif self.number == 26:  # Quartet
                if not "Abbas" in app.markers:
                    return False
                if app.troops <= 4:
                    return False
                for country in app.map:
                    if app.isAdjacent(country, "Israel"):
                        if app.map[country].is_islamist_rule():
                            return False
                app.changePrestige(2)
                app.changeFunding(-3)
                app.outputToHistory("", False)
            elif self.number == 27:  # Saddam Captured
                if app.map["Iraq"].troops() == 0:
                    return False
                app.markers.append("Saddam Captured")
                app.map["Iraq"].aid += 1
                app.outputToHistory("Aid added in Iraq", False)
                app.changePrestige(1)
                app.outputToHistory(app.map["Iraq"].countryStr(), True)
            elif self.number == 28:  # Sharia
                numBesieged = app.numBesieged()
                target = ""
                if numBesieged <= 0:
                    return False
                elif numBesieged == 1:
                    for country in app.map:
                        if app.map[country].besieged > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a country with a Besieged Regime marker to remove (? for list): ",  "XXX", app.listBesiegedCountries)
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].besieged <= 0:
                                print "%s is not a Besieged Regime." % input
                                print ""
                            else:
                                target = input
                                break
                app.map[target].besieged = 0
                app.outputToHistory("%s is no longer a Besieged Regime." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 29:  # Tony Blair
                app.map["United Kingdom"].posture = app.map["United States"].posture
                app.outputToHistory("United Kingdom posture now %s" % app.map["United Kingdom"].posture, False)
                print "You may roll War of Ideas in up to 3 Schengen countries."
                for i in range(3):
                    target = ""
                    finishedPicking = False
                    while not target:
                        input = app.getCountryFromUser("Choose Schengen country to make a WOI roll (done to stop rolling) (? for list)?: ",  "done", app.listSchengenCountries)
                        if input == "":
                            print ""
                            return
                        elif input == "done":
                            finishedPicking = True
                            break
                        else:
                            if not app.map[input].schengen:
                                print "%s is not a Schengen country." % input
                                print ""
                                return
                            else:
                                target = input
                                postureRoll = app.getRollFromUser("Enter Posture Roll or r to have program roll: ")
                                app.executeNonMuslimWOI(target, postureRoll)
                    if finishedPicking:
                        break
                app.outputToHistory("", False)
            elif self.number == 30:  # UN Nation Building
                numRC = app.numRegimeChange()
                if (numRC <= 0) or ("Vieira de Mello Slain" in app.markers):
                    return False
                target = ""
                if numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change country (? for list): ",  "XXX", app.listRegimeChangeCountries)
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break
                app.map[target].aid += 1
                app.outputToHistory("Aid added to %s." % target, False)
                woiRoll = app.getRollFromUser("Enter WOI Roll or r to have program roll: ")
                modRoll = app.modifiedWoIRoll(woiRoll, target, False)
                app.handleMuslimWoI(modRoll, target)
            elif self.number == 31:  # Wiretapping
                if "Leak-Wiretapping" in app.markers:
                    return False
                for country in ["United States", "United Kingdom", "Canada"]:
                    if app.map[country].activeCells > 0:
                        num = app.map[country].activeCells
                        if num > 0:
                            app.map[country].activeCells -= num
                            app.cells += num
                            app.outputToHistory("%d Active Cell(s) removed from %s." % (num, country), False)
                    if app.map[country].sleeperCells > 0:
                        num = app.map[country].sleeperCells
                        if num > 0:
                            app.map[country].sleeperCells -= num
                            app.cells += num
                            app.outputToHistory("%d Sleeper Cell(s) removed from %s." % (num, country), False)
                    if app.map[country].cadre > 0:
                        num = app.map[country].cadre
                        if num > 0:
                            app.map[country].cadre = 0
                            app.outputToHistory("Cadre removed from %s." % country, False)
                    if app.map[country].plots > 0:
                        num = app.map[country].plots
                        if num > 0:
                            app.map[country].plots -= num
                            app.outputToHistory("%d Plots remove(d) from %s." % (num, country), False)
                app.markers.append("Wiretapping")
                app.outputToHistory("Wiretapping in Play.", True)
            elif self.number == 32:  # Back Channel
                if app.map["United States"].posture == "Hard":
                    return False
                num_adversaries = app.numAdversary()
                if num_adversaries <= 0:
                    return False
                if app.getYesNoFromUser("Do you want to discard a card with a value that exactly matches an Adversary's Resources? (y/n): "):
                    while True:
                        input = app.getCountryFromUser("Choose an Adversary country (? for list): ",  "XXX", app.listAdversaryCountries)
                        if input == "":
                            print ""
                            return False
                        else:
                            if not app.map[input].is_adversary():
                                print "%s is not a Adversary country." % input
                                print ""
                            else:
                                app.map[input].make_neutral()
                                app.outputToHistory("%s now Neutral" % input, False)
                                app.map[input].aid += 1
                                app.outputToHistory("Aid added to %s." % input, False)
                                app.outputToHistory(app.map[input].countryStr(), True)
                                break
            elif self.number == 33:  # Benazir Bhutto
                app.markers.append("Benazir Bhutto")
                app.outputToHistory("Benazir Bhutto in Play.", False)
                if app.map["Pakistan"].is_poor():
                    app.map["Pakistan"].make_fair()
                    app.outputToHistory("Pakistan now Fair governance.", False)
                app.outputToHistory("No Jihads in Pakistan.", False)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 34:  # Enhanced Measures
                app.markers.append("Enhanced Measures")
                app.outputToHistory("Enhanced Measures in Play.", False)
                app.outputToHistory("Take a random card from the Jihadist hand.", False)
                app.disrupt_cells_or_cadre()
                app.outputToHistory("", False)
            elif self.number == 35:  # Hajib
                app.testCountry("Turkey")
                app.map["Turkey"].improve_governance()
                app.outputToHistory("Turkey Governance now %s." % app.map["Turkey"].govStr(), False)
                app.changeFunding(-2)
                posture = app.getPostureFromUser("Select Frances's Posture (hard or soft): ")
                app.map["France"].posture = posture
                app.outputToHistory(app.map["Turkey"].countryStr(), False)
                app.outputToHistory(app.map["France"].countryStr(), True)
            elif self.number == 36:  # Indo-Pakistani Talks
                app.markers.append("Indo-Pakistani Talks")
                app.outputToHistory("Indo-Pakistani Talks in Play.", False)
                app.map['Pakistan'].make_ally()
                app.outputToHistory("Pakistan now Ally", False)
                posture = app.getPostureFromUser("Select India's Posture (hard or soft): ")
                app.map["India"].posture = posture
                app.outputToHistory(app.map["Pakistan"].countryStr(), False)
                app.outputToHistory(app.map["India"].countryStr(), True)
            elif self.number == 37:  # Iraqi WMD
                app.markers.append("Iraqi WMD")
                app.outputToHistory("Iraqi WMD in Play.", False)
                app.outputToHistory("Use this or a later card for Regime Change in Iraq at any Governance.", True)
            elif self.number == 38:  # Libyan Deal
                app.markers.append("Libyan Deal")
                app.outputToHistory("Libyan Deal in Play.", False)
                app.map["Libya"].is_ally()
                app.outputToHistory("Libya now Ally", False)
                app.changePrestige(1)
                print "Select the Posture of 2 Schengen countries."
                for i in range(2):
                    target = ""
                    while not target:
                        input = app.getCountryFromUser("Choose Schengen country (? for list)?: ", "XXX", app.listSchengenCountries)
                        if input == "":
                            print ""
                        else:
                            if not app.map[input].schengen:
                                print "%s is not a Schengen country." % input
                                print ""
                                return
                            else:
                                target = input
                                posture = app.getPostureFromUser("Select %s's Posture (hard or soft): " % target)
                                app.map[target].posture = posture
                                app.outputToHistory(app.map[target].countryStr(), False)
                app.outputToHistory("", False)
            elif self.number == 39:  # Libyan WMD
                app.markers.append("Libyan WMD")
                app.outputToHistory("Libyan WMD in Play.", False)
                app.outputToHistory("Use this or a later card for Regime Change in Libya at any Governance.", True)
            elif self.number == 40:  # Mass Turnout
                numRC = app.numRegimeChange()
                target = ""
                if numRC <= 0:
                    return False
                elif numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change Country to improve governance (? for list): ",  "XXX", app.listRegimeChangeCountries)
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break
                app.improveGovernance(target)
                app.outputToHistory("%s Governance improved." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 41:  # NATO
                numRC = app.numRegimeChange()
                target = ""
                if numRC <= 0:
                    return False
                elif numRC == 1:
                    for country in app.map:
                        if app.map[country].regimeChange > 0:
                            target = country
                            break
                else:
                    while True:
                        input = app.getCountryFromUser("Choose a Regime Change Country to land NATO troops (? for list): ",  "XXX", app.listRegimeChangeCountries)
                        if input == "":
                            print ""
                            return
                        else:
                            if app.map[input].regimeChange <= 0:
                                print "%s is not a Regime Change country." % input
                                print ""
                            else:
                                target = input
                                break
                app.map[target].markers.append("NATO")
                app.outputToHistory("NATO added in %s" % target, False)
                app.map[target].aid += 1
                app.outputToHistory("Aid added in %s" % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 42:  # Pakistani Offensive
                if "FATA" in app.map["Pakistan"].markers:
                    app.map["Pakistan"].markers.remove("FATA")
                    app.outputToHistory("FATA removed from Pakistan", True)
            elif self.number == 43:  # Patriot Act
                app.markers.append("Patriot Act")
            elif self.number == 44:  # Renditions
                app.markers.append("Renditions")
                app.outputToHistory("Renditions in Play.", False)
                app.outputToHistory("Discard a random card from the Jihadist hand.", False)
                if app.num_disruptable() > 0:
                    app.disrupt_cells_or_cadre()
                app.outputToHistory("", False)
            elif self.number == 45:  # Safer Now
                app.changePrestige(3)
                postureRoll = app.getRollFromUser("Enter US Posture Roll or r to have program roll: ")
                if postureRoll <= 4:
                    app.map["United States"].posture = "Soft"
                    app.outputToHistory("US Posture now Soft.", False)
                else:
                    app.map["United States"].posture = "Hard"
                    app.outputToHistory("US Posture now Hard.", False)
                while True:
                    postureCountry = app.getCountryFromUser("Now choose a non-US country to set its Posture: ", "XXX", None)
                    if postureCountry == "":
                        print ""
                    else:
                        if postureCountry == "United States":
                            print "Choos a non-US country."
                            print ""
                        else:
                            postureStr = app.getPostureFromUser("What Posture should %s have (h or s)? " % postureCountry)
                            app.outputToHistory("%s Posture now %s" % (postureCountry, postureStr), False)
                            app.map[postureCountry].posture = postureStr
                            app.outputToHistory(app.map["United States"].countryStr(), False)
                            app.outputToHistory(app.map[postureCountry].countryStr(), True)
                            break
            elif self.number == 46:  # Sistani
                targetCountries = []
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        if app.map[country].regimeChange > 0:
                            if (app.map[country].totalCells(True)) > 0:
                                targetCountries.append(country)
                if len(targetCountries) == 1:
                    target = targetCountries[0]
                else:
                    target = None
                while not target:
                    input = app.getCountryFromUser("Choose a Shia-Mix Regime Change Country with a cell to improve governance (? for list): ",  "XXX", app.listShiaMixRegimeChangeCountriesWithCells)
                    if input == "":
                        print ""
                    else:
                        if input not in targetCountries:
                            print "%s is not a Shi-Mix Regime Change Country with a cell." % input
                            print ""
                        else:
                            target = input
                            break
                app.improveGovernance(target)
                app.outputToHistory("%s Governance improved." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 47:  # The door of Itjihad was closed
                app.lapsing.append("The door of Itjihad was closed")
            else:
                return False
        elif self.type == "Jihadist" and side == "Jihadist":
            if self.number == 48:  # Adam Gadahn
                cardNum = app.getCardNumFromUser("Enter the number of the next Jihadist card or none if there are none left: ")
                if cardNum == "none":
                    app.outputToHistory("No cards left to recruit to US.", True)
                    return
                ops = app.deck[str(cardNum)].ops
                rolls = app.randomizer.roll_d6(ops)
                app.executeRecruit("United States", ops, rolls, 2)
            elif self.number == 49:  # Al-Ittihad al-Islami
                app.placeCells("Somalia", 1)
            elif self.number == 50:  # Ansar al-Islam
                possible = ["Iraq", "Iran"]
                target = random.choice(possible)
                app.placeCells(target, 1)
            elif self.number == 51:  # FREs
                if "Saddam Captured" in app.markers:
                    cellsToMove = 2
                else:
                    cellsToMove = 4
                cellsToMove = min(cellsToMove, app.cells)
                app.placeCells("Iraq", cellsToMove)
            elif self.number == 52:  # IDEs
                app.outputToHistory("US randomly discards one card.", True)
            elif self.number == 53:  # Madrassas
                app.handleRecruit(1, True)
                cardNum = app.getCardNumFromUser("Enter the number of the next Jihadist card or none if there are none left: ")
                if cardNum == "none":
                    app.outputToHistory("No cards left to recruit.", True)
                    #app.outputToHistory("Jihadist Activity Phase finished, enter plot command.", True)
                    return
                ops = app.deck[str(cardNum)].ops
                app.handleRecruit(ops, True)
                #app.outputToHistory("Jihadist Activity Phase finished, enter plot command.", True)
            elif self.number == 54:  # Moqtada al-Sadr
                app.map["Iraq"].markers.append("Sadr")
                app.outputToHistory("Sadr Marker added in Iraq", True)
            elif self.number == 55:  # Uyghur Jihad
                app.testCountry("China")
                if app.cells > 0:
                    if app.map["China"].posture == "Soft":
                        app.place_cell("China")
                    else:
                        app.place_cell("Central Asia")
                else:
                    app.outputToHistory("No cells to place.", True)
            elif self.number == 56:  # Vieira de Mello Slain
                app.markers.append("Vieira de Mello Slain")
                app.outputToHistory("Vieira de Mello Slain in play.", False)
                app.changePrestige(-1)
            elif self.number == 57:  # Abu Sayyaf
                app.placeCells("Philippines", 1)
                app.markers.append("Abu Sayyaf")
            elif self.number == 58:  # Al-Anbar
                app.markers.append("Al-Anbar")
                app.outputToHistory("Al-Anbar in play.", True)
                app.testCountry("Iraq")
                if app.cells > 0:
                    app.place_cell("Iraq")
            elif self.number == 59:  # Amerithrax
                app.outputToHistory("US side discards its highest-value US-associated event card, if it has any.", True)
            elif self.number == 60:  # Bhutto Shot
                app.markers.append("Bhutto Shot")
                app.outputToHistory("Bhutto Shot in play.", True)
            elif self.number == 61:  # Detainee Release
                if app.cells > 0:
                    target = None
                    while not target:
                        input = app.getCountryFromUser("Choose a country where Disrupt occured this or last Action Phase: ",  "XXX", None)
                        if input == "":
                            print ""
                            return
                        else:
                            target = input
                            break
                    app.place_cell(target)
                app.outputToHistory("Draw a card for the Jihadist and put it on the top of their hand.", True)
            elif self.number == 62:  # Ex-KGB
                if "CTR" in app.map["Russia"].markers:
                    app.map["Russia"].markers.remove("CTR")
                    app.outputToHistory("CTR removed from Russia.", True)
                else:
                    targetCaucasus = False
                    if app.map["Caucasus"].posture == "" or app.map["Caucasus"].posture == app.map["United States"].posture:
                        if app.gwotPenalty() == 0:
                            cacPosture = app.map["Caucasus"].posture
                            if app.map["United States"].posture == "Hard":
                                app.map["Caucasus"].posture = "Soft"
                            else:
                                app.map["Caucasus"].posture = "Hard"
                            if app.gwotPenalty() < 0:
                                targetCaucasus = True
                            app.map["Caucasus"].posture = cacPosture
                    if targetCaucasus:
                        if app.map["United States"].posture == "Hard":
                            app.map["Caucasus"].posture = "Soft"
                        else:
                            app.map["Caucasus"].posture = "Hard"
                        app.outputToHistory("Caucasus posture now %s" % app.map["Caucasus"].posture, False)
                        app.outputToHistory(app.map["Caucasus"].countryStr(), True)
                    else:
                        app.testCountry("Central Asia")
                        if app.map["Central Asia"].is_ally():
                            app.map["Central Asia"].make_neutral()
                            app.outputToHistory("Central Asia now Neutral.", True)
                        elif app.map["Central Asia"].is_neutral():
                            app.map["Central Asia"].make_adversary()
                            app.outputToHistory("Central Asia now Adversary.", True)
                        app.outputToHistory(app.map["Central Asia"].countryStr(), True)
            elif self.number == 63:  # Gaza War
                app.changeFunding(1)
                app.changePrestige(-1)
                app.outputToHistory("US discards a random card.", True)
            elif self.number == 64:  # Hariri Killed
                app.testCountry("Lebanon")
                app.testCountry("Syria")
                app.map["Syria"].make_adversary()
                app.outputToHistory("Syria now Adversary.", False)
                if app.map["Syria"].governance_is_better_than(POOR):
                    app.worsenGovernance("Syria")
                    app.outputToHistory("Governance in Syria worsened.", False)
                    app.outputToHistory(app.map["Syria"].countryStr(), True)
                app.outputToHistory(app.map["Lebanon"].countryStr(), True)
            elif self.number == 65:  # HEU
                possibles = []
                if app.map["Russia"].totalCells() > 0 and "CTR" not in app.map["Russia"].markers:
                    possibles.append("Russia")
                if app.map["Central Asia"].totalCells() > 0 and "CTR" not in app.map["Central Asia"].markers:
                    possibles.append("Central Asia")
                target = random.choice(possibles)
                roll = random.randint(1, 6)
                app.executeCardHEU(target, roll)
            elif self.number == 66:  # Homegrown
                app.placeCells("United Kingdom", 1)
            elif self.number == 67:  # Islamic Jihad Union
                app.placeCells("Central Asia", 1)
                if app.cells > 0:
                    app.placeCells("Afghanistan", 1)
            elif self.number == 68:  # Jemaah Islamiya
                app.placeCells("Indonesia/Malaysia", 2)
            elif self.number == 69:  # Kazakh Strain
                roll = random.randint(1, 6)
                app.executeCardHEU("Central Asia", roll)
            elif self.number == 70:  # Lashkar-e-Tayyiba
                app.placeCells("Pakistan", 1)
                if app.cells > 0:
                    app.placeCells("India", 1)
            elif self.number == 71:  # Loose Nuke
                roll = random.randint(1, 6)
                app.executeCardHEU("Russia", roll)
            elif self.number == 72:  # Opium
                cellsToPlace = min(app.cells, 3)
                if app.map["Afghanistan"].is_islamist_rule():
                    cellsToPlace = app.cells
                app.placeCells("Afghanistan", cellsToPlace)
            elif self.number == 73:  # Pirates
                app.markers.append("Pirates")
                app.outputToHistory("Pirates in play.", False)
            elif self.number == 74:  # Schengen Visas
                if app.cells == 15:
                    app.outputToHistory("No cells to travel.", False)
                    return
                app.handleTravel(2, False, True)
            elif self.number == 75:  # Schroeder & Chirac
                app.map["Germany"].posture = "Soft"
                app.outputToHistory("%s Posture now %s" % ("Germany", app.map["Germany"].posture), True)
                app.map["France"].posture = "Soft"
                app.outputToHistory("%s Posture now %s" % ("France", app.map["France"].posture), True)
                app.changePrestige(-1)
            elif self.number == 76:  # Abu Ghurayb
                app.outputToHistory("Draw 2 cards.", False)
                app.changePrestige(-2)
                allys = app.minorJihadInGoodFairChoice(1, True)
                if not allys:
                    app.outputToHistory("No Allys to shift.", True)
                else:
                    target = allys[0][0]
                    app.map[target].make_neutral()
                    app.outputToHistory("%s Alignment shifted to Neutral." % target, True)
            elif self.number == 77:  # Al Jazeera
                choices = app.minorJihadInGoodFairChoice(1, False, True)
                if not choices:
                    app.outputToHistory("No countries to shift.", True)
                else:
                    target = choices[0][0]
                    if app.map[target].is_ally():
                        app.map[target].make_neutral()
                    elif app.map[target].is_neutral():
                        app.map[target].make_adversary()
                    app.outputToHistory("%s Alignment shifted to %s." % (target, app.map[target].alignment()), True)
            elif self.number == 78:  # Axis of Evil
                app.outputToHistory("US discards any Iran, Hizballah, or Jaysh al-Mahdi cards from hand.", False)
                if app.map["United States"].posture == "Soft":
                    app.map["United States"].posture = "Hard"
                    app.outputToHistory("US Posture now Hard.", False)
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1, 6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
            elif self.number == 79:  # Clean Operatives
                app.handleTravel(2, False, False, True)
            elif self.number == 80:  # FATA
                app.testCountry("Pakistan")
                if app.map["Pakistan"].markers.count("FATA") == 0:
                    app.map["Pakistan"].markers.append("FATA")
                    app.outputToHistory("FATA marker added in Pakistan", True)
                app.placeCells("Pakistan", 1)
            elif self.number == 81:  # Foreign Fighters
                possibles = []
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        possibles.append(country)
                if len(possibles) <= 0:
                    return False
                target = random.choice(possibles)
                app.placeCells(target, 5)
                if app.map[target].aid > 0:
                    app.map[target].aid -= 1
                    app.outputToHistory("Aid removed from %s" % target, False)
                else:
                    app.map[target].besieged = 1
                    app.outputToHistory("%s to Besieged Regime" % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 82:  # Jihadist Videos
                possibles = []
                for country in app.map:
                    if app.map[country].totalCells() == 0:
                        possibles.append(country)
                random.shuffle(possibles)
                for i in range(3):
                    app.testCountry(possibles[i])
                    # number of available cells does not matter for Jihadist Videos
                    # if app.cells > 0:
                    rolls = [random.randint(1, 6)]
                    app.executeRecruit(possibles[i], 1, rolls, False, True)
            elif self.number == 83:  # Kashmir
                app.placeCells("Pakistan", 1)
                if app.map["Pakistan"].is_ally():
                    app.map["Pakistan"].make_neutral()
                elif app.map["Pakistan"].is_neutral():
                    app.map["Pakistan"].make_adversary()
                app.outputToHistory("%s Alignment shifted to %s." % ("Pakistan", app.map["Pakistan"].alignment()), True)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 84 or self.number == 85:  # Leak
                possibles = []
                if "Enhanced Measures" in app.markers:
                    possibles.append("Enhanced Measures")
                if "Renditions" in app.markers:
                    possibles.append("Renditions")
                if "Wiretapping" in app.markers:
                    possibles.append("Wiretapping")
                target = random.choice(possibles)
                app.markers.remove(target)
                app.markers.append("Leak-"+target)
                app.outputToHistory("%s removed and can no longer be played." % target, False)
                usPrestigeRolls = []
                for i in range(3):
                    usPrestigeRolls.append(random.randint(1, 6))
                postureRoll = random.randint(1, 6)
                presMultiplier = 1
                if usPrestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(usPrestigeRolls[1], usPrestigeRolls[2]) * presMultiplier, False)
                if postureRoll <= 4:
                    app.map["United States"].posture = "Soft"
                else:
                    app.map["United States"].posture = "Hard"
                app.outputToHistory("US Posture now %s" % app.map["United States"].posture, True)
                allies = app.minorJihadInGoodFairChoice(1, True)
                if not allies:
                    app.outputToHistory("No Allies to shift.", True)
                else:
                    target = allies[0][0]
                    app.map[target].make_neutral()
                    app.outputToHistory("%s Alignment shifted to Neutral." % target, True)
            elif self.number == 86:  # Lebanon War
                app.outputToHistory("US discards a random card.", False)
                app.changePrestige(-1, False)
                possibles = []
                for country in app.map:
                    if app.map[country].type == "Shia-Mix":
                        possibles.append(country)
                target = random.choice(possibles)
                app.placeCells(target, 1)
            elif self.number == 87 or self.number == 88 or self.number == 89:  # Martyrdom Operation
                if app.executePlot(1, False, [1], True) == 1:
                    app.outputToHistory("No plots could be placed.", True)
                    app.handleRadicalization(app.deck[str(self.number)].ops)
            elif self.number == 90:  # Quagmire
                app.map["United States"].posture = "Soft"
                app.outputToHistory("US Posture now Soft.", False)
                app.outputToHistory("US randomly discards two cards and Jihadist plays them.", False)
                app.outputToHistory("Do this using the j # command for each card.", True)
            elif self.number == 91:  # Regional al-Qaeda
                possibles = []
                for country in app.map:
                    if app.map[country].is_muslim() and app.map[country].is_ungoverned():
                        possibles.append(country)
                random.shuffle(possibles)
                if app.numIslamistRule() > 0:
                    app.placeCells(possibles[0], 2)
                    app.placeCells(possibles[1], 2)
                else:
                    app.placeCells(possibles[0], 1)
                    app.placeCells(possibles[1], 1)
            elif self.number == 92:  # Saddam
                app.funding = 9
                app.outputToHistory("Jihadist Funding now 9.", True)
            elif self.number == 93:  # Taliban
                app.testCountry("Afghanistan")
                app.map["Afghanistan"].besieged = 1
                app.outputToHistory("Afghanistan is now a Besieged Regime.", False)
                app.placeCells("Afghanistan", 1)
                app.placeCells("Pakistan", 1)
                if (app.map["Afghanistan"].is_islamist_rule()) or (app.map["Pakistan"].is_islamist_rule()):
                    app.changePrestige(-3)
                else:
                    app.changePrestige(-1)
            elif self.number == 94:  # The door of Itjihad was closed
                target = None
                while not target:
                    country = app.getCountryFromUser("Choose a country tested or improved to Fair or Good this or last Action Phase: ", "XXX", None)
                    if country == "":
                        print ""
                    elif app.map[country].is_fair() or app.map[country].is_good():
                        target = country
                    else:
                        print "%s is neither Fair nor Good."
                app.map[target].worsenGovernance()
                app.outputToHistory("%s Governance worsened." % target, False)
                app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 95:  # Wahhabism
                if app.map["Saudi Arabia"].is_islamist_rule():
                    app.changeFunding(9)
                else:
                    app.changeFunding(app.map["Saudi Arabia"].governance_as_funding())
        else:
            if self.number == 96:  # Danish Cartoons
                posture = app.getPostureFromUser("Select Scandinavia's Posture (hard or soft): ")
                app.map["Scandinavia"].posture = posture
                app.outputToHistory("Scandinavia posture now %s." % posture, False)
                possibles = []
                for country in app.map:
                    if app.map[country].is_muslim() and not app.map[country].is_islamist_rule():
                        possibles.append(country)
                target = random.choice(possibles)
                app.testCountry(target)
                if app.numIslamistRule() > 0:
                    app.outputToHistory("Place any available plot in %s." % target, False)
                else:
                    app.outputToHistory("Place a Plot 1 in %s." % target, False)
                app.map[target].plots += 1
            elif self.number == 97:  # Fatwa
                app.outputToHistory("Trade random cards.", False)
                if side == "US":
                    app.outputToHistory("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi).", False)
                else:
                    app.aiFlowChartMajorJihad(97)
            elif self.number == 98:  # Gaza Withdrawl
                if side == "US":
                    app.changeFunding(-1)
                else:
                    app.placeCells("Israel", 1)
            elif self.number == 99:  # HAMAS Elected
                app.outputToHistory("US selects and discards one card.", False)
                app.changePrestige(-1)
                app.changeFunding(-1)
            elif self.number == 100:  # His Ut-Tahrir
                if app.troops >= 10:
                    app.changeFunding(-2)
                elif app.troops < 5:
                    app.changeFunding(2)
            elif self.number == 101:  # Kosovo
                app.changePrestige(1)
                app.testCountry("Serbia")
                if app.map["United States"].posture == "Soft":
                    app.map["Serbia"].posture = "Hard"
                else:
                    app.map["Serbia"].posture = "Soft"
                app.outputToHistory("Serbia Posture now %s." %                         app.map["Serbia"].posture, True)
            elif self.number == 102:  # Former Soviet Union
                testRoll = random.randint(1, 6)
                if testRoll <= 4:
                    app.map["Central Asia"].make_poor()
                else:
                    app.map["Central Asia"].make_fair()
                app.map["Central Asia"].make_neutral()
                app.outputToHistory("%s tested, governance %s" % (app.map["Central Asia"].name, app.map["Central Asia"].govStr()), False)
            elif self.number == 103:  # Hizballah
                if side == "US":
                    oneAway = []
                    twoAway = []
                    threeAway = []
                    for countryObj in app.map["Lebanon"].links:
                        oneAway.append(countryObj.name)
                    for country in oneAway:
                        for subCountryObj in app.map[country].links:
                            if subCountryObj.name not in twoAway and subCountryObj.name not in oneAway and subCountryObj.name != "Lebanon":
                                twoAway.append(subCountryObj.name)
                    for country in twoAway:
                        for subCountryObj in app.map[country].links:
                            if subCountryObj.name not in threeAway and subCountryObj.name not in twoAway and subCountryObj.name not in oneAway and subCountryObj.name != "Lebanon":
                                threeAway.append(subCountryObj.name)
                    possibles = []
                    for country in oneAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    for country in twoAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    for country in threeAway:
                        if country not in possibles and app.map[country].totalCells(True) > 0 and app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    if len(possibles) <= 0:
                        app.outputToHistory("No Shia-Mix countries with cells within 3 countries of Lebanon.", True)
                        target = None
                    elif len(possibles) == 1:
                        target = possibles[0]
                    else:
                        target = None
                        while not target:
                            input = app.getCountryFromUser("Remove a cell from what Shia-Mix country within 3 countries of Lebanon (? for list)?: ",  "XXX", app.listCountriesInParam, possibles)
                            if input == "":
                                print ""
                            else:
                                if app.map[input].totalCells(True) <= 0:
                                    print "There are no cells in %s" % input
                                    print ""
                                elif input not in possibles:
                                    print "%s not a Shia-Mix country within 3 countries of Lebanon." % input
                                    print ""
                                else:
                                    target = input
                    if target:
                        app.removeCell(target, side)    # 20150131PS added side
                        app.outputToHistory(app.map[target].countryStr(), True)
                else:
                    app.testCountry("Lebanon")
                    app.map["Lebanon"].make_poor()
                    app.outputToHistory("Lebanon governance now Poor.", False)
                    app.map["Lebanon"].make_neutral()
                    app.outputToHistory("Lebanon alignment now Neutral.", True)
            elif self.number == 104 or self.number == 105:  # Iran
                if side == "US":
                    target = None
                    while not target:
                        input = app.getCountryFromUser("Choose a Shia-Mix country to test. You can then remove a cell from there or Iran (? for list)?: ",  "XXX", app.listShiaMixCountries)
                        if input == "":
                            print ""
                        else:
                            if app.map[input].type != "Shia-Mix":
                                print "%s is not a Shia-Mix country." % input
                                print ""
                            else:
                                target = input
                    picked = target
                    app.testCountry(picked)
                    if app.map["Iran"].totalCells(True) > 0:
                        target = None
                        while not target:
                            input = app.getCountryFromUser("Remove a cell from %s or %s: " % (picked, "Iran"),  "XXX", None)
                            if input == "":
                                print ""
                            else:
                                if input != picked and input != "Iran":
                                    print "Remove a cell from %s or %s: " % (picked, "Iran")
                                    print ""
                                else:
                                    target = input
                    else:
                        target = picked
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory(app.map[target].countryStr(), True)
                else:
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.testCountry(target)
                    tested = target
                    target = None
                    goods = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                            if app.map[country].is_good():
                                goods.append(country)
                    if len(goods) > 1:
                        distances = []
                        for country in goods:
                            distances.append((app.countryDistance(tested, country), country))
                        distances.sort()
                        target = distances[0][1]
                    elif len(goods) == 1:
                        target = goods[0]
                    else:
                        fairs = []
                        for country in app.map:
                            if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                                if app.map[country].is_fair():
                                    fairs.append(country)
                        if len(fairs) > 1:
                            distances = []
                            for country in fairs:
                                distances.append((app.countryDistance(tested, country), country))
                            distances.sort()
                            target = distances[0][1]
                        elif len(fairs) == 1:
                            target = fairs[0]
                        else:
                            app.outputToHistory("No Good or Fair countries to Jihad in.", True)
                            return
                    app.outputToHistory("%s selected for jihad rolls." % target, False)
                    for i in range(2):
                        roll = random.randint(1, 6)
                        app.outputToHistory("Rolled: " + str(roll), False)
                        if app.map[target].is_non_recruit_success(roll):
                            if app.map[target].governance_is_better_than(POOR):
                                app.map[target].worsenGovernance()
                                app.outputToHistory("Governance worsened in %s." % target, False)
                                app.outputToHistory(app.map[target].countryStr(), True)
                        else:
                            app.outputToHistory("Roll failed.  No change to governance in %s." % target, False)

            elif self.number == 106:  # Jaysh al-Mahdi
                if side == "US":
                    target = None
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            if app.map[country].troops() > 0 and app.map[country].totalCells() > 0:
                                possibles.append(country)
                    if len(possibles) == 1:
                        target = possibles[0]
                    while not target:
                        input = app.getCountryFromUser("Choose a Shia-Mix country with cells and troops (? for list)?: ",  "XXX", app.listShiaMixCountriesWithCellsTroops)
                        if input == "":
                            print ""
                        else:
                            if input not in possibles:
                                print "%s is not a Shia-Mix country with cells and troops." % input
                                print ""
                            else:
                                target = input
                    app.removeCell(target, side)    # 20150131PS added side
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory(app.map[target].countryStr(), True)
                else:   # jihadist play
                    possibles = []
                    for country in app.map:
                        if app.map[country].type == "Shia-Mix":
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.testCountry(target)
                    tested = target
                    target = None
                    goods = []
                    for country in app.map:
                        if app.map[country].is_muslim():
                            if app.map[country].is_good():
                                goods.append(country)
                    if len(goods) > 1:
                        distances = []
                        for country in goods:
                            distances.append((app.countryDistance(tested, country), country))
                        distances.sort()
                        target = distances[0][1]
                    elif len(goods) == 1:
                        target = goods[0]
                    else:
                        fairs = []
                        for country in app.map:
                            if app.map[country].type == "Shia-Mix" or app.map[country].type == "Suni":
                                if app.map[country].is_fair():
                                    fairs.append(country)
                        if len(fairs) > 1:
                            distances = []
                            for country in fairs:
                                distances.append((app.countryDistance(tested, country), country))
                            distances.sort()
                            target = distances[0][1]
                        elif len(fairs) == 1:
                            target = fairs[0]
                        else:
                            app.outputToHistory("No Good or Fair countries to worsen Governance in.", True)
                            return
                        if app.map[target].governance_is_better_than(ISLAMIST_RULE):
                            app.map[target].worsenGovernance()
                            app.outputToHistory("Governance worsened in %s." % target, False)
                            app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 107:  # Kurdistan
                if side == "US":
                    app.testCountry("Iraq")
                    app.map["Iraq"].aid += 1
                    app.outputToHistory("Aid added to Iraq.", False)
                    app.outputToHistory(app.map["Iraq"].countryStr(), True)
                else:
                    app.testCountry("Turkey")
                    target = None
                    possibles = []
                    if app.map["Turkey"].governance_is_better_than(POOR):
                        possibles.append("Turkey")
                    if app.map["Iraq"].is_governed() and app.map["Iraq"].governance_is_better_than(POOR):
                        possibles.append("Iraq")
                    if len(possibles) == 0:
                        app.outputToHistory("Iraq and Turkey cannot have governance worsened.", True)
                        return
                    elif len(possibles) == 0:
                        target = possibles[0]
                    else:
                        countryScores = {}
                        for country in possibles:
                            countryScores[country] = 0
                            if app.map[country].aid > 0:
                                countryScores[country] += 10000
                            if app.map[country].besieged > 0:
                                countryScores[country] += 1000
                            countryScores[country] += (app.countryResources(country) * 100)
                            countryScores[country] += random.randint(1, 99)
                        countryOrder = []
                        for country in countryScores:
                            countryOrder.append((countryScores[country], (app.map[country].totalCells(True)), country))
                        countryOrder.sort()
                        countryOrder.reverse()
                        target = countryOrder[0][2]
                    app.map[target].worsenGovernance()
                    app.outputToHistory("Governance worsened in %s." % target, False)
                    app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 108:  # Musharraf
                app.removeCell("Pakistan", side)    # 20150131PS added side
                app.map["Pakistan"].make_poor()
                app.map["Pakistan"].make_ally()
                app.outputToHistory("Pakistan now Poor Ally.", False)
                app.outputToHistory(app.map["Pakistan"].countryStr(), True)
            elif self.number == 109:  # Tora Bora
                possibles = []
                for country in app.map:
                    if app.map[country].regimeChange > 0:
                        if app.map[country].totalCells() >= 2:
                            possibles.append(country)
                target = None
                if len(possibles) == 0:
                    return False
                if len(possibles) == 1:
                    target = possibles[0]
                else:
                    if side == "US":
                        app.outputToHistory("US draws one card.", False)
                        while not target:
                            input = app.getCountryFromUser("Choose a Regime Change country with at least 2 troops. (? for list)?: ",  "XXX", app.listRegimeChangeWithTwoCells)
                            if input == "":
                                print ""
                            else:
                                if input not in possibles:
                                    print "%s is not a Regime Change country with at least 2 troops." % input
                                    print ""
                                else:
                                    target = input
                    else:
                        app.outputToHistory("Jihadist draws one card.", False)
                        target = random.choice(possibles)
                app.removeCell(target, side)    # 20150131PS added side
                app.removeCell(target, side)    # 20150131PS added side
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1, 6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
            elif self.number == 110:  # Zarqawi
                if side == "US":
                    app.changePrestige(3)
                    app.outputToHistory("Remove card from game.", False)
                else:
                    possibles = []
                    for country in ["Iraq", "Syria", "Lebanon", "Jordan"]:
                        if app.map[country].troops() > 0:
                            possibles.append(country)
                    target = random.choice(possibles)
                    app.placeCells(target, 3)
                    app.map[target].plots += 1
                    app.outputToHistory("Add a Plot 2 to %s." % target, False)
                    app.outputToHistory(app.map[target].countryStr(), True)
            elif self.number == 111:  # Zawahiri
                if side == "US":
                    app.changeFunding(-2)
                else:
                    if app.numIslamistRule() > 0:
                        app.changePrestige(-3)
                    else:
                        app.changePrestige(-1)
            elif self.number == 112:  # Bin Ladin
                if side == "US":
                    app.changeFunding(-4)
                    app.changePrestige(1)
                    app.outputToHistory("Remove card from game.", False)
                else:
                    if app.numIslamistRule() > 0:
                        app.changePrestige(-4)
                    else:
                        app.changePrestige(-2)
            elif self.number == 113:  # Darfur
                app.testCountry("Sudan")
                if app.prestige >= 7:
                    app.map["Sudan"].aid += 1
                    app.outputToHistory("Aid added to Sudan.", False)
                    if app.map["Sudan"].is_adversary():
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan alignment improved.", False)
                    elif app.map["Sudan"].is_neutral():
                        app.map["Sudan"].make_ally()
                        app.outputToHistory("Sudan alignment improved.", False)
                else:
                    app.map["Sudan"].besieged = 1
                    app.outputToHistory("Sudan now Besieged Regime.", False)
                    if app.map["Sudan"].is_ally():
                        app.map["Sudan"].make_neutral()
                        app.outputToHistory("Sudan alignment worsened.", False)
                    elif app.map["Sudan"].is_neutral():
                        app.map["Sudan"].make_adversary()
                        app.outputToHistory("Sudan alignment worsened.", False)
                app.outputToHistory(app.map["Sudan"].countryStr(), True)
            elif self.number == 114:  # GTMO
                app.lapsing.append("GTMO")
                app.outputToHistory("GTMO in play. No recruit operations or Detainee Release the rest of this turn.", False)
                prestigeRolls = []
                for i in range(3):
                    prestigeRolls.append(random.randint(1, 6))
                presMultiplier = 1
                if prestigeRolls[0] <= 4:
                    presMultiplier = -1
                app.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
            elif self.number == 115:  # Hambali
                if side == "US":
                    possibles = ["Indonesia/Malaysia"]
                    targets = []
                    target = None
                    for countryObj in app.map["Indonesia/Malaysia"].links:
                        possibles.append(countryObj.name)
                    for country in possibles:
                        if app.map[country].totalCells(True) > 0:
                            if app.map[country].type == "Non-Muslim":
                                if app.map[country].posture == "Hard":
                                    targets.append(country)
                            else:
                                if app.map[country].is_ally():
                                    targets.append(country)
                    if len(targets) == 1:
                        target = targets[0]
                    else:
                        while not target:
                            input = app.getCountryFromUser("Choose Indonesia or an adjacent country that has a cell and is Ally or Hard. (? for list)?: ",  "XXX", app.listHambali)
                            if input == "":
                                print ""
                            else:
                                if input not in targets:
                                    print "%s is not Indonesia or an adjacent country that has a cell and is Ally or Hard." % input
                                    print ""
                                else:
                                    target = input
                    app.removeCell(target, side)    # 20150131PS added side
                    app.outputToHistory("US draw 2 cards.", False)
                else:
                    possibles = ["Indonesia/Malaysia"]
                    targets = []
                    target = None
                    for countryObj in app.map["Indonesia/Malaysia"].links:
                        possibles.append(countryObj.name)
                    for country in possibles:
                        if app.map[country].totalCells(True) > 0:
                            if app.map[country].type == "Non-Muslim":
                                if app.map[country].posture == "Hard":
                                    targets.append(country)
                            else:
                                if app.map[country].is_ally():
                                    targets.append(country)
                    target = random.choice(targets)
                    app.map[target].plots += 1
                    app.outputToHistory("Place an plot in %s." % target, True)
            elif self.number == 116:  # KSM
                if side == "US":
                    for country in app.map:
                        if app.map[country].plots > 0:
                            if app.map[country].is_ally() or app.map[country].type == "Non-Muslim":
                                numPlots = app.map[country].plots
                                app.map[country].plots = 0
                                app.outputToHistory("%d Plots removed from %s." % (numPlots, country), False)
                    app.outputToHistory("US draws 2 cards.", True)
                else:
                    if app.executePlot(1, False, [1], False, False, True) == 1:
                        app.outputToHistory("No plots could be placed.", True)
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                app.lapsing.append("Oil Price Spike")
                app.outputToHistory("Oil Price Spike in play. Add +1 to the resources of each Oil Exporter country for the turn.", False)
                if side == "US":
                    app.outputToHistory("Select, reveal, and draw a card other than Oil Price Spike from the discard pile or a box.", True)
                else:
                    if app.getYesNoFromUser("Are there any Jihadist event cards in the discard pile? "):
                        app.outputToHistory("Draw from the Discard Pile randomly among the highest-value Jihadist-associated event cards. Put the card on top of the Jihadist hand.", True)
            elif self.number == 119:  # Saleh
                app.testCountry("Yemen")
                if side == "US":
                    if not app.map["Yemen"].is_islamist_rule():
                        if app.map["Yemen"].is_adversary():
                            app.map["Yemen"].make_neutral()
                        elif app.map["Yemen"].is_neutral():
                            app.map["Yemen"].make_ally()
                        app.outputToHistory("Yemen Alignment improved to %s." % app.map["Yemen"].alignment(), False)
                        app.map["Yemen"].aid += 1
                        app.outputToHistory("Aid added to Yemen.", True)
                else:
                    if app.map["Yemen"].is_ally():
                        app.map["Yemen"].make_neutral()
                    elif app.map["Yemen"].is_neutral():
                        app.map["Yemen"].make_adversary()
                    app.outputToHistory("Yemen Alignment worsened to %s." % app.map["Yemen"].alignment(), False)
                    app.map["Yemen"].besieged = 1
                    app.outputToHistory("Yemen now Besieged Regime.", True)
            elif self.number == 120:  # US Election
                app.executeCardUSElection(random.randint(1, 6))
        if self.remove:
            app.outputToHistory("Remove card from game.", True)
        if self.mark:
            app.outputToHistory("Place marker for card.", True)
        if self.lapsing:
            app.outputToHistory("Place card in Lapsing.", True)

