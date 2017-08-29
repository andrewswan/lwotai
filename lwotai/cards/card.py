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
            elif self.number == 74:  # Schengen Visas
                return True
            else:
                raise Exception("Has subclass")
        else:  # Unassociated Events
            if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 96:  # Danish Cartoons
                raise Exception("Has subclass")
            elif self.number == 97:  # Fatwa
                raise Exception("Has subclass")
            elif self.number == 98:  # Gaza Withdrawl
                raise Exception("Has subclass")
            elif self.number == 99:  # HAMAS Elected
                raise Exception("Has subclass")
            elif self.number == 100:  # His Ut-Tahrir
                raise Exception("Has subclass")
            elif self.number == 101:  # Kosovo
                raise Exception("Has subclass")
            elif self.number == 102:  # Former Soviet Union    #20150312PS
                raise Exception("Has subclass")
            elif self.number == 103:  # Hizballah
                raise Exception("Has subclass")
            elif self.number == 104 or self.number == 105:  # Iran
                raise Exception("Has subclass")
            elif self.number == 106:  # Jaysh al-Mahdi
                raise Exception("Has subclass")
            elif self.number == 107:  # Kurdistan
                raise Exception("Has subclass")
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
        elif self.number <= 73:  # Pirates
            raise Exception("Has subclass")
        elif self.number == 74:  # Schengen Visas
            return False
        elif self.number <= 95:  # Wahhabism
            raise Exception("Has subclass")
        elif self.number == 96:  # Danish Cartoons
            raise Exception("Has subclass")
        elif self.number == 97:  # Fatwa
            raise Exception("Has subclass")
        elif self.number == 98:  # Gaza Withdrawl
            raise Exception("Has subclass")
        elif self.number == 99:  # HAMAS Elected
            raise Exception("Has subclass")
        elif self.number == 100:  # His Ut-Tahrir
            raise Exception("Has subclass")
        elif self.number == 101:  # Kosovo
            raise Exception("Has subclass")
        elif self.number == 102:  # Former Soviet Union
            raise Exception("Has subclass")
        elif self.number == 103:  # Hizballah
            raise Exception("Has subclass")
        elif self.number == 104 or self.number == 105:  # Iran
            raise Exception("Has subclass")
        elif self.number == 106:  # Jaysh al-Mahdi
            raise Exception("Has subclass")
        elif self.number == 107:  # Kurdistan
            raise Exception("Has subclass")
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
            if self.number == 74:  # Schengen Visas
                if app.cells == 15:
                    app.output_to_history("No cells to travel.", False)
                    return
                app.handle_travel(2, False, True)
            else:
                raise Exception("Has subclass")
        else:
            if self.number == 96:  # Danish Cartoons
                raise Exception("Has subclass")
            elif self.number == 97:  # Fatwa
                raise Exception("Has subclass")
            elif self.number == 98:  # Gaza Withdrawl
                raise Exception("Has subclass")
            elif self.number == 99:  # HAMAS Elected
                raise Exception("Has subclass")
            elif self.number == 100:  # His Ut-Tahrir
                raise Exception("Has subclass")
            elif self.number == 101:  # Kosovo
                raise Exception("Has subclass")
            elif self.number == 102:  # Former Soviet Union
                raise Exception("Has subclass")
            elif self.number == 103:  # Hizballah
                raise Exception("Has subclass")
            elif self.number == 104 or self.number == 105:  # Iran
                raise Exception("Has subclass")
            elif self.number == 106:  # Jaysh al-Mahdi
                raise Exception("Has subclass")
            elif self.number == 107:  # Kurdistan
                raise Exception("Has subclass")
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
