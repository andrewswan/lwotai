from cmd import Cmd

from lwotai.labyrinth import Labyrinth
from lwotai.saver import Saver
from lwotai.utils import Utils


class Command(Cmd):
    """The command-line processor for this application"""

    def __init__(self, app, saver=Saver(), complete_key='tab', std_in=None, std_out=None):
        Cmd.__init__(self, complete_key, std_in, std_out)
        self.__country_names = app.get_country_names()
        self.__game_attributes = ["cells", "funding", "ideology", "lapsing", "marker", "prestige"]
        self.app = Utils.require_type(app, Labyrinth)
        self.saver = Utils.require_type(saver, Saver)
        self.prompt = "Enter command (? for help, Tab to complete): "

    # noinspection SpellCheckingInspection: comes from Cmd superclass
    def emptyline(self):
        self.app.print_turn_number()

    def postcmd(self, stop, line):
        self.saver.save_suspend_file(self.app)
        if line == "quit":
            return True
        if self.app.undo:
            return True
        if self.app.roll_turn >= 0:
            return True
        self.app.validate()
        print "--------------------------------------------------------------------------------"

    # ----------------------------- App-specific commands ---------------------------
    # The superclass expects these methods to be named "do_<command_name>" and take an argument.
    # The docstring for each command is what the user sees when they type "help <command_name>".

    def do_adjust(self, remaining_line):
        """
        Adjusts the game state - no validation is done, so be careful.
        Examples:
            adjust funding
            adjust Morocco sleepers
        """
        args = remaining_line.split()
        if not args:
            print "Please specify the country (if applicable) and the attribute to change"
        elif len(args) == 1:
            # Should be a game (not country) attribute
            arg_1 = args[0]
            if arg_1 in self.__game_attributes:
                self.app.adjust_game_attribute(arg_1)
            elif arg_1 in self.__country_names:
                print "Please specify the thing to adjust in %s (press Tab to see options)" % arg_1
            else:
                print "Invalid option '%s'" % arg_1
        elif len(args) == 2:
            # Should be a country name and a valid attribute for that country
            country_name = args[0]
            country_attribute = args[1]
            self.app.adjust_country(country_name, country_attribute)
        else:
            print "Invalid input (hint: use Tab key to complete or find valid options)"

    def complete_adjust(self, text, line, begin_index, _end_index):
        """
        :param text: the string we are matching against
        :param line: the current input line (lstripped)
        :param begin_index: the beginning index of the text being matched, which could be used to provide
            different completion depending upon which position the argument is in.
        :param _end_index: the end index of the text being matched
        :return: a list of adjustable things
        """
        # print "text = '%s', line = '%s', begin_index = %d, end_index = %d" % (text, line, begin_index, _end_index)
        options = []
        if begin_index == len("adjust "):
            # Picking a game attribute or country
            options.extend(self.__country_names)
            options.extend(self.__game_attributes)
        else:
            # Picking a country attribute
            country_name = line.split()[1]
            country = self.app.get_country(country_name)
            options.extend(country.get_adjustable_attributes())
        return [option for option in options if option.lower().startswith(text.lower())]

    def do_alert(self, _):
        """Alerts a country to an active plot."""
        self.app.alert_plot()

    def do_clear_reserves(self, _):
        """Manually resets the US Reserves track to 0 Ops after use."""
        self.app.us_reserves = 0
        print "Reset the US Reserves track to 0 Ops."

    def do_deploy(self, _):
        """
        Move troops from the troop track or a country to a Muslim Ally.
        Use the "regime_change" command to deploy to an Islamist Rule country.
        """
        self.app.deploy_troops()

    def do_disrupt(self, _):
        """Disrupts cells or cadre in a country."""
        self.app.disrupt_cells_or_cadre()

    def do_history(self, argument):
        """Displays the game history. Type 'history save' to also save it to a file called history.txt."""
        self.app.show_history(argument)

    def do_jihadist_card(self, card_num_str):
        """Plays the given card as the Jihadist player, when it's their turn."""
        self._play_card(card_num_str, self.app.play_jihadist_card)

    def do_plot(self, _):
        """Use this command after the US Action Phase to resolve any unblocked plots."""
        self.app.resolve_plots()

    def do_quit(self, _):
        """Quits the game and prompts you to save."""
        if Utils.getUserYesNoResponse("Save the game?"):
            print "Saving suspend file."
            self.saver.save_suspend_file(self.app)
        print "Exiting."

    def do_reassessment(self, _):
        """Changes the US Posture, i.e. toggles between Hard <--> Soft."""
        self.app.toggle_us_posture()

    def do_regime_change(self, _):
        """Performs a Regime Change in a selected Islamist Rule country."""
        self.app.change_regime()

    def do_reserves(self, _):
        """Allows the US player to add the given Ops value to the US Reserves track. (6.3.3)"""
        self.app.deploy_reserves()

    def do_roll_back(self, _):
        """Rolls the game back to a chosen turn in the game."""
        loaded_app = self.saver.load_turn_file(self.app.turn)
        if loaded_app:
            self.app = loaded_app

    def do_status(self, country_name):
        """Displays the game status, or 'status [country]' displays the status of that country."""
        self.app.show_status(country_name)

    def do_summary(self, _):
        """Displays a summary of the game status."""
        self.app.print_summary()

    def do_turn(self, _):
        """Use this command to indicate the end of the turn."""
        self.saver.save_current_turn_file(self.app)
        self.app.end_turn()

    def do_undo(self):
        """Rolls back to the last card played."""
        self.app.undo_last_turn()

    def do_us_card(self, card_num_str):
        """Plays the given card as the US when it's the US action phase."""
        self._play_card(card_num_str, self.app.play_us_card)

    def _play_card(self, card_num_str, handler):
        """Plays the given card using the given handler function"""
        card_number = self._get_card_number(card_num_str)
        if card_number:
            self.saver.save_undo_file(self.app)
            handler(card_number)

    @staticmethod
    def _get_card_number(card_number_str):
        if card_number_str:
            return Utils.parse_card_number(card_number_str)
        return Utils.prompt_for_card_number()

    def do_war_of_ideas(self, _):
        """Carries out a "War of Ideas" action in a selected country."""
        self.app.war_of_ideas()

    def do_withdraw(self, _):
        """Withdraws troops from a selected country"""
        self.app.withdraw_troops()
