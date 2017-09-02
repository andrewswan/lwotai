import random

from lwotai.governance import POOR


class AIPlayer(object):
    """The AI that uses the flowchart to play as the Jihadist player"""

    def __init__(self, app):
        self.__app = app

    def ai_flow_chart_top(self, card_number):
        card = self.__app.card(card_number)
        if self.__app.playable_non_us_event(card_number):
            self.__app.output_to_history("Playable Non-US Event.", False)
            if card.puts_cell() and self.__app.cells == 0:
                self.handle_radicalization(card.ops)
            else:
                self._ai_flow_chart_play_event(card_number)
        else:
            if self.__app.playable_us_event(card_number):
                self.__app.output_to_history("Playable US Event.", False)
                unused_ops = self._handle_ai_plot_action(card.ops, True)
                if unused_ops > 0:
                    self.handle_radicalization(unused_ops)
            else:
                self.__app.output_to_history("Unplayable Event. Using Ops for Operations.", False)
                self.ai_flow_chart_major_jihad(card_number)

    def _ai_flow_chart_play_event(self, card_number):  # TODO pass the Card
        card = self.__app.card(card_number)
        card.play_event("Jihadist", self.__app)
        if card.is_unassociated():
            self.__app.output_to_history("Unassociated event now being used for Ops.", False)
            self.ai_flow_chart_major_jihad(card_number)

    def ai_flow_chart_major_jihad(self, card_number):  # TODO pass the Card
        card = self.__app.card(card_number)
        country = self.major_jihad_choice(card.ops)
        if country:
            unused_ops = self.handle_jihad(country, card.ops)
            if unused_ops > 0:
                self.handle_radicalization(unused_ops)
        else:
            country_list = self.__app.minor_jihad_in_good_fair_choice(card.ops)
            if country_list:
                unused_ops = self._handle_minor_jihad(country_list, card.ops)
                if unused_ops > 0:
                    self.handle_radicalization(unused_ops)
            else:
                if self.__app.num_cells_available() > 0:
                    unused_ops = self.__app.handle_recruit(card.ops)
                    if unused_ops > 0:
                        self.handle_radicalization(unused_ops)
                else:
                    unused_ops = self.__app.handle_travel(card.ops)
                    if unused_ops > 0:
                        self.handle_radicalization(unused_ops)

    def execute_jihad(self, country_name, roll_list):
        successes = 0
        failures = 0
        target_country = self.__app.map.get(country_name)
        original_besieged = target_country.is_besieged()
        for roll in roll_list:
            if target_country.is_non_recruit_success(roll):
                successes += 1
            else:
                failures += 1
        aid_removed = target_country.reduce_aid_by(successes)
        self.__app.output_to_history("Jihad operation. %d Successes rolled, %d Failures rolled, %d Aid removed." %
                                     (successes, failures, aid_removed), False)
        is_major_jihad = country_name in self.__app.major_jihad_possible(len(roll_list))
        if is_major_jihad:  # all cells go active
            self.__app.output_to_history("* Major Jihad attempt in %s" % country_name, False)
            sleepers = target_country.sleeperCells
            target_country.sleeperCells = 0
            target_country.activeCells += sleepers
            self.__app.output_to_history("All cells go Active", False)
            if ((failures >= 2 and not target_country.is_besieged()) or
                    (failures == 3 and target_country.is_besieged())) and\
                    len(roll_list) == 3 and target_country.is_poor():
                self.__app.output_to_history("Major Jihad Failure", False)
                target_country.make_besieged()
                self.__app.output_to_history("Besieged Regime", False)
                if target_country.is_adversary():
                    target_country.make_neutral()
                elif target_country.is_neutral():
                    target_country.make_ally()
                self.__app.output_to_history("Alignment %s" % target_country.alignment(), False)
        else:  # a cell is active for each roll
            self.__app.output_to_history("* Minor Jihad attempt in %s" % country_name, False)
            for _ in range(len(roll_list) - target_country.num_active_cells()):
                self.__app.output_to_history("Cell goes Active", False)
                target_country.sleeperCells -= 1
                target_country.activeCells += 1
        while successes > 0 and target_country.governance_is_better_than(POOR):
            target_country.worsen_governance()
            successes -= 1
            self.__app.output_to_history("Governance to %s" % target_country.governance_str(), False)
        if is_major_jihad and ((successes >= 2) or (original_besieged and successes >= 1)):  # Major Jihad
            self.__app.output_to_history("Islamist Revolution in %s" % country_name, False)
            target_country.make_islamist_rule()
            self.__app.output_to_history("Governance to Islamist Rule", False)
            target_country.make_adversary()
            self.__app.output_to_history("Alignment to Adversary", False)
            target_country.remove_regime_change()
            if target_country.is_besieged():
                self.__app.output_to_history("Besieged Regime marker removed.", False)
            target_country.remove_besieged()
            target_country.set_aid(0)
            self.__app.output_to_history("All Aid removed.", False)
            self.__app.funding = min(9, self.__app.funding + self.__app.country_resources_by_name(country_name))
            self.__app.output_to_history("Funding now %d" % self.__app.funding, False)
            if target_country.troops() > 0:
                self.__app.prestige = 1
                self.__app.output_to_history("Troops present so US Prestige now 1", False)
        if self.__app.ideology.failed_jihad_rolls_remove_cells():
            for _ in range(failures):
                if target_country.num_active_cells() > 0:
                    target_country.remove_active_cell()
                else:
                    target_country.sleeperCells -= 1
                    self.__app.output_to_history("Sleeper cell Removed to Funding Track", False)
                    self.__app.cells += 1
        self.__app.output_to_history(target_country.summary(), False)
        print ""

    def _handle_ai_plot_action(self, ops, is_ops):
        plot_rolls = [random.randint(1, 6) for _ in range(ops)]
        return self.__app.execute_plot(ops, is_ops, plot_rolls)

    def handle_jihad(self, country_name, ops):
        """Returns number of unused Ops"""
        cells = self.__app.map.get(country_name).total_cells(True)
        roll_list = [random.randint(1, 6) for _ in range(min(cells, ops))]
        self.execute_jihad(country_name, roll_list)
        return ops - len(roll_list)

    def _handle_minor_jihad(self, country_list, ops):
        ops_remaining = ops
        for countryData in country_list:
            self.handle_jihad(countryData[0], countryData[1])
            ops_remaining -= countryData[1]
        return ops_remaining

    def handle_radicalization(self, ops):
        ops_remaining = ops
        # First box
        if ops_remaining > 0:
            if self.__app.cells > 0:
                country_name = self.__app.randomizer.pick_one(self.__app.map.country_names())
                self.__app.place_cell(country_name)
                ops_remaining -= 1
                # Second box
        if ops_remaining > 0:
            if self.__app.cells < 15:
                self.__app.handle_travel(1, True)
                ops_remaining -= 1
                # Third box
        if ops_remaining > 0:
            if self.__app.funding < 9:
                possibles = []
                for country in self.__app.map.country_names():
                    if not self.__app.map.get(country).is_islamist_rule():
                        if (self.__app.map.get(country).total_cells(True)) > 0:
                            possibles.append(country)
                if len(possibles) > 0:
                    location_name = random.choice(possibles)
                    self.__app.test_country(location_name)
                    self.__app.map.get(location_name).plots += 1
                    self.__app.output_to_history("--> Plot placed in %s." % location_name, True)
                    ops_remaining -= 1
                    # Fourth box
        while ops_remaining > 0:
            possibles = []
            for country in self.__app.map.country_names():
                if self.__app.map.get(country).is_muslim() and \
                        (self.__app.map.get(country).is_good() or self.__app.map.get(country).is_fair()):
                    possibles.append(country)
            if len(possibles) == 0:
                self.__app.output_to_history("--> No remaining Good or Fair countries.", True)
                break
            else:
                location = self.__app.map.get(random.choice(possibles))
                location.worsen_governance()
                self.__app.output_to_history(
                    "--> Governance in %s worsens to %s." % (location.name, location.governance_str()))
                self.__app.output_to_history(location.summary(), True)
                ops_remaining -= 1

    def major_jihad_choice(self, ops):
        """Return AI choice country."""
        possible = self.__app.major_jihad_possible(ops)
        if not possible:
            return False
        else:
            if "Pakistan" in possible:
                return "Pakistan"
            else:
                max_resources = 0
                for country_name in possible:
                    if self.__app.country_resources_by_name(country_name) > max_resources:
                        max_resources = self.__app.country_resources_by_name(country_name)
                new_possible = []
                for country_name in possible:
                    if self.__app.country_resources_by_name(country_name) == max_resources:
                        new_possible.append(country_name)
                return random.choice(new_possible)
