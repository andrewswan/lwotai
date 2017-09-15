import random

from lwotai.ai import AIPlayer
from lwotai.cards.deck import Deck
from lwotai.governance import GOOD, FAIR, POOR
from lwotai.governance import governance_with_level
from lwotai.ideologies.ideologies import get_ideology, choose_ideology
from lwotai.map import Map
from lwotai.postures.posture import HARD, SOFT
from lwotai.randomizer import Randomizer
from lwotai.scenarios.scenarios import get_scenario
from lwotai.utils import Utils


class Labyrinth(object):
    """The main game entity"""

    def __init__(self, scenario_num, ideology_num, setup_function=None, test_user_input=None, **kwargs):
        # Inputs
        self.scenario = get_scenario(scenario_num)
        self.ideology = get_ideology(ideology_num)
        self.testUserInput = test_user_input
        self.randomizer = kwargs.get('randomizer', Randomizer())
        self.ai_rolls = kwargs.get('ai_rolls', False)
        # Defaults
        self.__us_reserves_card = None
        self.backlashInPlay = False
        self.cells = 0
        self.deck = Deck()
        self.funding = 0
        self.gameOver = False
        self.history = []
        self.__ai_player = AIPlayer(self)
        self.lapsing = []
        self.map = Map(self)
        self.markers = []
        self.phase = ""
        self.prestige = 0
        self.roll_turn = -1
        self.startYear = 0
        self.troops = 0
        self.turn = 1
        self.undo = False
        self.us_reserves = 0
        self.validCountryMarkers = []
        self.validGlobalMarkers = []
        self.validLapsingMarkers = []
        # Initialise
        self.valid_markers_setup()
        # Apply any passed-in setup function
        if setup_function:
            setup_function(self)
        else:
            self.scenario.set_up(self)
            self._print_initial_state()
        self._print_game_start_messages()

    def card(self, card_number):
        """Returns the given numbered card"""
        return self.deck.get(card_number)

    def _print_game_start_messages(self):
        self.output_to_history(self.scenario.name, False)
        self.output_to_history("Jihadist Ideology: %s" % self.ideology, False)
        print ""
        self.output_to_history("Game Start")
        self.output_to_history("")
        self.output_to_history("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), True)

    @staticmethod
    def debug_print(_):
        return

    def output_to_history(self, output, line_feed=True):
        print output
        self.history.append(output)
        if line_feed:
            print ""

    def _get_world_posture_str(self):
        net_hard_countries = self.map.get_net_hard_countries()
        if net_hard_countries > 0:
            return "World Posture: Hard %d" % net_hard_countries
        if net_hard_countries < 0:
            return "World Posture: Soft %d" % -net_hard_countries
        return "Even"

    def _print_initial_state(self):
        """Prints the initial game state"""
        print "Good Resources:     %d" % self.map.get_good_resources()
        print "Islamist Resources: %d" % self.map.get_islamist_rule_resources()
        print "---"
        print "Fair/Good Muslim Countries:   %d" % self._count_good_or_fair_muslim_countries()
        print "Poor/Islamist Rule Countries: %d" % self._count_poor_or_islamist_rule_countries()
        print ""
        print "GWOT"
        print "US Posture: %s" % self.us_posture()
        print self._get_world_posture_str()
        print "US Prestige: %d" % self.prestige
        print ""

    def _count_good_or_fair_muslim_countries(self):
        """Returns the number of Muslim countries with Good or Fair governance"""
        return self.map.count_countries(lambda c: c.is_muslim() and (c.is_good() or c.is_fair()))

    def _count_poor_or_islamist_rule_countries(self):
        """Returns the number of Muslim countries with Poor governance or under Islamist Rule"""
        return self.map.count_countries(lambda c: c.is_muslim() and (c.is_poor() or c.is_islamist_rule()))

    def valid_markers_setup(self):
        self.validGlobalMarkers.append("Moro Talks")
        self.validGlobalMarkers.append("NEST")
        self.validGlobalMarkers.append("Abbas")
        self.validGlobalMarkers.append("Anbar Awakening")
        self.validGlobalMarkers.append("Saddam Captured")
        self.validGlobalMarkers.append("Wiretapping")
        self.validGlobalMarkers.append("Benazir Bhutto")
        self.validGlobalMarkers.append("Enhanced Measures")
        self.validGlobalMarkers.append("Indo-Pakistani Talks")
        self.validGlobalMarkers.append("Iraqi WMD")
        self.validGlobalMarkers.append("Libyan Deal")
        self.validGlobalMarkers.append("Libyan WMD")
        self.validGlobalMarkers.append("Patriot Act")
        self.validGlobalMarkers.append("Renditions")
        self.validGlobalMarkers.append("Vieira de Mello Slain")
        self.validGlobalMarkers.append("Abu Sayyaf")
        self.validGlobalMarkers.append("Al-Anbar")
        self.validGlobalMarkers.append("Bhutto Shot")
        self.validGlobalMarkers.append("Pirates")
        self.validGlobalMarkers.append("Leak-Enhanced Measures")
        self.validGlobalMarkers.append("Leak-Wiretapping")
        self.validGlobalMarkers.append("Leak-Renditions")
        self.validCountryMarkers.append("CTR")    # 20150616PS
        self.validCountryMarkers.append("NATO")
        self.validCountryMarkers.append("Sadr")
        self.validCountryMarkers.append("FATA")
        self.validLapsingMarkers.append("Biometrics")
        self.validLapsingMarkers.append("The door of Itjihad was closed")
        self.validLapsingMarkers.append("GTMO")
        self.validLapsingMarkers.append("Oil Price Spike")

    @staticmethod
    def _matches(input_text, full_string):
        """Indicates whether the given text starts with the given prefix, case-insensitively"""
        return input_text and full_string.lower().startswith(input_text.lower())

    def my_raw_input(self, prompt):
        """Reads a line from the test input, if any is left, otherwise from standard input"""
        fake_input = self._next_fake_user_input()
        if fake_input:
            print "TEST: Prompt: '%s' Value: '%s'" % (prompt, fake_input)
            return fake_input
        return raw_input(prompt)

    def _next_fake_user_input(self):
        """Returns the next line of fake user input, or None"""
        if self.testUserInput and len(self.testUserInput) > 0:
            return self.testUserInput.pop(0)
        return None

    def get_country_from_user(self, prompt, special, help_function, help_parameter=None):
        good_country = None
        while not good_country:
            country_name = self.my_raw_input(prompt)
            if country_name == "":
                return ""
            elif country_name == "?" and help_function:
                help_function(help_parameter)
                continue
            elif country_name == special:
                return special
            matching_countries = self.map.find_by_name(country_name)
            if not matching_countries:
                print "Unrecognized country."
                print ""
            elif len(matching_countries) > 1:
                print "Be more specific", matching_countries
                print ""
            else:
                good_country = matching_countries[0]
        return good_country

    def get_num_troops_from_user(self, prompt, maximum):
        """Prompts the user for a number of troops, up to the given maximum.
        Returns that number, or None if the user aborted."""
        while True:
            troops_str = self.my_raw_input(prompt)
            if troops_str == "":
                return None
            try:
                troops = int(troops_str)
                if 0 <= troops <= maximum:
                    return troops
                else:
                    print "Not enough troops (max %d)." % maximum
                    print ""
            except ValueError:
                print "Invalid number '%s'" % troops_str
                print ""

    def get_card_num_from_user(self, prompt):
        while True:
            try:
                card_num_str = self.my_raw_input(prompt)
                if card_num_str.lower() == "none":
                    return "none"
                card_num = int(card_num_str)
                if card_num <= 120:
                    return card_num
                else:
                    print "Enter a card number."
                    print ""
            except ValueError:
                print "Enter a card number."
                print ""

    def get_plot_countries(self):
        """Returns the countries that contain plots"""
        return [country for country in self.get_countries() if country.plots > 0]

    def get_plot_type_from_user(self, prompt):
        while True:
            try:
                plot_type = self.my_raw_input(prompt)
                if self._matches(plot_type, "WMD"):
                    return "WMD"
                plot_type_num = int(plot_type)
                if 1 <= plot_type_num <= 3:
                    return plot_type_num
                else:
                    print "Enter 1, 2, 3 or W for WMD."
                    print ""
            except ValueError:
                print "Enter 1, 2, 3 or W for WMD."
                print ""

    def get_random_shia_mix_country(self):
        """Returns the name of a Shia-Mix country rolled up on the AI chart"""
        rolls = self.randomizer.roll_d6(3)
        return self.map.look_up_shia_mix_country(rolls)

    def get_roll(self, purpose):
        """Either rolls a d6 or asks the user to do so, based on the provided preference"""
        if self.ai_rolls:
            ai_roll = random.randint(1, 6)
            print "Auto %s roll: %d" % (purpose, ai_roll)
            return ai_roll
        while True:
            try:
                user_input = self.my_raw_input("Enter %s roll: " % purpose)
                roll_num = int(user_input)
                if 1 <= roll_num <= 6:
                    return roll_num
                else:
                    raise ValueError("Roll should be from 1 to 6")
            except ValueError:
                print "Entry error"
                print ""

    def get_yes_no_from_user(self, prompt):
        while True:
            answer = self.my_raw_input(prompt)
            if self._matches(answer, "yes"):
                return True
            elif self._matches(answer, "no"):
                return False
            else:
                print "Enter y or n."
                print ""

    def get_posture_from_user(self, prompt):
        """Prompts the user to pick a posture"""
        while True:
            posture = self.my_raw_input(prompt)
            if self._matches(posture, "hard"):
                return HARD
            elif self._matches(posture, "soft"):
                return SOFT
            else:
                print "Enter h or s."
                print ""

    def get_event_or_ops_from_user(self, prompt):
        """Asks the user to choose between "event" or "ops" (or None)"""
        while True:
            choice = self.my_raw_input("%s (enter e or o): " % prompt)
            if choice == "":
                return None
            elif self._matches(choice, "event"):
                return "event"
            elif self._matches(choice, "ops"):
                return "ops"
            else:
                print "Enter e or o, or press <Enter> to cancel."
                print ""

    def modified_woi_roll(self, base_roll, country_name, use_gwot_penalty=True):
        modified_roll = base_roll

        if self.prestige <= 3:
            modified_roll -= 1
            self.output_to_history("-1 for Prestige", False)
        elif 7 <= self.prestige <= 9:
            modified_roll += 1
            self.output_to_history("+1 for Prestige", False)
        elif self.prestige >= 10:
            modified_roll += 2
            self.output_to_history("+2 for Prestige", False)

        country = self.map.get(country_name)
        if country.is_ally() and country.is_fair():
            modified_roll -= 1
            self.output_to_history("-1 for Attempt to shift to Good", False)

        if use_gwot_penalty:
            gwot_penalty = self.gwot_penalty()
            modified_roll -= gwot_penalty
            if gwot_penalty:
                self.output_to_history("-%d penalty for GWOT Relations" % gwot_penalty, False)

        if country.get_aid() > 0:
            modified_roll += country.get_aid()  # 20150131PS use number of aid markers rather than 1
            self.output_to_history("+%s for Aid" % country.get_aid(), False)

        for adj in country.links:
            if adj.is_ally() and adj.is_good():
                modified_roll += 1
                self.output_to_history("+1 for Adjacent Good Ally", False)
                break
        return modified_roll

    def gwot_penalty(self):
        """Returns the penalty to be subtracted from a WoI roll, i.e. a number between 0 (no penalty) and 3"""
        net_hard_countries = self.map.get_net_hard_countries()
        if net_hard_countries > 0:
            world_posture = HARD
        elif net_hard_countries < 0:
            world_posture = SOFT
        else:
            world_posture = None
        if self.us_posture() == world_posture:
            return 0
        return abs(net_hard_countries)

    def change_prestige(self, delta, line_feed=True):
        """Changes US prestige by the given amount, then prints the new value"""
        if delta < 0:
            self._reduce_prestige(-delta)
        elif delta > 0:
            self._increase_prestige(delta)
        self.output_to_history("Prestige now %d" % self.prestige, line_feed)

    def change_funding(self, delta, line_feed=True):
        self.funding += delta
        if self.funding < 1:
            self.funding = 1
        elif self.funding > 9:
            self.funding = 9
        self.output_to_history("Jihadist Funding now %d" % self.funding, line_feed)

    def validate(self):
        """Checks that this instance is in a valid state"""
        # Check cells
        cell_count = 0
        for country_name in self.map.country_names():
            country = self.map.get(country_name)
            cell_count += country.activeCells + country.sleeperCells
        cell_count += self.cells
        if cell_count != 15:
            print "WARNING: Expected 15 cells in total but have %d (%d on the track)" % (cell_count, self.cells)
        # Check troops
        troop_count = 0
        for country_name in self.map.country_names():
            troop_count += self.map.get(country_name).troops()
        troop_count += self.troops
        assert troop_count == 15, "Expected 15 troops but have %d" % troop_count
        # Check tested countries
        for country in self.get_countries():
            country.check_is_tested()

    def place_cells(self, country_name, cells_requested):
        if self.cells == 0:
            self.output_to_history("No cells are on the Funding Track.", True)
        else:
            self.test_country(country_name)
            cells_to_move = min(cells_requested, self.cells)
            self.map.get(country_name).sleeperCells += cells_to_move
            # remove cadre
            self.map.get(country_name).cadre = 0
            self.cells -= cells_to_move
            self.output_to_history("%d Sleeper Cell(s) placed in %s" % (cells_to_move, country_name), False)
            self.output_to_history(self.map.get(country_name).summary(), True)

    def remove_cell(self, country_name, side):
        # 20150131PS included Sadr in cell count, added test for side to determine order of removal
        if self.map.get(country_name).total_cells(True) == 0:
            return
        if side == "US":
            if self.map.get(country_name).sleeperCells > 0:
                self.map.get(country_name).sleeperCells -= 1
                self.cells += 1
                self.output_to_history("Sleeper Cell removed from %s." % country_name, True)
            elif "Sadr" in self.map.get(country_name).markers:
                self.map.get(country_name).markers.remove("Sadr")
                self.output_to_history("Sadr removed from %s." % country_name, True)
            elif self.map.get(country_name).activeCells > 0:
                self.map.get(country_name).activeCells -= 1
                self.cells += 1
                self.output_to_history("Active Cell removed from %s." % country_name, True)
        else:
            if self.map.get(country_name).activeCells > 0:
                self.map.get(country_name).activeCells -= 1
                self.cells += 1
                self.output_to_history("Active Cell removed from %s." % country_name, True)
            elif self.map.get(country_name).sleeperCells > 0:
                self.map.get(country_name).sleeperCells -= 1
                self.cells += 1
                self.output_to_history("Sleeper Cell removed from %s." % country_name, True)
            elif "Sadr" in self.map.get(country_name).markers:
                self.map.get(country_name).markers.remove("Sadr")
                self.output_to_history("Sadr removed from %s." % country_name, True)
        if self.map.get(country_name).total_cells() == 0:
            self.output_to_history("Cadre added in %s." % country_name, True)
            self.map.get(country_name).cadre = 1

    def remove_all_cells_from_country(self, country_name):
        cells_to_remove = self.map.get(country_name).total_cells()
        if self.map.get(country_name).sleeperCells > 0:
            number_of_cells = self.map.get(country_name).sleeperCells
            self.map.get(country_name).sleeperCells -= number_of_cells
            self.cells += number_of_cells
            self.output_to_history("%d Sleeper Cell(s) removed from %s." % (number_of_cells, country_name), False)
        if self.map.get(country_name).activeCells > 0:
            number_of_cells = self.map.get(country_name).activeCells
            self.map.get(country_name).activeCells -= number_of_cells
            self.cells += number_of_cells
            self.output_to_history("%d Active Cell(s) removed from %s." % (number_of_cells, country_name), False)
        if cells_to_remove > 0:
            self.output_to_history("Cadre added in %s." % country_name, False)
            self.map.get(country_name).cadre = 1

    def remove_marker(self, marker_name):
        """Removes the given marker"""
        if marker_name in self.markers:
            self.markers.remove(marker_name)

    def improve_governance(self, country_name):
        """Improves governance in the named country"""
        self.get_country(country_name).improve_governance()

    def worsen_governance(self, country_name):
        """Worsens governance in the named country"""
        self.get_country(country_name).worsen_governance()

    def num_cells_available(self, ignore_funding=False):
        available_cells = self.cells
        if ignore_funding:
            return available_cells
        if self.funding <= 3:
            available_cells -= 10
        elif self.funding <= 6:
            available_cells -= 5
        return max(available_cells, 0)

    def num_islamist_rule(self):
        return self.num_countries(lambda c: c.is_islamist_rule())

    def num_besieged(self):
        return self.num_countries(lambda c: c.is_besieged())

    def num_regime_change(self):
        return self.num_countries(lambda c: c.is_regime_change())

    def num_adversary(self):
        return self.num_countries(lambda c: c.is_adversary())

    def num_disruptable(self):
        """Returns the number of countries in which the US player can Disrupt"""
        return self.num_countries(lambda c: c.can_disrupt())

    def num_countries(self, predicate):
        """Returns the number of countries matching the given predicate"""
        return self.map.count_countries(predicate)

    def oil_price_spikes(self):
        """Returns the number of oil price spikes in effect"""
        return Utils.count(self.lapsing, lambda marker: marker == "Oil Price Spike")

    def country_resources_by_name(self, country_name):
        """
        Returns the amount of resources that the named country produces,
        taking into account game state such as Oil Price Spikes.
        """
        return self.country_resources(self.map.get(country_name))

    def country_resources(self, country):
        """
        Returns the amount of resources that the given country produces,
        taking into account game state such as Oil Price Spikes.
        """
        return country.get_resources(self.oil_price_spikes())

    def handle_muslim_woi(self, roll, country_name):
        if roll <= 3:
            self.output_to_history("* WoI in %s failed." % country_name)
        elif roll == 4:
            if self.map.get(country_name).get_aid() == 0:        # 20150131PS check for existing aid marker
                self.map.get(country_name).set_aid(1)
                self.output_to_history("* WoI in %s adds Aid." % country_name, False)
                self.output_to_history(self.map.get(country_name).summary(), True)
        else:
            if self.map.get(country_name).is_neutral():
                self.map.get(country_name).make_ally()
                self.output_to_history("* WoI in %s succeeded - Alignment now Ally." % country_name, False)
                self.output_to_history(self.map.get(country_name).summary(), True)
            elif self.map.get(country_name).is_ally():
                self.improve_governance(country_name)
                self.output_to_history("* WoI in %s succeeded - Governance now %s." %
                                       (country_name, self.map.get(country_name).governance_str()), False)
                self.output_to_history(self.map.get(country_name).summary(), True)

    def toggle_us_posture(self):
        """Switches the US posture between Hard and Soft"""
        self.us().toggle_posture()
        self.output_to_history("* Reassessment = US Posture now %s" % self.us_posture())

    def handle_regime_change(self, where, move_from, how_many, governance_roll, prestige_rolls):
        if self.us().is_soft():
            return
        if move_from == 'track':
            self.troops -= how_many
        else:
            self.map.get(move_from).change_troops(-how_many)
        self.map.get(where).change_troops(how_many)
        sleepers = self.map.get(where).sleeperCells
        self.map.get(where).sleeperCells = 0
        self.map.get(where).activeCells += sleepers
        self.map.get(where).make_ally()
        if governance_roll <= 4:
            self.map.get(where).make_poor()
        else:
            self.map.get(where).make_fair()
        self.map.get(where).make_regime_change()
        prestige_multiplier = 1
        if prestige_rolls[0] <= 4:
            prestige_multiplier = -1
        self.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
        self.output_to_history("* Regime Change in %s" % where, False)
        self.output_to_history(self.map.get(where).summary(), False)
        if move_from == "track":
            self.output_to_history("%d Troops on Troop Track" % self.troops, False)
        else:
            self.output_to_history("%d Troops in %s" % (self.map.get(move_from).troops(), move_from), False)
        self.output_to_history("US Prestige %d" % self.prestige)
        if where == "Iraq" and "Iraqi WMD" in self.markers:
            self.markers.remove("Iraqi WMD")
            self.output_to_history("Iraqi WMD no longer in play.", True)
        if where == "Libya" and "Libyan WMD" in self.markers:
            self.markers.remove("Libyan WMD")
            self.output_to_history("Libyan WMD no longer in play.", True)

    def handle_withdraw(self, move_from, move_to, how_many, prestige_rolls):
        if self.us().is_hard():
            return
        self.map.get(move_from).change_troops(-how_many)
        if move_to == "track":
            self.troops += how_many
        else:
            self.map.get(move_to).change_troops(how_many)
        self.map.get(move_from).set_aid(0)
        self.map.get(move_from).make_besieged()
        prestige_multiplier = 1
        if prestige_rolls[0] <= 4:
            prestige_multiplier = -1
        self.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
        self.output_to_history("* Withdraw troops from %s" % move_from, False)
        self.output_to_history(self.map.get(move_from).summary(), False)
        if move_to == "track":
            self.output_to_history("%d Troops on Troop Track" % self.troops, False)
        else:
            self.output_to_history("%d Troops in %s" % (self.map.get(move_to).troops(), move_to), False)
            self.output_to_history(self.map.get(move_to).summary(), False)
        self.output_to_history("US Prestige %d" % self.prestige)

    def handle_disrupt(self, target_name):
        """Performs a disrupt action in the named country"""
        target = self.map.get(target_name)
        number_to_disrupt = self._get_number_of_cells_to_disrupt(target)
        if target.total_cells(False) <= 0 and target.has_cadre():
            self._disrupt_cadre(target)
        elif target.total_cells(False) <= number_to_disrupt:
            self._disrupt_all_cells(number_to_disrupt, target)
        else:
            # More cells than disrupt actions
            if target.activeCells <= 0:
                target.activate_sleepers(number_to_disrupt)
                self.output_to_history("* %d cell(s) disrupted in %s." % (number_to_disrupt, target_name), False)
            elif target.sleeperCells <= 0:
                self._disrupt_active_cells(number_to_disrupt, target)
            else:
                # A mixture of active and sleeper cells
                if number_to_disrupt == 1:
                    self._disrupt_one_cell(target)
                else:
                    self._disrupt_two_cells(target)
        if target.troops() >= 2:
            self._increase_prestige(1)
            self.output_to_history("US Prestige now %d." % self.prestige, False)
        self.output_to_history(target.summary(), True)

    def _get_two_cell_types(self, options):
        """Prompts the user to choose one of the given options for disrupting two cells, returns None if not valid"""
        prompt = "You can disrupt two cells. Enter one of %s for active or sleeper cells: " % options
        cell_types = self.my_raw_input(prompt)
        if cell_types and cell_types.lower() in options:
            return cell_types.lower()
        return None

    def _disrupt_two_cells(self, target):
        """Disrupts two cells in the given target Country (assumes at least one active and one sleeper)"""
        assert target.activeCells and target.sleeperCells
        cell_types = None
        while not cell_types:
            if target.sleeperCells >= 2 and target.activeCells >= 2:
                # Free choice
                cell_types = self._get_two_cell_types(["aa", "as", "ss"])
            elif target.sleeperCells >= 2:
                # 1 active cell
                cell_types = self._get_two_cell_types(["as", "ss"])
            elif target.activeCells >= 2:
                # 1 or 2 active cells and 1 sleeper cell
                cell_types = self._get_two_cell_types(["aa", "as"])
        if cell_types == "aa":
            target.activeCells -= 2
            self.cells += 2
        elif cell_types == "as":
            target.sleeperCells -= 1
            self.cells += 1
        else:
            # Two sleepers
            target.sleeperCells -= 2
            target.activeCells += 2
        self.output_to_history("* 2 cells disrupted in %s." % target.name)

    def _disrupt_one_cell(self, target):
        """Disrupts one cell in the given target Country"""
        cell_type = self._get_cell_type("You can disrupt one cell. Enter a or s for either an active or sleeper cell: ")
        if cell_type == "a":
            target.activeCells -= 1
            self.cells += 1
            self.output_to_history("* 1 cell disrupted in %s." % target.name)
        else:
            # sleeper
            target.sleeperCells -= 1
            target.activeCells += 1
            self.output_to_history("* 1 cell disrupted in %s." % target.name)

    def _disrupt_active_cells(self, number_to_disrupt, target):
        """Disrupts the given number of active cells in the given target Country"""
        assert target.activeCells >= number_to_disrupt
        target.activeCells -= number_to_disrupt
        self.cells += number_to_disrupt
        self.output_to_history("* %d cell(s) disrupted in %s." % (number_to_disrupt, target.name), False)
        if target.total_cells(False) <= 0:
            self.output_to_history("Cadre added in %s." % target.name, False)
            target.cadre = 1

    def _disrupt_all_cells(self, number_to_disrupt, target):
        """Disrupts all cells in the given target Country"""
        self.output_to_history(
            "* %d cell(s) disrupted in %s." % (target.total_cells(False), target.name), False)
        if target.sleeperCells > 0:
            # First make all sleepers active
            target.activeCells += target.sleeperCells
            number_to_disrupt -= target.sleeperCells
            target.sleeperCells = 0
        if number_to_disrupt > 0:
            # Spend any remaining removals on removing active cells
            target.activeCells -= number_to_disrupt
            self.cells += number_to_disrupt
            if target.activeCells < 0:
                target.activeCells = 0
            if self.cells > 15:
                self.cells = 15
        if target.total_cells(False) <= 0 and not target.has_cadre():
            self.output_to_history("Cadre added to %s." % target.name, False)
            target.cadre = 1

    def _get_number_of_cells_to_disrupt(self, target):
        """Returns the number of cells that can be disrupted in the given country"""
        if "Al-Anbar" in self.markers and target.name in ["Iraq", "Syria"]:
            return 1
        elif target.troops() >= 2 or target.is_hard():
            return min(2, target.total_cells(False))
        else:
            return 1

    def _disrupt_cadre(self, target):
        """Disrupts all cadre in the given country"""
        if "Al-Anbar" not in self.markers or target.name not in ["Iraq", "Syria"]:
            self.output_to_history("* Cadre removed in %s" % target.name)
            target.cadre = 0

    def _get_cell_type(self, prompt):
        """Prompts the user to choose a cell type; 'a' or 's', case-insensitive"""
        while True:
            cell_type = self.my_raw_input(prompt)
            if cell_type.lower() in ["a", "s"]:
                return cell_type.lower()

    def ai_major_jihad(self, card_number):
        card = self.card(card_number)
        self.__ai_player.ai_flow_chart_major_jihad(card)

    def excess_cells_needed_for_major_jihad(self):
        return self.ideology.excess_cells_for_major_jihad()

    def execute_jihad(self, country_name, rolls):
        self.__ai_player.execute_jihad(country_name, rolls)

    def bhutto_in_play(self):
        return "Benazir Bhutto" in self.markers

    def handle_jihad(self, country_name, ops):
        return self.__ai_player.handle_jihad(country_name, ops)

    def handle_radicalization(self, ops):
        self.__ai_player.handle_radicalization(ops)

    def major_jihad_choice(self, ops):
        return self.__ai_player.major_jihad_choice(ops)

    def major_jihad_possible(self, ops):
        """Return list of countries where major jihad is possible."""
        excess_cells_needed = self.excess_cells_needed_for_major_jihad()
        bhutto = self.bhutto_in_play()
        return [country.name for country in self.map.countries() if
                country.is_major_jihad_possible(ops, excess_cells_needed, bhutto)]

    def minor_jihad_in_good_fair_choice(self, ops, is_abu_ghurayb=False, is_al_jazeera=False):
        possible = []
        for country in self.map.countries():
            if is_abu_ghurayb:
                if country.is_ally() and not country.is_islamist_rule():
                    possible.append(country.name)
            elif is_al_jazeera:
                if country.name == "Saudi Arabia" or self.is_adjacent(country.name, "Saudi Arabia"):
                    if country.troops() > 0:
                        possible.append(country.name)
            elif country.is_muslim() and (country.is_good() or country.is_fair()) and country.total_cells(True) > 0:
                if "Benazir Bhutto" in self.markers and country.name == "Pakistan":
                    continue
                possible.append(country.name)
        if not possible:
            return False
        else:
            country_scores = {}
            for country_name in possible:
                if self.map.get(country_name).is_good():
                    country_scores[country_name] = 2000000
                else:
                    country_scores[country_name] = 1000000
                if country_name == "Pakistan":
                    country_scores[country_name] += 100000
                if self.map.get(country_name).get_aid() > 0:
                    country_scores[country_name] += 10000
                if self.map.get(country_name).is_besieged():
                    country_scores[country_name] += 1000
                country_scores[country_name] += (self.country_resources_by_name(country_name) * 100)
                country_scores[country_name] += random.randint(1, 99)
            country_order = []
            for country_name in country_scores:
                country_order.append(
                    (country_scores[country_name], (self.map.get(country_name).total_cells(True)), country_name))
            country_order.sort()
            country_order.reverse()
            return_list = []
            ops_remaining = ops
            for countryData in country_order:
                rolls = min(ops_remaining, countryData[1])
                return_list.append((countryData[2], rolls))
                ops_remaining -= rolls
                if ops_remaining <= 0:
                    break
            return return_list

    def _increase_prestige(self, amount):
        """Increases US prestige by the given amount (to no more than 12)"""
        assert amount > 0
        self.prestige += amount
        if self.prestige > 12:
            self.prestige = 12

    def _reduce_prestige(self, amount):
        """Reduces US prestige by the given amount (to no less than 1)"""
        assert amount > 0
        self.prestige -= amount
        if self.prestige < 1:
            self.prestige = 1

    def recruit_choice(self, ops, is_madrassas=False):
        self.debug_print("DEBUG: recruit with remaining %d ops" % ops)
        self.debug_print("DEBUG: recruit with remaining %d ops" % (2 * ops))
        country_scores = {}
        for country in self.map.countries():
            if country.can_recruit(is_madrassas):
                country_recruit_score = country.get_recruit_score(ops)
                if country_recruit_score is not None:
                    country_scores[country.name] = country_recruit_score
        for country_name in country_scores:
            country = self.map.get(country_name)
            self.debug_print("c")
            if country.is_besieged():
                country_scores[country_name] += 100000
            country_scores[country_name] += (1000 * (country.troops() + country.total_cells(True)))
            country_scores[country_name] += 100 * self.country_resources_by_name(country_name)
            country_scores[country_name] += random.randint(1, 99)
        country_order = []
        for country_name in country_scores:
            self.debug_print("here: %d " % country_scores[country_name])
            if country_scores[country_name] > 0:
                country_order.append(
                    (country_scores[country_name], (self.map.get(country_name).total_cells(True)), country_name))
        country_order.sort()
        country_order.reverse()
        if not country_order:
            self.debug_print("d")
            return False
        else:
            self.debug_print("e")
            return country_order[0][2]

    def execute_recruit(
            self, country_name, ops, rolls, recruit_override=None, is_jihadist_videos=False, is_madrassas=False):
        self.output_to_history("* Recruit to %s" % country_name)
        cells_requested = ops * self.ideology.recruits_per_success()
        cells = self.num_cells_available(is_madrassas or is_jihadist_videos)
        cells_to_recruit = min(cells_requested, cells)
        if self.map.get(country_name).is_regime_change() or self.map.get(country_name).is_islamist_rule():
            if self.map.get(country_name).is_regime_change():
                self.output_to_history("Recruit to Regime Change country automatically successful.", False)
            else:
                self.output_to_history("Recruit to Islamist Rule country automatically successful.", False)
            self.cells -= cells_to_recruit
            self.map.get(country_name).sleeperCells += cells_to_recruit

            if cells_to_recruit == 0 and is_jihadist_videos:
                self.map.get(country_name).cadre = 1
                self.output_to_history("No cells available to recruit. Cadre added.", False)
                self.output_to_history(self.map.get(country_name).summary(), True)
                return ops - 1
            else:
                self.map.get(country_name).cadre = 0

            self.output_to_history("%d sleeper cells recruited to %s." % (cells_to_recruit, country_name), False)
            self.output_to_history(self.map.get(country_name).summary(), True)
            return ops - self.ideology.ops_to_recruit(cells_to_recruit)
        else:
            ops_remaining = ops
            i = 0
            if (self.num_cells_available(is_jihadist_videos)) <= 0 and (ops_remaining > 0):
                self.map.get(country_name).cadre = 1
                self.output_to_history("No cells available to recruit. Cadre added.", False)
                self.output_to_history(self.map.get(country_name).summary(), True)
                return ops - 1
            else:
                while self.num_cells_available(is_madrassas or is_jihadist_videos) > 0 and ops_remaining > 0:
                    if self.map.get(country_name).is_recruit_success(rolls[i], recruit_override):
                        cells_moving = min(self.num_cells_available(is_madrassas or is_jihadist_videos),
                                           self.ideology.recruits_per_success())
                        self.cells -= cells_moving
                        self.map.get(country_name).sleeperCells += cells_moving
                        self.map.get(country_name).cadre = 0
                        self.output_to_history("Roll successful, %d sleeper cell(s) recruited." % cells_moving, False)
                    else:
                        self.output_to_history("Roll failed.", False)
                        if is_jihadist_videos:
                            self.map.get(country_name).cadre = 1
                            self.output_to_history("Cadre added.", False)
                    ops_remaining -= 1
                    i += 1
                self.output_to_history(self.map.get(country_name).summary(), True)
                return ops_remaining

    def handle_recruit(self, ops, is_madrassas=False):
        self.debug_print("recruit ops: ")
        self.debug_print("DEBUG: recruit with remaining %d ops" % ops)
        country_name = self.recruit_choice(ops, is_madrassas)
        if not country_name:
            self.output_to_history("* No countries qualify to Recruit.", True)
            return ops
        else:
            if is_madrassas:
                cells = self.cells
            else:
                if "GTMO" in self.lapsing:
                    self.output_to_history("* Cannot Recruit due to GTMO.", True)
                    return ops
                cells = self.num_cells_available()
            if cells <= 0:
                self.output_to_history("* No cells available to Recruit.", True)
                return ops
            else:
                rolls = [random.randint(1, 6) for _ in range(ops)]
                return self.execute_recruit(country_name, ops, rolls, None, False, is_madrassas)

    def is_adjacent(self, here, there):
        if "Patriot Act" in self.markers:
            if here == "United States" or there == "United States":
                if here == "Canada" or there == "Canada":
                    return True
                else:
                    return False
        if self.map.get(here) in self.map.get(there).links:
            return True
        if self.map.get(here).schengen and self.map.get(there).schengen:
            return True
        if self.map.get(here).schengenLink and self.map.get(there).schengen:
            return True
        if self.map.get(here).schengen and self.map.get(there).schengenLink:
            return True
        return False

    def adjacent_country_has_cell(self, target_country):
        for country_name in self.map.country_names():
            if self.is_adjacent(target_country, country_name):
                if self.map.get(country_name).total_cells(True) > 0:
                    return True
        return False

    @staticmethod
    def in_lists(element, lists):
        for inner_list in lists:
            if element in inner_list:
                return True
        return False

    def country_distance(self, start, end):
        if start == end:
            return 0
        distance_groups = [[start]]
        distance = 1
        while not self.in_lists(end, distance_groups):
            distance_group = distance_groups[distance - 1]
            next_wave = []
            for country_name in distance_group:
                for subCountry in self.map.country_names():
                    if not self.in_lists(subCountry, distance_groups):
                        if self.is_adjacent(subCountry, country_name):
                            if subCountry == end:
                                return distance
                            if subCountry not in next_wave:
                                next_wave.append(subCountry)
            distance_groups.append(next_wave)
            distance += 1

    def travel_destination_choose_based_on_priority(self, country_names):
        for country_name in country_names:
            if country_name == "Pakistan":
                return country_name
        max_resources = 0
        for country_name in country_names:
            if self.country_resources_by_name(country_name) > max_resources:
                max_resources = self.country_resources_by_name(country_name)
        max_destinations = [name for name in country_names if self.country_resources_by_name(name) == max_resources]
        return random.choice(max_destinations)

    def contains_country(self, predicate):
        """Indicates whether the map contains a country matching the given predicate"""
        return self.map.contains(predicate)

    def get_country(self, country_name):
        """Returns the country with the given name (case-sensitive), if it exists"""
        return self.map.get(country_name)

    def get_countries(self):
        """Returns the countries on the map"""
        return self.map.countries()

    def get_country_names(self):
        """Returns the names of countries in the game"""
        return [country.name for country in self.get_countries()]

    def get_posture(self, country_name):
        """Returns the given country's posture"""
        return self.get_country(country_name).get_posture()

    def set_posture(self, country_name, posture):
        """Sets the posture of the named country"""
        self.get_country(country_name).set_posture(posture)

    def travel_destinations(self, ops, is_radicalization=False):
        dests = []
        # A non-Islamist Rule country with Regime Change, Besieged Regime, or Aid, if any
        if not is_radicalization:
            subdests = []
            for country in self.map.countries():
                if (not country.is_islamist_rule()) and\
                        (country.is_besieged() or country.is_regime_change() or country.get_aid() > 0):
                    if "Biometrics" in self.lapsing and not self.adjacent_country_has_cell(country.name):
                        continue
                    subdests.append(country.name)
            if len(subdests) == 1:
                dests.append(subdests[0])
            elif len(subdests) > 1:
                dests.append(self.travel_destination_choose_based_on_priority(subdests))
            if len(dests) == ops:
                return dests

        # A Poor country where Major Jihad would be possible if two (or fewer) cells were added.
        subdests = []
        for country in self.map.countries():
            if country.is_poor() and\
                    (country.total_cells(True) + 2 - country.troops()) >= self.excess_cells_needed_for_major_jihad():
                if not is_radicalization and "Biometrics" in self.lapsing and\
                        not self.adjacent_country_has_cell(country.name):
                    continue
                subdests.append(country.name)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travel_destination_choose_based_on_priority(subdests))
        if len(dests) == ops:
            return dests

        # A Good or Fair Muslim country with at least one cell adjacent.
        subdests = []
        for country in self.map.countries():
            if country.is_muslim() and (country.is_good() or country.is_fair()):
                if self.adjacent_country_has_cell(country.name):
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.adjacent_country_has_cell(country.name):
                        subdests.append(country.name)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travel_destination_choose_based_on_priority(subdests))
        if len(dests) == ops:
            return dests

        # An unmarked non-Muslim country if US Posture is Hard, or a Soft non-Muslim country if US Posture is Soft.
        subdests = []
        if self.us().is_hard():
            for country in self.get_countries():
                if country.is_non_muslim() and not country.get_posture():
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.adjacent_country_has_cell(country.name):
                        subdests.append(country.name)
        else:
            for country in self.get_countries():
                if country.name != "United States" and country.is_non_muslim() and country.is_soft():
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.adjacent_country_has_cell(country.name):
                        subdests.append(country.name)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(random.choice(subdests))
        if len(dests) == ops:
            return dests

            # Random
        if (not is_radicalization) and ("Biometrics" in self.lapsing):
            subdests = []
            for country_name in self.map.country_names():
                if self.adjacent_country_has_cell(country_name):
                    subdests.append(country_name)
            if len(subdests) > 0:
                while len(dests) < ops:
                    dests.append(random.choice(subdests))
        else:
            while len(dests) < ops:
                dests.append(random.choice(self.map.country_names()))

        return dests

    def names_of_countries(self, predicate):
        """Returns the names of countries matching the given predicate"""
        return [country.name for country in self.find_countries(predicate)]

    def travel_destinations_schengen_visas(self):
        """
        Returns the names of countries that are valid travel
        destinations for the Schengen Visas event
        """
        if self.us().is_hard():
            candidates = self.names_of_countries(lambda c: c.schengen and not c.get_posture())
        else:
            candidates = self.names_of_countries(lambda c: c.schengen and c.is_soft())
        if len(candidates) == 1:
            return [candidates[0], candidates[0]]  # yes, same one twice
        if len(candidates) > 1:
            return self.randomizer.pick(2, candidates)
        schengens = self.names_of_countries(lambda c: c.schengen)
        return self.randomizer.pick(2, schengens)

    def travel_source_choose_based_on_priority(self, country_list, i, destinations):
        sub_possibles = []
        for country in country_list:
            if self.map.get(country).activeCells > 0:
                sub_possibles.append(country)
        if len(sub_possibles) == 1:
            return sub_possibles[0]
        elif len(sub_possibles) > 1:
            return random.choice(sub_possibles)
        else:
            sub_possibles = []
            for country in country_list:
                for j in range(len(destinations)):
                    if (i != j) and (country == destinations[j]):
                        sub_possibles.append(country)
        if len(sub_possibles) == 1:
            return sub_possibles[0]
        elif len(sub_possibles) > 1:
            return random.choice(sub_possibles)
        else:
            return random.choice(country_list)

    def travel_source_box_one(self, i, destinations, sources, ops, is_radicalization=False):
        possibles = []
        for country in self.get_countries():
            if country.is_islamist_rule():
                num_times_is_source = sources.count(country.name)
                if (country.sleeperCells + country.activeCells - num_times_is_source) > ops:
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.is_adjacent(country.name, destinations[i]):
                        possibles.append(country.name)
        if not possibles:
            return False
        elif len(possibles) == 1:
            return possibles[0]
        else:
            return self.travel_source_choose_based_on_priority(possibles, i, destinations)

    def travel_source_box_two(self, i, destinations, sources, is_radicalization=False):
        possibles = []
        for country in self.get_countries():
            if country.is_regime_change():
                num_times_is_source = sources.count(country.name)
                if ((country.sleeperCells + country.activeCells) - num_times_is_source) > country.troops():
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.is_adjacent(country.name, destinations[i]):
                        possibles.append(country.name)
        if not possibles:
            return False
        elif len(possibles) == 1:
            return possibles[0]
        else:
            return self.travel_source_choose_based_on_priority(possibles, i, destinations)

    def travel_source_box_three(self, i, destinations, sources, is_radicalization=False):
        possibles = []
        for country in self.map.country_names():
            if self.is_adjacent(destinations[i], country):
                adjacent = self.map.get(country)
                num_times_is_source = sources.count(adjacent.name)
                if (adjacent.sleeperCells + adjacent.activeCells - num_times_is_source) > 0:
                    if is_radicalization or "Biometrics" not in self.lapsing or\
                            self.is_adjacent(country, destinations[i]):
                        possibles.append(adjacent.name)
        if not possibles:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travel_source_choose_based_on_priority(possibles, i, destinations)

    def travel_source_box_four(self, i, destinations, sources, is_radicalization=False):
        possibles = []
        for country in self.map.country_names():
            num_times_is_source = sources.count(country)
            if ((self.map.get(country).sleeperCells + self.map.get(country).activeCells) - num_times_is_source) > 0:
                if is_radicalization or "Biometrics" not in self.lapsing or self.is_adjacent(country, destinations[i]):
                    possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travel_source_choose_based_on_priority(possibles, i, destinations)

    def travel_sources(self, destinations, ops, is_radicalization=False):
        sources = []
        for i in range(len(destinations)):
            source = self.travel_source_box_one(i, destinations, sources, ops, is_radicalization)
            if source:
                sources.append(source)
            else:
                source = self.travel_source_box_two(i, destinations, sources, is_radicalization)
                if source:
                    sources.append(source)
                else:
                    source = self.travel_source_box_three(i, destinations, sources, is_radicalization)
                    if source:
                        sources.append(source)
                    else:
                        source = self.travel_source_box_four(i, destinations, sources, is_radicalization)
                        if source:
                            sources.append(source)
        return sources

    def test_country(self, country_name):
        # Tests the named country, if untested
        country = self.map.get(country_name)
        test_roll = self.roll_d6()
        country.test(test_roll)

    def get_countries_with_us_posture_by_governance(self):
        """Returns a dict of governance -> names of countries with US posture and that governance"""
        countries_by_governance = {GOOD: [], FAIR: [], POOR: []}
        for country in self.get_countries():
            if country.name != "United States" and country.get_posture() == self.us_posture():
                if country.is_good():
                    countries_by_governance[GOOD].append(country.name)
                elif country.is_fair():
                    countries_by_governance[FAIR].append(country.name)
                elif country.is_poor():
                    countries_by_governance[POOR].append(country.name)
        return countries_by_governance

    def get_countries_with_troops_by_governance(self):
        """Returns a dict of governance -> names of countries with troops and that governance"""
        countries_by_governance = {GOOD: [], FAIR: [], POOR: []}
        for country in self.get_countries():
            if country.troops() > 0:
                if country.is_good():
                    countries_by_governance[GOOD].append(country.name)
                elif country.is_fair():
                    countries_by_governance[FAIR].append(country.name)
                elif country.is_poor():
                    countries_by_governance[POOR].append(country.name)
        return countries_by_governance

    def get_countries_with_aid_by_governance(self):
        countries_by_governance = {GOOD: [], FAIR: [], POOR: []}
        for country_name in self.map.country_names():
            country = self.map.get(country_name)
            if country.get_aid() > 0:
                if country.is_good():
                    countries_by_governance[GOOD].append(country_name)
                elif country.is_fair():
                    countries_by_governance[FAIR].append(country_name)
                elif country.is_poor():
                    countries_by_governance[POOR].append(country_name)
        return countries_by_governance

    def get_non_muslim_countries_by_governance(self):
        countries_by_governance = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map.country_names():
            if country != "United States" and self.map.get(country).is_non_muslim():
                if self.map.get(country).is_good():
                    countries_by_governance[GOOD].append(country)
                elif self.map.get(country).is_fair():
                    countries_by_governance[FAIR].append(country)
                elif self.map.get(country).is_poor():
                    countries_by_governance[POOR].append(country)
        return countries_by_governance

    def get_muslim_countries_by_governance(self):
        countries_by_governance = {GOOD: [], FAIR: [], POOR: []}
        for country in self.get_countries():
            if not country.is_non_muslim():
                if country.is_good():
                    countries_by_governance[GOOD].append(country.name)
                elif country.is_fair():
                    countries_by_governance[FAIR].append(country.name)
                elif country.is_poor():
                    countries_by_governance[POOR].append(country.name)
        return countries_by_governance

    def handle_travel(self, ops, is_radicalization=False, is_schengen_visas=False, is_clean_operatives=False):
        destinations = self._get_travel_destinations(is_clean_operatives, is_radicalization, is_schengen_visas, ops)
        sources = self.travel_sources(destinations, ops, is_radicalization)
        if not is_radicalization and not is_schengen_visas and not is_clean_operatives:
            self.output_to_history("* Cells Travel", False)
        for i in range(len(sources)):
            self._travel_one_cell(
                destinations[i], is_clean_operatives, is_radicalization, is_schengen_visas, sources[i])
        return ops - len(sources)

    def _travel_one_cell(self, destination_country_name, is_clean_operatives, is_radicalization, is_schengen_visas,
                         source_country_name):
        """Travels one cell from the named source country to the named destination country"""
        self.output_to_history("->Travel from %s to %s." % (source_country_name, destination_country_name), False)
        success = False
        destination_country = self.get_country(destination_country_name)
        if is_radicalization:
            success = True
            display_str = "Travel by Radicalization is automatically successful."
        elif is_schengen_visas:
            success = True
            display_str = "Travel by Schengen Visas is automatically successful."
        elif is_clean_operatives:
            success = True
            display_str = "Travel by Clean Operatives is automatically successful."
        else:
            if source_country_name == destination_country_name:
                success = True
                display_str = "Travel within country automatically successful."
            else:
                if self.is_adjacent(source_country_name, destination_country_name):
                    if "Biometrics" not in self.lapsing:
                        success = True
                        display_str = "Travel to adjacent country automatically successful."
                    else:
                        roll = random.randint(1, 6)
                        if destination_country.is_non_recruit_success(roll):
                            success = True
                            display_str = "Travel roll needed due to Biometrics - roll successful."
                        else:
                            display_str = \
                                "Travel roll needed due to Biometrics - roll failed, cell to funding track."
                else:
                    roll = random.randint(1, 6)
                    if destination_country.is_non_recruit_success(roll):
                        success = True
                        display_str = "Travel roll successful."
                    else:
                        display_str = "Travel roll failed, cell to funding track."
        self.output_to_history(display_str)
        self.test_country(destination_country_name)
        source_country = self.get_country(source_country_name)
        if success:
            if source_country.activeCells > 0:
                source_country.activeCells -= 1
            else:
                source_country.sleeperCells -= 1
            destination_country.sleeperCells += 1
            self.output_to_history(source_country.summary(), False)
            self.output_to_history(destination_country.summary())
        else:
            if source_country.activeCells > 0:
                source_country.activeCells -= 1
            else:
                source_country.sleeperCells -= 1
            self.cells += 1
            self.output_to_history(source_country.summary())

    def _get_travel_destinations(self, is_clean_operatives, is_radicalization, is_schengen_visas, ops):
        """Returns a list of country names"""
        if is_schengen_visas:
            return self.travel_destinations_schengen_visas()
        elif is_clean_operatives:
            return ["United States", "United States"]
        else:
            return self.travel_destinations(ops, is_radicalization)

    def place_plots(self, country_name, roll_position, plot_rolls, is_martyrdom_operation=False,
                    is_danish_cartoons=False, is_ksm=False):
        if (self.map.get(country_name).total_cells(True)) > 0:
            if is_martyrdom_operation:
                self.remove_cell(country_name, "Jihadist")
                self.output_to_history("Place 2 available plots in %s." % country_name, False)
                self.map.get(country_name).plots += 2
                roll_position = 1
            elif is_danish_cartoons:
                if self.num_islamist_rule() > 0:
                    self.output_to_history("Place any available plot in %s." % country_name, False)
                else:
                    self.output_to_history("Place a Plot 1 in %s." % country_name, False)
                self.map.get(country_name).plots += 1
                roll_position = 1
            elif is_ksm:
                if not self.map.get(country_name).is_islamist_rule():
                    self.output_to_history("Place any available plot in %s." % country_name, False)
                    self.map.get(country_name).plots += 1
                    roll_position = 1
            else:
                ops_remaining = len(plot_rolls) - roll_position
                cells_available = self.map.get(country_name).total_cells(True)
                plots_to_place = min(cells_available, ops_remaining)
                self.output_to_history("--> %s plot attempt(s) in %s." % (plots_to_place, country_name), False)
                successes = 0
                failures = 0
                for i in range(roll_position, roll_position + plots_to_place):
                    if self.map.get(country_name).is_non_recruit_success(plot_rolls[i]):
                        successes += 1
                    else:
                        failures += 1
                self.output_to_history(
                    "Plot rolls: %d Successes rolled, %d Failures rolled" % (successes, failures), False)
                for i in range(plots_to_place - self.map.get(country_name).num_active_cells()):
                    self.output_to_history("Cell goes Active", False)
                    self.map.get(country_name).sleeperCells -= 1
                    self.map.get(country_name).activeCells += 1
                plots_placed = successes * self.ideology.plots_per_success()
                self.map.get(country_name).plots += plots_placed
                self.output_to_history("%d Plot(s) placed in %s." % (plots_placed, country_name), False)
                if "Abu Sayyaf" in self.markers and country_name == "Philippines" and \
                        self.map.get(country_name).troops() <= self.map.get(country_name).total_cells() and\
                        successes > 0:
                    self.output_to_history("Prestige loss due to Abu Sayyaf.", False)
                    self.change_prestige(-successes)
                if "NEST" in self.markers and country_name == "Unites States":
                    self.output_to_history(
                        "NEST in play. If jihadists have WMD, all plots in the US placed face up.", False)
                self.output_to_history(self.map.get(country_name).summary(), True)
                roll_position += plots_to_place
        return roll_position

    def handle_plot_priorities(self, countries_dict, ops, roll_position, plot_rolls, is_ops,
                               is_martyrdom_operation=False, is_danish_cartoons=False, is_ksm=False):
        if is_ops:
            if len(countries_dict[FAIR]) > 0:
                targets = countries_dict[FAIR]
                random.shuffle(targets)
                i = 0
                while roll_position < ops and i < len(targets):
                    roll_position = self.place_plots(
                        targets[i], roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                    i += 1
            if roll_position == ops:
                return roll_position
            if len(countries_dict[GOOD]) > 0:
                targets = countries_dict[GOOD]
                random.shuffle(targets)
                i = 0
                while roll_position < ops and i < len(targets):
                    roll_position = self.place_plots(
                        targets[i], roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                    i += 1
            if roll_position == ops:
                return roll_position
        else:
            if len(countries_dict[GOOD]) > 0:
                targets = countries_dict[GOOD]
                random.shuffle(targets)
                i = 0
                while roll_position < ops and i < len(targets):
                    roll_position = self.place_plots(
                        targets[i], roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                    i += 1
            if roll_position == ops:
                return roll_position
            if len(countries_dict[FAIR]) > 0:
                targets = countries_dict[FAIR]
                random.shuffle(targets)
                i = 0
                while roll_position < ops and i < len(targets):
                    roll_position = self.place_plots(
                        targets[i], roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                    i += 1
            if roll_position == ops:
                return roll_position
        if len(countries_dict[POOR]) > 0:
            targets = countries_dict[POOR]
            random.shuffle(targets)
            i = 0
            while roll_position < ops and i < len(targets):
                roll_position = self.place_plots(
                    targets[i], roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                i += 1
        return roll_position

    def execute_plot(self, ops, is_ops, plot_rolls, is_martyrdom_operation=False, is_danish_cartoons=False,
                     is_ksm=False):
        if not is_martyrdom_operation and not is_danish_cartoons and not is_ksm:
            self.output_to_history("* Jihadists attempting to Plot...", False)
        # In US
        self.debug_print("DEBUG: In US")
        roll_position = self.place_plots(
            "United States", 0, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
        if roll_position == ops:
            return 0
        if self.prestige >= 4:
            # Prestige high
            self.debug_print("DEBUG: Prestige high")
            if "Abu Sayyaf" in self.markers and \
                    (self.map.get("Philippines").total_cells(True)) >= self.map.get("Philippines").troops():
                # In Philippines
                self.debug_print("DEBUG: Philippines")
                roll_position = self.place_plots(
                    "Philippines", roll_position, plot_rolls, is_martyrdom_operation, is_danish_cartoons, is_ksm)
                if roll_position == ops:
                    return 0
            # With troops
            self.debug_print("DEBUG: troops")
            troop_dict = self.get_countries_with_troops_by_governance()
            roll_position = self.handle_plot_priorities(
                troop_dict, ops, roll_position, plot_rolls, is_ops, is_martyrdom_operation, is_danish_cartoons, is_ksm)
            if roll_position == ops:
                return 0
        # No GWOT Penalty
        if not self.gwot_penalty():
            self.debug_print("DEBUG: No GWOT Penalty")
            posture_dict = self.get_countries_with_us_posture_by_governance()
            roll_position = self.handle_plot_priorities(posture_dict, ops, roll_position, plot_rolls, is_ops,
                                                        is_martyrdom_operation, is_danish_cartoons, is_ksm)
            if roll_position == ops:
                return 0
        # With aid
        self.debug_print("DEBUG: aid")
        aid_dict = self.get_countries_with_aid_by_governance()
        roll_position = self.handle_plot_priorities(
            aid_dict, ops, roll_position, plot_rolls, is_ops, is_martyrdom_operation, is_danish_cartoons, is_ksm)
        if roll_position == ops:
            return 0
        # Funding < 9
        if self.funding < 9:
            self.debug_print("DEBUG: Funding < 9")
            non_muslim_dict = self.get_non_muslim_countries_by_governance()
            roll_position = self.handle_plot_priorities(non_muslim_dict, ops, roll_position, plot_rolls, is_ops,
                                                        is_martyrdom_operation, is_danish_cartoons, is_ksm)
            if roll_position == ops:
                return 0
            muslim_dict = self.get_muslim_countries_by_governance()
            roll_position = self.handle_plot_priorities(muslim_dict, ops, roll_position, plot_rolls, is_ops,
                                                        is_martyrdom_operation, is_danish_cartoons, is_ksm)
            if roll_position == ops:
                return 0
        return len(plot_rolls) - roll_position

    def place_cell(self, country_name):
        """Places a cell from the funding track into the given country"""
        country = self.map.get(country_name)
        country.sleeperCells += 1
        self.cells -= 1
        self.test_country(country_name)
        self.output_to_history("--> Sleeper Cell placed in %s." % country_name)
        if country.has_cadre():
            country.cadre = 0
            self.output_to_history("--> Cadre removed from %s." % country_name)
        self.output_to_history(self.map.get(country_name).summary(), True)

    def resolve_plot(self, country, plot_type, posture_roll, us_prestige_rolls, schengen_countries,
                     schengen_posture_rolls, governance_olls, is_backlash=False):
        self.output_to_history("--> Resolve \"%s\" plot in %s" % (str(plot_type), country), False)
        if country == "United States":
            self._resolve_plot_in_us(plot_type, posture_roll, us_prestige_rolls)
        elif self.map.get(country).is_non_muslim():
            self._resolve_plot_in_non_muslim_country(
                country, plot_type, posture_roll, schengen_countries, schengen_posture_rolls)
        else:  # e.g. Iran
            self._resolve_plot_in_muslim_country(country, governance_olls, is_backlash, plot_type)
        self.map.get(country).remove_plot_marker()

    def _resolve_plot_in_non_muslim_country(
            self, country_name, plot_type, posture_roll, schengen_countries, schengen_posture_rolls):
        if country_name == "Israel" and "Abbas" in self.markers:
            self.markers.remove("Abbas")
            self.output_to_history("Abbas no longer in play.", True)
        if country_name == "India" and "Indo-Pakistani Talks" in self.markers:
            self.markers.remove("Indo-Pakistani Talks")
            self.output_to_history("Indo-Pakistani Talks no longer in play.", True)
        target_country = self.map.get(country_name)
        if plot_type == "WMD":
            self.funding = 9
        else:
            if target_country.is_good():
                self.change_funding(plot_type * 2)
            else:
                self.change_funding(plot_type)
        self.output_to_history("Jihadist Funding now %d" % self.funding, False)
        if target_country.name != "Israel":
            if posture_roll <= 4:
                target_country.make_soft()
            else:
                target_country.make_hard()
            self.output_to_history("%s Posture now %s" % (country_name, target_country.get_posture()), True)
        if target_country.troops() > 0:
            if plot_type == "WMD":
                self.prestige = 1
            else:
                self._reduce_prestige(1)
            self.output_to_history("Troops present so US Prestige now %d" % self.prestige, False)
        if target_country.schengen:
            for i in range(len(schengen_countries)):
                schengen_country = self.get_country(schengen_countries[i])
                if schengen_posture_rolls[i] <= 4:
                    schengen_country.make_soft()
                else:
                    schengen_country.make_hard()
                self.output_to_history(
                    "%s Posture now %s" % (schengen_countries[i], schengen_country.get_posture()), False)
        self.output_to_history("", False)

    def _resolve_plot_in_muslim_country(self, country_name, governance_rolls, is_backlash, plot_type):
        country = self.map.get(country_name)
        if is_backlash:
            if plot_type == "WMD":
                self.funding = 1
            else:
                self.funding -= 1
                if country.is_good():
                    self.funding -= 1
                if self.funding < 1:
                    self.funding = 1
            self.output_to_history("BACKLASH: Jihadist Funding reduced to %d" % self.funding, False)
        elif self.funding < 9:
            if country.is_good():
                self.change_funding(2)
            else:
                self.change_funding(1)
            self.output_to_history("Jihadist Funding raised to %d" % self.funding, False)
        if country.troops() > 0 and self.prestige > 1:
            if plot_type == "WMD":
                self.prestige = 1
            else:
                self._reduce_prestige(1)
            self.output_to_history("Troops present so US Prestige reduced to %d" % self.prestige, False)
        if country.name != "Iran" and (country.governance_is_better_than(POOR) or country.get_aid() > 0):
            successes = 0
            failures = 0
            for roll in governance_rolls:
                if country.is_non_recruit_success(roll):
                    successes += 1
                else:
                    failures += 1
            self.output_to_history("Governance rolls: %d Successes rolled, %d Failures rolled" % (successes, failures),
                                   False)
            if country.get_aid() > 0 and successes > 0:
                country.reduce_aid_by(successes)
                self.output_to_history("Aid removed, now %d." % country.get_aid(), False)
            if country.is_poor() and successes > 0:
                self.output_to_history("Governance stays at %s" % country.governance_str(), True)
            while successes > 0 and country.governance_is_better_than(POOR):
                self.worsen_governance(country_name)
                successes -= 1
                self.output_to_history("Governance to %s" % country.governance_str(), True)

    def _resolve_plot_in_us(self, plot_type, posture_roll, us_prestige_rolls):
        if plot_type == "WMD":
            self.gameOver = True
            self.output_to_history("== GAME OVER - JIHADIST AUTOMATIC VICTORY ==", True)
        else:
            self.funding = 9
            self.output_to_history("Jihadist Funding now 9", False)
            prestige_multiplier = 1
            if us_prestige_rolls[0] <= 4:
                prestige_multiplier = -1
            self.change_prestige(min(us_prestige_rolls[1], us_prestige_rolls[2]) * prestige_multiplier)
            self.output_to_history("US Prestige now %d" % self.prestige, False)
            if posture_roll <= 4:
                self.us().make_soft()
            else:
                self.us().make_hard()
            self.output_to_history("US Posture now %s" % self.us_posture(), True)

    def playable_non_us_event(self, card_number):
        card = self.card(card_number)
        return card.is_playable_non_us_event(self)

    def playable_us_event(self, card_number):
        card = self.card(card_number)
        return card.is_playable_us_event(self)

    def execute_non_muslim_woi(self, country, posture_roll):
        if posture_roll > 4:
            self.map.get(country).make_hard()
            self.output_to_history("* War of Ideas in %s - Posture Hard" % country, False)
            if self.us().is_hard():
                self.change_prestige(1)
        else:
            self.map.get(country).make_soft()
            self.output_to_history("* War of Ideas in %s - Posture Soft" % country, False)
            if self.us().is_soft():
                self.change_prestige(1)

    def roll_d6(self):
        """Rolls a d6 and returns the result"""
        return self.randomizer.roll_d6(1)[0]

    def list_countries_in_param(self, needed=None):
        print ""
        print "Countries"
        print "---------"
        for country in needed:
            self.map.get(country).print_country()
        print ""

    def list_countries_with_troops(self, needed=None):
        print ""
        print "Countries with Troops"
        print "---------------------"
        if needed is None:
            needed = 0
        if self.troops > needed:
            print "Troop Track: %d" % self.troops
        for country in self.get_countries():
            if country.troops() > needed:
                print "%s: %d" % (country.name, country.troops())
        print ""

    def _can_deploy_to(self, country_name):
        """Indicates whether the US player can peacefully deploy troops to the named country"""
        return self.map.get(country_name).is_ally() or ("Abu Sayyaf" in self.markers and country_name == "Philippines")

    def list_deploy_options(self, _=None):
        print ""
        print "Deploy Options"
        print "--------------"
        for country in self.map.country_names():
            if self._can_deploy_to(country):
                print "%s: %d troops" % (country, self.map.get(country).troops())
        print ""

    def list_disruptable_countries(self, _=None):
        print ""
        print "Disruptable Countries"
        print "---------------------"
        for country in self.get_countries():
            if country.can_disrupt():
                print country.get_disrupt_summary()
        print ""

    def list_woi_countries(self, _=None):
        print ""
        print "War of Ideas Eligible Countries"
        print "-------------------------------"
        for country in self.get_countries():
            if country.is_ally() or country.is_neutral() or country.is_ungoverned():
                print "%s, %s %s - %d Active Cells, %d Sleeper Cells, %d Cadre, %d troops" %\
                      (country.name, country.governance_str(), country.alignment(), country.activeCells,
                       country.sleeperCells, country.cadre, country.troops())
        for country in self.get_countries():
            if country.is_non_muslim() and country.name != "United States" and country.is_hard():
                print "%s, Posture %s" % (country.name, country.get_posture())
        for country in self.get_countries():
            if country.is_non_muslim() and country.name != "United States" and country.is_soft():
                print "%s, Posture %s" % (country.name, country.get_posture())
        for country in self.get_countries():
            if country.is_non_muslim() and country.name != "United States" and not country.get_posture():
                print "%s, Untested" % country.name

    def list_plot_countries(self, _=None):
        print ""
        print "Countries with Active Plots"
        print "---------------------------"
        for country in self.map.country_names():
            if self.map.get(country).plots > 0:
                self.map.get(country).print_country()
        print ""

    def list_islamist_countries(self, _=None):
        print ""
        print "Islamist Rule Countries"
        print "-----------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_islamist_rule():
                self.map.get(country).print_country()
        print ""

    def list_regime_change_countries(self, _=None):
        print ""
        print "Regime Change Countries"
        print "-----------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_regime_change():
                self.map.get(country).print_country()
        print ""

    def list_regime_change_with_two_cells(self, _=None):
        print ""
        print "Regime Change Countries with Two Cells"
        print "--------------------------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_regime_change():
                if self.map.get(country).total_cells() >= 2:
                    self.map.get(country).print_country()
        print ""

    def list_countries_with_cell_and_adjacent_troops(self, _=None):
        print ""
        print "Countries with Cells and with Troops or adjacent to Troops"
        print "----------------------------------------------------------"
        for country in self.map.country_names():
            if self.map.get(country).total_cells(True) > 0:
                if self.map.get(country).troops() > 0:
                    self.map.get(country).print_country()
                else:
                    for subCountry in self.map.country_names():
                        if subCountry != country:
                            if self.map.get(subCountry).troops() > 0 and self.is_adjacent(country, subCountry):
                                self.map.get(country).print_country()
                                break
        print ""

    def list_adversary_countries(self, _=None):
        print ""
        print "Adversary Countries"
        print "-------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_adversary():
                self.map.get(country).print_country()
        print ""

    def list_good_ally_plot_countries(self, _=None):
        print ""
        print "Ally or Good Countries with Plots"
        print "---------------------------------"
        for country in self.map.country_names():
            if self.map.get(country).plots > 0:
                if self.map.get(country).is_ally() or self.map.get(country).is_good():
                    self.map.get(country).print_country()
        print ""

    def list_muslim_countries_with_cells(self, _=None):
        print ""
        print "Muslim Countries with Cells"
        print "---------------------------"
        for country in self.get_countries():
            if country.total_cells(True) > 0 and country.is_muslim():
                country.print_country()
        print ""

    def list_besieged_countries(self, _=None):
        print ""
        print "Besieged Regimes"
        print "----------------"
        for country in self.get_countries():
            if country.is_besieged():
                country.print_country()
        print ""

    def list_shia_mix_regime_change_countries_with_cells(self, _=None):
        print ""
        print "Shia-Mix Regime Change Countries with Cells"
        print "-------------------------------------------"
        for country in self.get_countries():
            if country.is_shia_mix() and country.is_regime_change() and country.total_cells(True) > 0:
                country.print_country()
        print ""

    def list_shia_mix_countries(self, _=None):
        print ""
        print "Shia-Mix Countries"
        print "------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_shia_mix():
                self.map.get(country).print_country()
        print ""

    def list_shia_mix_countries_with_cells_troops(self, _=None):
        print ""
        print "Shia-Mix Countries with Cells and Troops"
        print "----------------------------------------"
        for country in self.map.country_names():
            if self.map.get(country).is_shia_mix():
                if self.map.get(country).troops() > 0 and self.map.get(country).total_cells() > 0:
                    self.map.get(country).print_country()
        print ""

    def list_schengen_countries(self, _=None):
        print ""
        print "Schengen Countries"
        print "------------------"
        for country in self.map.country_names():
            if self.map.get(country).schengen > 0:
                self.map.get(country).print_country()
        print ""

    def list_hambali(self, _=None):
        print ""
        print "Indonesia or adjacent country with cell and Ally or Hard"
        print "--------------------------------------------------------"
        possibles = ["Indonesia/Malaysia"]
        for countryObj in self.get_country("Indonesia/Malaysia").links:
            possibles.append(countryObj.name)
        for country in possibles:
            if self.map.get(country).total_cells(True) > 0:
                if self.map.get(country).is_non_muslim():
                    if self.map.get(country).is_hard():
                        self.map.get(country).print_country()
                else:
                    if self.map.get(country).is_ally():
                        self.map.get(country).print_country()

    def deploy_reserves(self):
        """Allows the US player to add the last played card's ops to the US Reserves track (6.3.3)."""
        if self.__us_reserves_card:
            self.us_reserves = min(self.us_reserves + self.__us_reserves_card.ops, 2)
            print "US reserves now %d; discard the '%s' card" % (self.us_reserves, self.__us_reserves_card.name)
            self.__us_reserves_card = None
        else:
            print "No US card was chosen; use the 'us_card' command"

    def show_status(self, country_name=None):
        """Shows the status of the given country, if any, otherwise the whole game."""
        if country_name:
            return self._show_country_status(country_name)
        good_resources = self.map.get_good_resources()
        islamist_resources = self.map.get_islamist_rule_resources()
        good_or_fair_countries = self._count_good_or_fair_muslim_countries()
        poor_or_islamist_countries = self._count_poor_or_islamist_rule_countries()
        print ""
        print "GOOD GOVERNANCE"
        any_good = False
        for country in self.get_countries():
            if not country.is_non_muslim() and country.is_good():
                any_good = True
                country.print_country()
        if not any_good:
            print "none"
        print ""
        print "FAIR GOVERNANCE"
        any_fair = False
        for country in self.get_countries():
            if country.is_muslim() and country.is_fair():
                any_fair = True
                country.print_country()
        if not any_fair:
            print "none"
        print ""
        print "POOR GOVERNANCE"
        any_poor = False
        for country in self.get_countries():
            if country.is_muslim() and country.is_poor():
                any_poor = True
                country.print_country()
        if not any_poor:
            print "none"
        print ""
        print "ISLAMIST RULE"
        any_islamist = False
        for country in self.get_countries():
            if country.is_islamist_rule():
                any_islamist = True
                country.print_country()
        if not any_islamist:
            print "none"
        print ""

        print "UNTESTED WITH DATA"
        any_untested_with_data = False
        for country in self.get_countries():
            if country.is_ungoverned() and country.has_data():
                any_untested_with_data = True
                country.print_country()
        if not any_untested_with_data:
            print "none"
        print ""

        print "HARD POSTURE"
        hard_countries = self.find_countries(lambda c: c.is_hard())
        for country in hard_countries:
            country.print_country()
        if not hard_countries:
            print "none"
        print ""

        print "SOFT POSTURE"
        soft_countries = self.find_countries(lambda c: c.is_soft())
        for country in soft_countries:
            country.print_country()
        if not soft_countries:
            print "none"
        print ""

        print "PLOTS"
        any_plots = False
        for country in self.get_countries():
            if country.plots > 0:
                any_plots = True
                print "%s: %d plot(s)" % (country.name, country.plots)
        if not any_plots:
            print "No Plots"
        print ""

        print "VICTORY"
        print "Good Resources:     %d" % good_resources
        print "Islamist Resources: %d" % islamist_resources
        print "---"
        print "Fair/Good Countries:     %d" % good_or_fair_countries
        print "Poor/Islamist Countries: %d" % poor_or_islamist_countries
        print ""
        print "GWOT"
        print "US Posture: %s" % self.us_posture()
        print self._get_world_posture_str()
        print "US Prestige: %d" % self.prestige
        print ""
        print "TROOPS"
        if self.troops >= 10:
            print "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            print "War: %d troops available" % self.troops
        else:
            print "Overstretch: %d troops available" % self.troops
        print ""
        print "JIHADIST FUNDING"
        print "Funding: %d" % self.funding
        print "Cells Available: %d" % self.cells
        print ""
        print "EVENTS"
        if len(self.markers) == 0:
            print "Markers: None"
        else:
            print "Markers: %s" % ", ".join(self.markers)
        if len(self.lapsing) == 0:
            print "Lapsing: None"
        else:
            print "Lapsing: %s" % ", ".join(self.lapsing)
        print ""
        print "DATE"
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""

    def _show_country_status(self, country_name):
        """Prints the status of the given country (if it exists)"""
        good_country = None
        possible = []
        for country in self.map.country_names():
            if country_name.lower() == country.lower():
                possible = [country]
                break
            elif country_name.lower() in country.lower():
                possible.append(country)
        if len(possible) == 0:
            print "Unrecognized country."
            print ""
        elif len(possible) > 1:
            print "Be more specific", possible
            print ""
        else:
            good_country = possible[0]
        if good_country:
            self.map.get(good_country).print_country()

    def get_summary(self):
        """Returns a human-readable summary of the game state"""
        good_resources = self.map.get_good_resources()
        islamist_resources = self.map.get_islamist_rule_resources()
        good_or_fair_countries = self._count_good_or_fair_muslim_countries()
        poor_or_islamist_countries = self._count_poor_or_islamist_rule_countries()
        if self.troops >= 10:
            troop_track = "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            troop_track = "War: %d troops available" % self.troops
        else:
            troop_track = "Overstretch: %d troops available" % self.troops
        if self.markers:
            markers = "Markers: %s" % ", ".join(self.markers)
        else:
            markers = "Markers: None"
        if self.lapsing:
            lapsing = "Lapsing: %s" % ", ".join(self.lapsing)
        else:
            lapsing = "Lapsing: None"

        summary = [
            "Jihadist Ideology: %s" % self.ideology,
            "",
            "VICTORY",
            "Good Resources: %d        Islamist Resources: %d" % (good_resources, islamist_resources),
            "Fair/Good Countries: %d   Poor/Islamist Countries: %d" % (
                good_or_fair_countries, poor_or_islamist_countries),
            "",
            "GWOT",
            ("US Posture: %s" % self.us_posture()) + "    " + self._get_world_posture_str(),
            "US Prestige: %d" % self.prestige,
            "",
            "TROOPS",
            troop_track,
            "",
            "JIHADIST FUNDING",
            "Funding: %d    Cells Available: %d" % (self.funding, self.cells),
            "",
            "EVENTS",
            markers,
            lapsing,
            "",
            "US Reserves: %d" % self.us_reserves
        ]
        return summary

    def print_summary(self):
        print ""
        for line in self.get_summary():
            print line
        print ""

    def find_countries(self, predicate):
        """Returns a list of countries matching the given predicate"""
        return self.map.find(predicate)

    def adjust_ideology(self):
        print "Adjusting ideology"
        new_ideology_number = choose_ideology()
        if new_ideology_number:
            self.ideology = get_ideology(new_ideology_number)
        else:
            print "Ideology unchanged"

    def get_adjust_prestige(self):
        """Asks the user for a new prestige value and returns it (or None if the user quitted)"""
        while True:
            prestige_str = self.my_raw_input("Enter new prestige (1-12): ")
            if prestige_str == "":
                return None
            try:
                prestige = int(prestige_str)
                if prestige < 1 or prestige > 12:
                    print "Invalid prestige value -", prestige
                else:
                    return prestige
            except ValueError:
                print "Invalid prestige value -", prestige_str

    def adjust_prestige(self):
        print "Adjusting prestige"
        new_prestige = self.get_adjust_prestige()
        if new_prestige:
            self.change_prestige(new_prestige - self.prestige)
        else:
            print "Prestige unchanged"

    def get_adjust_cells(self):
        """Asks the user for a new cell count on the funding track and returns it (or None if the user quitted)"""
        while True:
            cells_str = self.my_raw_input("Enter new cell count for the funding track (1-15): ")
            if cells_str == "":
                return None
            try:
                cells = int(cells_str)
                if cells < 0 or cells > 15:
                    print "Invalid cell count %d" % cells
                else:
                    return cells
            except ValueError:
                print "Invalid number '%s'" % cells_str

    def get_adjust_funding(self):
        """Asks the user for a new funding level and returns it (or None if the user quitted)"""
        while True:
            funding_str = self.my_raw_input("Enter new funding (1-9): ")
            if funding_str == "":
                return None
            try:
                funding = int(funding_str)
                if funding < 1 or funding > 9:
                    print "Invalid funding value -", funding
                else:
                    return funding
            except ValueError:
                print "Invalid funding value -", funding_str

    def adjust_cells(self):
        print "Adjusting cells"
        new_cell_count = self.get_adjust_cells()
        if new_cell_count:
            self.cells = new_cell_count
        else:
            print "Cells unchanged"

    def adjust_funding(self):
        print "Adjusting funding"
        new_funding_level = self.get_adjust_funding()
        if new_funding_level:
            self.change_funding(new_funding_level - self.funding)
        else:
            print "Funding unchanged"

    def adjust_lapsing(self):
        print "Adjusting lapsing event"
        if len(self.lapsing) == 0:
            print "There are no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""
        print "Available lapsing events are:"
        for validEvent in self.validLapsingMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it:"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.lapsing:
                self.lapsing.remove(event)
                print "Removed lapsing event -", event
                break
            elif event in self.validLapsingMarkers:
                self.lapsing.append(event)
                print "Added lapsing event -", event
                break
            else:
                print "Not a valid event"
        if len(self.lapsing) == 0:
            print "There are now no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""

    def adjust_marker(self):
        print "Adjusting event markers in play"
        if len(self.markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""
        print "Available global events are:"
        for validEvent in self.validGlobalMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.markers:
                self.markers.remove(event)
                print "Removed event -", event
                break
            elif event in self.validGlobalMarkers:
                self.markers.append(event)
                print "Added event -", event
                break
            else:
                print "Not a valid event"
        if len(self.markers) == 0:
            print "There are now no events in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""

    def adjust_country_governance(self, country_name):
        print "Adjusting governance for -", country_name
        while True:
            gov_str = self.my_raw_input("Enter governance (0-4) (0 = untested): ")
            if gov_str == "":
                return False
            try:
                gov_num = int(gov_str)
                new_governance = governance_with_level(gov_num)
                print "Changing governance to %s" % new_governance
                country = self.map.get(country_name)
                if new_governance:
                    country.test(self.roll_d6())
                    country.set_governance(new_governance)
                else:
                    country.untest()
                return True
            except ValueError:
                print "Invalid governance value '%s'" % gov_str

    def adjust_country_alignment(self, country_name):
        print "Adjusting alignment for -", country_name
        while True:
            alignment = self.my_raw_input("Enter alignment ('Ally', 'Neutral', 'Adversary'): ")
            if alignment == "":
                return False
            if alignment == "Adversary":
                print "Changing alignment to Adversary"
                self.map.get(country_name).make_adversary()
                return True
            if alignment == "Ally":
                print "Changing alignment to Ally"
                self.map.get(country_name).make_ally()
                return True
            if alignment == "Neutral":
                print "Changing alignment to Neutral"
                self.map.get(country_name).make_neutral()
                return True
            print "Invalid alignment value -", alignment

    def adjust_country_posture(self, country_name):
        """Prompts the user to set the posture of the named country (returns true if successful)"""
        print "Adjusting posture for -", country_name
        while True:
            posture_str = self.my_raw_input("Enter posture ('Hard', 'Soft', 'Untested'): ")
            if posture_str == "":  # User aborted
                return False
            country = self.get_country(country_name)
            assert country, "No such country '%s'" % country_name
            if posture_str.lower() == "hard":
                print "Changing posture to Hard"
                country.make_hard()
                return True
            if posture_str.lower() == "soft":
                print "Changing posture to Soft"
                country.make_soft()
                return True
            if posture_str.lower() == "untested":
                print "Changing posture to Untested"
                country.remove_posture()
                return True
            print "Invalid posture value '%s'" % posture_str
            return False

    def adjust_country_troops(self, country_name):
        print "Adjusting troops for - ", country_name
        country = self.map.get(country_name)
        if 'NATO' in country.markers:
            print "NATO contributes 2 troops to count, actual troop cubes are %d" % country.troopCubes
        while True:
            troop_str = self.my_raw_input("Enter new troop count (0-15, or <Enter> to abort): ")
            if troop_str == "":
                return False
            try:
                new_country_troops = int(troop_str)
                if new_country_troops < 0 or new_country_troops > 15:
                    print "Invalid troop cube count %d" % new_country_troops
                else:
                    troop_change = new_country_troops - country.troopCubes
                    if troop_change > self.troops:
                        # Trying to add more than are on troop track
                        print "There are not %d more troops on the troop track." % troop_change
                    else:
                        print "Changing troop cubes in %s to %d" % (country_name, new_country_troops)
                        self.troops -= troop_change
                        country.troopCubes = new_country_troops
                        print "Troop track now has %d cubes" % self.troops
                        return True
            except ValueError:
                print "Invalid troop cube value -", troop_str

    def adjust_country_active(self, country_name):
        print "Adjusting active cells for - ", country_name
        while True:
            cell_str = self.my_raw_input("Enter new active cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid active cell value -", cells
                else:
                    print "Changing active cells to ", cells
                    active_change = cells - self.map.get(country_name).activeCells
                    self.cells -= active_change
                    self.map.get(country_name).activeCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid active cell value -", cell_str

    def adjust_country_sleeper(self, country_name):
        country = self.map.get(country_name)
        if country.is_untested():
            print "Cannot adjust sleeper cells in an untested country; set governance or posture first."
            return
        print "Adjusting sleeper cells in %s" % country.name
        while True:
            cell_str = self.my_raw_input("Enter new sleeper cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid sleeper cell value -", cells
                else:
                    print "Changing sleeper cells to", cells
                    sleeper_change = cells - country.sleeperCells
                    self.cells -= sleeper_change
                    country.sleeperCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid sleeper cell value -", cell_str

    def adjust_country_cadre(self, country_name):
        print "Adjusting cadre for - ", country_name
        while True:
            cadre_str = self.my_raw_input("Enter new cadre count (0-1): ")
            if cadre_str == "":
                return False
            try:
                cadres = int(cadre_str)
                if cadres < 0 or cadres > 1:
                    print "Invalid cadre value -", cadres
                else:
                    print "Changing cadre count to", cadres
                    self.map.get(country_name).cadre = cadres
                    return True
            except ValueError:
                print "Invalid cadre value -", cadre_str

    def adjust_country_aid(self, country_name):
        print "Adjusting aid for - ", country_name
        while True:
            aid_str = self.my_raw_input("Enter new aid count (0-9): ")
            if aid_str == "":
                return False
            try:
                aid = int(aid_str)
                if aid < 0 or aid > 9:
                    print "Invalid aid value -", aid
                else:
                    print "Changing aid count to", aid
                    self.map.get(country_name).set_aid(aid)
                    return True
            except ValueError:
                print "Invalid aid value -", aid_str

    def adjust_country_besieged(self, country_name):
        """Changes whether the given country is a besieged regime"""
        print "Adjusting besieged for %s" % country_name
        country = self.get_country(country_name)
        if country.is_besieged():
            country.remove_besieged()
            print "%s is no longer a besieged regime" % country_name
        else:
            country.make_besieged()
            print "%s is now a besieged regime" % country_name
        return True

    def adjust_country_regime(self, country_name):
        print "Adjusting regime change for - ", country_name
        country = self.get_country(country_name)
        if country.is_regime_change():
            country.remove_regime_change()
            print "%s is no longer a Regime Change country" % country_name
        else:
            country.make_regime_change()
            print "%s is now a Regime Change country" % country_name
        return True

    def adjust_country_plots(self, country_name):
        country = self.map.get(country_name)
        if country.is_untested():
            print "%s is untested; set its governance or posture first." % country_name
            return False
        while True:
            plots_str = self.my_raw_input("Enter new plot count (0-12, or Enter to abort): ")
            if plots_str == "":
                return False
            try:
                plots = int(plots_str)
                if plots < 0 or plots > 12:
                    print "Invalid plot value - ", plots
                else:
                    country.plots = plots
                    print "Plot count is now %d" % plots
                    return True
            except ValueError:
                print "Invalid plot value - ", plots_str

    def adjust_country_marker(self, country_name):
        print "Adjusting event markers for - ", country_name
        if len(self.map.get(country_name).markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current markers in play: %s" % ", ".join(self.map.get(country_name).markers)
        print ""
        print "Available country events are:"
        for validEvent in self.validCountryMarkers:
            print validEvent
        print "Enter a new marker to add it to the list, or enter an existing marker to remove it"
        while True:
            marker = self.my_raw_input("Enter marker to be added or removed: ")
            if marker == "":
                return ""
            if marker in self.map.get(country_name).markers:
                self.map.get(country_name).markers.remove(marker)
                print "Removed marker - ", marker
                break
            elif marker in self.validCountryMarkers:
                self.map.get(country_name).markers.append(marker)
                print "Added marker - ", marker
                break
            else:
                print "'%s' is not a valid marker" % marker
        if self.map.get(country_name).markers:
            print "Current events in play: %s" % ", ".join(self.map.get(country_name).markers)
        else:
            print "There are now no events in play"
        print ""
        return True

    def adjust_country(self, country_name, attribute):
        """Adjusts the given attribute of the given country"""
        assert country_name
        assert attribute
        country = self.map.get(country_name)
        print "Adjusting the %s of %s" % (attribute, country.name)
        country.print_country()
        attributes = country.get_adjustable_attributes()
        if attribute not in attributes:
            print "Invalid country attribute '%s'" % attribute
            return
        adjust_success = False
        if attribute == "governance":
            adjust_success = self.adjust_country_governance(country.name)
        elif attribute == "alignment":
            adjust_success = self.adjust_country_alignment(country.name)
        elif attribute == "posture":
            adjust_success = self.adjust_country_posture(country.name)
        elif attribute == "troops":
            adjust_success = self.adjust_country_troops(country.name)
        elif attribute == "active":
            adjust_success = self.adjust_country_active(country.name)
        elif attribute == "sleeper":
            adjust_success = self.adjust_country_sleeper(country.name)
        elif attribute == "cadre":
            adjust_success = self.adjust_country_cadre(country.name)
        elif attribute == "aid":
            adjust_success = self.adjust_country_aid(country.name)
        elif attribute == "besieged":
            adjust_success = self.adjust_country_besieged(country.name)
        elif attribute == "regime":
            adjust_success = self.adjust_country_regime(country.name)
        elif attribute == "plots":
            adjust_success = self.adjust_country_plots(country.name)
        elif attribute == "marker":
            adjust_success = self.adjust_country_marker(country.name)
        if adjust_success:
            country.print_country()
        else:
            print "%s is unchanged" % country.name

    def adjust_game_attribute(self, attribute):
        print "Warning: your changes will not be checked for correctness!"
        print "Start adjusting"
        if attribute == "cells":
            self.adjust_cells()
        elif attribute == "funding":
            self.adjust_funding()
        elif attribute == "ideology":
            self.adjust_ideology()
        elif attribute == "lapsing":
            self.adjust_lapsing()
        elif attribute == "marker":
            self.adjust_marker()
        elif attribute == "prestige":
            self.adjust_prestige()
        else:
            print "Invalid attribute '%s'" % attribute
        print ""

    def show_history(self, argument):
        if argument == 'save':
            with open('history.txt', 'w') as history_file:
                for event in self.history:
                    history_file.write(event + "\r\n")
        for event in self.history:
            print event
        print ""

    def deploy_troops(self):
        """Deploys troops to a Muslim Ally or the track; does not perform Regime Change"""
        if not self.find_countries(lambda c: self._can_deploy_to(c.name)):
            print "There are no Muslim Allies to deploy to."
            return
        move_from = self._get_deploy_source()
        if not move_from:
            return
        move_to = self._get_deploy_destination(move_from)
        if not move_to:
            return
        how_many = self._get_deploy_size(move_from)
        if not how_many:
            return
        self._do_deploy(how_many, move_from, move_to)

    def _get_deploy_source(self):
        """Prompts the user for the location from which troops are deploying;
        returns "track", a country name, or None if they abort """
        while True:
            user_input = self.get_country_from_user("From what country (track for Troop Track) (? for list)?: ",
                                                    "track", self.list_countries_with_troops)
            if user_input == "":
                print ""
                return None
            elif user_input == "track":
                if self.troops <= 0:
                    print "There are no troops on the Troop Track."
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    return "track"
            else:
                country = self.get_country(user_input)
                if country.troops() <= 0:
                    print "There are no troops in %s." % country.name
                else:
                    print "Deploy from %s: %d available" % (country.name, country.troops())
                    print ""
                    return country.name
            print ""

    def _get_deploy_destination(self, move_from):
        """Returns the location to which to deploy, or None if the user aborts"""
        user_input = self.get_country_from_user(
            "To what country ('track' for Troop Track, ? for list): ", "track", self.list_deploy_options)
        if user_input == "":
            print ""
            return None
        if user_input == "track":
            print "Deploying troops from %s to Troop Track" % move_from
            print ""
            return user_input
        print "Deploying troops from %s to %s" % (move_from, user_input)
        print ""
        return user_input

    def _get_deploy_size(self, move_from):
        """Prompts the user for the number of troops to deploy from the named location (country or track);
        returns None if the user aborts"""
        available = self.troops if move_from == "track" else self.get_country(move_from).troops()
        return self.get_num_troops_from_user("Deploy how many troops (%d available)? " % available, available)

    def _do_deploy(self, how_many, move_from, move_to):
        """Deploys the given number of troops from the first named country to the second named country"""
        if move_from == "track":
            self.troops -= how_many
            troops_left = self.troops
        else:
            if self.map.get(move_from).is_regime_change():
                if (self.map.get(move_from).troops() - how_many) < (5 + self.map.get(move_from).total_cells(True)):
                    print "You cannot move that many troops from a Regime Change country."
                    print ""
                    return
            self.map.get(move_from).change_troops(how_many * -1)
            troops_left = self.map.get(move_from).troops()
        if move_to == "track":
            self.troops += how_many
            troops_now = self.troops
        else:
            self.map.get(move_to).change_troops(how_many)
            troops_now = self.map.get(move_to).troops()
        self.output_to_history(
            "* %d troops deployed from %s (%d) to %s (%d)" % (how_many, move_from, troops_left, move_to, troops_now))

    def disrupt_cells_or_cadre(self):
        """Performs a Disrupt operation for the US player."""
        if self.num_disruptable() == 0:
            print "No countries can be disrupted."
            return
        where = None
        while not where:
            country_name = self.get_country_from_user("Disrupt what country?  (? for list): ", "XXX",
                                                      self.list_disruptable_countries)
            if country_name == "":
                print ""
                return
            else:
                country = self.map.get(country_name)
                if country.sleeperCells + country.activeCells <= 0 and country.cadre <= 0:
                    print "There are no cells or cadre in %s." % country_name
                    print ""
                elif "FATA" in country.markers and not country.is_regime_change():
                    print "No disrupt allowed due to FATA."
                    print ""
                elif country.troops() > 0 or country.is_non_muslim() or country.is_ally():
                    print ""
                    where = country_name
                else:
                    print "You can't disrupt there."
                    print ""
        self.handle_disrupt(where)

    def war_of_ideas(self):
        """Conducts a 'War of Ideas' operation for the US player"""
        where = None
        country_name = None
        while not where:
            country_name = self.get_country_from_user("War of Ideas in what country?  (? for list): ", "XXX",
                                                      self.list_woi_countries)
            if country_name == "":
                print ""
                return
            else:
                country = self.map.get(country_name)
                if country.is_non_muslim() and country_name != "United States":
                    where = country_name
                elif country.is_ally() or country.is_neutral() or country.is_ungoverned():
                    where = country_name
                else:
                    print "Country not eligible for War of Ideas."
                    print ""
        if self.map.get(where).is_non_muslim() and country_name != "United States":  # Non-Muslim
            posture_roll = self.get_roll("posture")
            if posture_roll > 4:
                self.map.get(where).make_hard()
                self.output_to_history("* War of Ideas in %s - Posture Hard" % where)
                if self.us().is_hard():
                    self._increase_prestige(1)
                    self.output_to_history("US Prestige now %d" % self.prestige)
            else:
                self.map.get(where).make_soft()
                self.output_to_history("* War of Ideas in %s - Posture Soft" % where)
                if self.us().is_soft():
                    self._increase_prestige(1)
                    self.output_to_history("US Prestige now %d" % self.prestige)
        else:  # Muslim
            self.test_country(where)
            woi_roll = self.get_roll("WoI")
            modified_roll = self.modified_woi_roll(woi_roll, where)
            self.output_to_history("Modified Roll: %d" % modified_roll)
            self.handle_muslim_woi(modified_roll, where)

    def alert_plot(self, country_name):
        """Alerts one plot in the named country"""
        country = self.get_country(country_name)
        assert country.plots
        if country.remove_plot_marker():
            self.output_to_history("* Alert in %s - %d plot(s) remain." % (country.name, country.plots))

    def change_regime(self):
        if self.us().is_soft():
            print "No Regime Change with US Posture Soft"
            print ""
            return
        where = None
        while not where:
            country_name = self.get_country_from_user(
                "Regime Change in what country?  (? for list): ", "XXX", self.list_islamist_countries)
            if country_name == "":
                print ""
                return
            else:
                iraqi_wmd = country_name == "Iraq" and "Iraqi WMD" in self.markers
                libyan_wmd = country_name == "Libya" and "Libyan WMD" in self.markers
                if self.map.get(country_name).is_islamist_rule() or iraqi_wmd or libyan_wmd:
                    where = country_name
                else:
                    print "Country not Islamist Rule."
                    print ""
        move_from = None
        available = 0
        while not move_from:
            country_name = self.get_country_from_user(
                "Deploy 6+ troops from what country (track for Troop Track) (? for list)?: ",
                "track", self.list_countries_with_troops, 6)
            if country_name == "":
                print ""
                return
            elif country_name == "track":
                if self.troops <= 6:
                    print "There are not enough troops on the Troop Track."
                    print ""
                    return
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    available = self.troops
                    move_from = country_name
            else:
                if self.map.get(country_name).troops() <= 6:
                    print "There are not enough troops in %s." % country_name
                    print ""
                    return
                else:
                    print "Deploy from %s = %d available" % (country_name, self.map.get(country_name).troops())
                    print ""
                    available = self.map.get(country_name).troops()
                    move_from = country_name
        how_many = 0
        while not how_many:
            troops = self.get_num_troops_from_user("Deploy how many troops (%d available)? " % available, available)
            if troops == 0:
                print ""
                return
            elif troops < 6:
                print "At least 6 troops needed for Regime Change"
            else:
                how_many = troops
        governance_roll = self.get_roll("governance")
        pre_first_roll = self.get_roll("first (drop/raise) prestige")
        pre_second_roll = self.get_roll("second (amount) prestige")
        pre_third_roll = self.get_roll("third (amount) prestige")
        self.handle_regime_change(
            where, move_from, how_many, governance_roll, (pre_first_roll, pre_second_roll, pre_third_roll))

    def withdraw_troops(self):
        if self.us().is_hard():
            print "No Withdrawal with US Posture Hard"
            print ""
            return
        move_from = None
        available = 0
        while not move_from:
            country_name = self.get_country_from_user(
                "Withdraw from which country?  (? for list): ", "XXX", self.list_regime_change_countries)
            if country_name == "":
                print ""
                return
            elif self.map.get(country_name).is_regime_change():
                move_from = country_name
                available = self.map.get(country_name).troops()
            else:
                print "Country is not Regime Change."
                print ""
        move_to = None
        while not move_to:
            country_name = self.get_country_from_user(
                "To what country (track for Troop Track)  (? for list)?: ", "track", self.list_deploy_options)
            if country_name == "":
                print ""
                return
            elif country_name == "track":
                print "Withdraw troops from %s to Troop Track" % move_from
                print ""
                move_to = country_name
            else:
                print "Withdraw troops from %s to %s" % (move_from, country_name)
                print ""
                move_to = country_name
        how_many = 0
        while not how_many:
            troops = self.get_num_troops_from_user("Withdraw how many troops (%d available)? " % available, available)
            if troops == "":
                print ""
                return
            else:
                how_many = troops
        pre_first_roll = self.get_roll("first (drop/raise) prestige")
        pre_second_roll = self.get_roll("second (amount) prestige")
        pre_third_roll = self.get_roll("third (amount) prestige")
        self.handle_withdraw(move_from, move_to, how_many, (pre_first_roll, pre_second_roll, pre_third_roll))

    def play_jihadist_card(self, card_number):
        """Plays the given numbered card during the Jihadist action phase"""
        self.output_to_history("", False)
        card = self.card(card_number)
        self.output_to_history("== Jihadist plays %s - %d Ops ==" % (card.name, card.ops))
        self.__ai_player.ai_flow_chart_top(card)

    def play_us_card(self, card_num):
        """Plays the given card as the US when it's the US action phase."""
        self.output_to_history("", False)
        card = self.card(card_num)
        self.__us_reserves_card = card
        self.output_to_history("== US plays %s - %d Ops ==" % (card.name, card.ops))

        if card.playable("US", self, True):
            self.play_playable_event_card_as_us(card)
        else:
            if card.get_type() == "Jihadist" and card.playable("Jihadist", self, True):
                self.output_to_history("Jihadist Event is playable.", False)
                play_event_first = self.get_yes_no_from_user(
                    "Do you want to play the Jihadist event before using the Ops? (y/n): ")
                if play_event_first:
                    card.play_event("Jihadist", self)
                else:
                    print "Use the Ops now, then enter us_card <card #> again, to play the event"
                print self.get_us_prompt_to_spend_ops(card_num)
                return
            # It's unplayable by either side.
            self.output_to_history("Unplayable %s Event" % card.get_type(), False)
            print self.get_us_prompt_to_spend_ops(card_num)

    def play_playable_event_card_as_us(self, card):
        self.output_to_history("Playable %s Event" % card.get_type(), False)
        if card.number == 120:
            prompt = "This event must be played, do you want the Event or Ops to happen first"
        else:
            prompt = "Play card for Event or Ops"
        choice = self.get_event_or_ops_from_user(prompt)
        if choice == "event":
            self.output_to_history("Played for Event.", False)
            card.play_event("US", self)
            if card.number == 120:
                print self.get_us_prompt_to_spend_ops(card.number)
        elif choice == "ops":
            self.output_to_history("Played for Ops.", False)
            if card.number == 120:
                print "When finished with Ops, enter 'us_card 120' again to play the event."
            print self.get_us_prompt_to_spend_ops(card.number)

    def get_us_prompt_to_spend_ops(self, card_number):
        """Prompts the US player to spend the given card's Ops value"""
        ops = min(self.card(card_number).ops + self.us_reserves, 3)
        operation_min_ops = {
            "alert": 3,
            "deploy": 1,
            "disrupt": 1,
            "reassessment": 3,
            "regime_change": 3,
            "reserves": 1,
            "war_of_ideas": 1,
            "withdraw": 3
        }
        valid_commands = [op for op in operation_min_ops if operation_min_ops[op] <= ops]
        available_commands = ", ".join(sorted(valid_commands))
        reserves = " (with reserves)" if self.us_reserves > 0 else ""
        return "%d Ops available%s. Use one of: %s" % (ops, reserves, available_commands)

    def resolve_plots(self):
        """Resolves any active plots at the end of the US action phase."""
        found_plot = False
        for country_name in self.map.country_names():
            while self.map.get(country_name).plots > 0:
                if not found_plot:
                    self.output_to_history("", False)
                    self.output_to_history("[[ Resolving Plots ]]", True)
                found_plot = True
                print ""
                plot_type = self.get_plot_type_from_user("Enter Plot type from %s: " % country_name)
                print ""
                is_backlash = False
                if self.backlashInPlay and not self.map.get(country_name).is_non_muslim():
                    is_backlash = self.get_yes_no_from_user("Was this plot selected with backlash (y/n): ")
                posture_roll = 0
                us_prestige_rolls = []
                schengen_countries = []
                schengen_posture_rolls = []
                gov_rolls = []
                if country_name == "United States":
                    if plot_type != "WMD":
                        posture_roll = random.randint(1, 6)
                        us_prestige_rolls.append(random.randint(1, 6))
                        us_prestige_rolls.append(random.randint(1, 6))
                        us_prestige_rolls.append(random.randint(1, 6))
                elif not self.map.get(country_name).is_non_muslim():
                    if country_name != "Iran":
                        if plot_type == "WMD":
                            num_rolls = 3
                        else:
                            num_rolls = plot_type
                        for _ in range(num_rolls):
                            gov_rolls.append(random.randint(1, 6))
                elif self.map.get(country_name).is_non_muslim():
                    posture_roll = random.randint(1, 6)
                    if self.map.get(country_name).schengen:
                        schengen_choices =\
                            [c.name for c in self.get_countries() if c.name != country_name and c.schengen]
                        schengen_countries.append(random.choice(schengen_choices))
                        schengen_countries.append(schengen_countries[0])
                        while schengen_countries[0] == schengen_countries[1]:
                            schengen_countries[1] = random.choice(schengen_choices)
                        for _ in range(2):
                            schengen_posture_rolls.append(random.randint(1, 6))
                self.resolve_plot(country_name, plot_type, posture_roll, us_prestige_rolls, schengen_countries,
                                  schengen_posture_rolls, gov_rolls, is_backlash)
        if not found_plot:
            self.output_to_history("", False)
            self.output_to_history("[[ No unblocked plots to resolve ]]", True)
        self.backlashInPlay = False

    def us(self):
        """Returns the Country of the USA"""
        return self.map.get("United States")

    def us_posture(self):
        """Returns the US posture ('HARD' or 'SOFT' Posture)"""
        return self.us().get_posture()

    def end_turn(self):
        """Performs end-of-turn activities."""
        self.output_to_history("* End of Turn.", False)
        if "Pirates" in self.markers and\
                (self.map.get("Somalia").is_islamist_rule() or self.map.get("Yemen").is_islamist_rule()):
            self.output_to_history("No funding drop due to Pirates.", False)
        else:
            self.funding -= 1
            if self.funding < 1:
                self.funding = 1
            self.output_to_history("Jihadist Funding now %d" % self.funding, False)
        any_islamist_rule = self.contains_country(lambda c: c.is_islamist_rule())
        if any_islamist_rule:
            self._reduce_prestige(1)
            self.output_to_history("Islamist Rule - US Prestige now %d" % self.prestige, False)
        else:
            self.output_to_history("No Islamist Rule - US Prestige stays at %d" % self.prestige, False)
        world_position = self.map.get_net_hard_countries()
        if (self.us().is_hard() and world_position >= 3) or\
                (self.us().is_soft() and world_position <= -3):
            self._increase_prestige(1)
            self.output_to_history("GWOT World posture is 3 and matches US - US Prestige now %d" % self.prestige, False)
        for event in self.lapsing:
            self.output_to_history("%s has Lapsed." % event, False)
        self.lapsing = []
        good_resources = self.map.get_good_resources()
        islamist_resources = self.map.get_islamist_rule_resources()
        good_or_fair_countries = self._count_good_or_fair_muslim_countries()
        islamist_countries = self._count_poor_or_islamist_rule_countries()
        self.output_to_history("---", False)
        self.output_to_history("Good Resources:     %d" % good_resources, False)
        self.output_to_history("Islamist Resources: %d" % islamist_resources, False)
        self.output_to_history("---", False)
        self.output_to_history("Fair/Good Countries:     %d" % good_or_fair_countries, False)
        self.output_to_history("Poor/Islamist Countries: %d" % islamist_countries, False)
        self.turn += 1
        self.output_to_history("---", False)
        self.output_to_history("", False)
        jihadist_cards = self._get_jihadist_hand_limit()
        us_cards = self._get_us_hand_limit()
        self.output_to_history("Jihadist draws %d cards." % jihadist_cards, False)
        self.output_to_history("US draws %d cards." % us_cards, False)
        self.output_to_history("---", False)
        self.output_to_history("", False)
        self.output_to_history("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), False)
        if self.us_reserves > 0:
            self.us_reserves = 0
            self.output_to_history("US Reserves reset to 0")

    def _get_jihadist_hand_limit(self):
        """Returns the number of cards to deal to the Jihadist player"""
        if self.funding >= 7:
            return 9
        elif self.funding >= 4:
            return 8
        return 7

    def _get_us_hand_limit(self):
        """Returns the number of cards to deal to the US player"""
        if self.troops >= 10:
            return 9
        elif self.troops >= 5:
            return 8
        return 7

    def undo_last_turn(self):
        self.undo = self.get_yes_no_from_user("Undo to last card played? (y/n): ")

    def print_turn_number(self):
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""

    def roll_back(self):
        self.roll_turn = -1
        need_turn = True
        while need_turn:
            try:
                last_turn = self.turn - 1
                turn_str = raw_input("Roll back to which turn? (0 to %d, or Q to cancel): " % last_turn)
                if turn_str.upper() == "Q":
                    print "Rollback cancelled"
                    break
                else:
                    turn_number = int(turn_str)
                    if 0 <= turn_number <= last_turn:
                        self.roll_turn = turn_number
                        need_turn = False
                    else:
                        raise ValueError
            except ValueError:
                print "Entry error"
                print ""
