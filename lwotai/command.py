from cmd import Cmd

from lwotai.labyrinth import Labyrinth
from lwotai.saver import Saver
from lwotai.utils import Utils


class Command(Cmd):
    """The command-line processor for this application"""

    def __init__(self, app, saver=Saver(), complete_key='tab', std_in=None, std_out=None):
        Cmd.__init__(self, complete_key, std_in, std_out)
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

    # The complete_<command_name> methods take four arguments:
    #
    # 1. 'text' is the string we are matching against, all returned matches must begin with it
    # 2. 'line' is the current input line
    # 3. 'begidx' is the beginning index in the line of the text being matched
    # 4. 'endidx' is the end index in the line of the text being matched
    #
    # e.g. for the "alert" command: alert text = '', line = 'alert ', begidx = 6, endidx = 6

    def do_adjust(self, _):
        """Adjusts the game state - no validation is done, so be careful."""
        self.app.adjust_state()

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

    def do_reserves(self, ops_str):
        """Allows the US player to add the given Ops value to the US Reserves track. (6.3.3)"""
        ops = None
        if ops_str:
            try:
                ops = int(ops_str)
            except ValueError:
                print "Invalid ops value '%s'" % ops_str
        if not ops:
            card_number = Utils.prompt_for_card_number()
            if not card_number:
                return
            ops = self.app.card(card_number).ops
        self.app.deploy_reserves(ops)
        print "Discard this card and set the US Reserves track to %d" % self.app.us_reserves

    def do_roll_back(self, _):
        """Rolls the game back to a chosen turn in the game."""
        self.app.load_turn_file()

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
