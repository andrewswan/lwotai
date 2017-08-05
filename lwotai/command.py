from cmd import Cmd
from saver import Saver

class Command(Cmd):
    """The command-line processor for this application"""

    def __init__(self, app, saver=Saver(), completekey='tab', stdin=None, stdout=None):
        Cmd.__init__(self, completekey, stdin, stdout)
        self.app = app
        self.saver = saver

    # noinspection SpellCheckingInspection: comes from Cmd superclass
    def emptyline(self):
        self.app.print_turn_number()

    def postcmd(self, stop, line):
        self.saver.save_suspend_file(self)
        if line == "quit":
            return True
        if self.app.undo:
            return True
        if self.app.roll_turn >= 0:
            return True
        self.app.validate()
        print "--------------------------------------------------------------------------------"

    # ----------------------------- App-specific commands ---------------------------
    # These methods are named "do_<command_name>", as expected by the superclass.
    # The docstring for each command is what the user sees when they type "help <command_name>"

    def do_adjust(self, ignored):
        """Adjusts the game state - no validation is done, so be careful."""
        self.app.adjust_state()

    def do_alert(self, ignored):
        """Alerts a country to an active plot."""
        self.app.alert_plot()

    def do_deploy(self, ignored):
        """Move troops from the troop track or a country to another country."""
        self.app.redeploy_troops()

    def do_disrupt(self, ignored):
        """Disrupts cells or cadre in a country."""
        self.app.disrupt_cells_or_cadre()

    def do_history(self, argument):
        """Displays the game history. Type 'history save' to also save it to a file called history.txt."""
        self.app.show_history(argument)

    def do_jihadist_card(self, card_number):
        """Plays the given card as the Jihadist player, when it's their turn."""
        self.app.play_jihadist_card(card_number)

    def do_plot(self, ignored):
        """Use this command after the US Action Phase to resolve any unblocked plots."""
        self.app.resolve_plots()

    def do_quit(self, ignored):
        """Quits the game and prompts you to save."""
        self.app.quit()

    def do_reassessment(self, ignored):
        """Changes the US Posture, i.e. toggles between Hard <--> Soft."""
        self.app.toggle_us_posture()

    def do_regime_change(self, ignored):
        """Performs a Regime Change in a selected Islamist Rule country."""
        self.app.change_regime()

    def do_reserves(self, ignored):
        """
        Allows the US player to add a card's Ops value to the US Reserves track. (6.3.3)
        Remember to set this track to 0 when you use it or at end of turn, whichever comes first.
        """
        self.app.deploy_reserves()

    def do_roll_back(self, ignored):
        """Rolls the game back to a chosen turn in the game."""
        self.app.roll_back()

    def do_status(self, country_name):
        """Displays the game status. 'status [country]' will print the status of that country."""
        self.app.show_status(country_name)

    def do_summary(self, ignored):
        """Displays a summary of the game status."""
        self.app.show_summary()

    def do_turn(self, ignored):
        """Use this command to indicate the end of the turn."""
        self.app.end_turn()

    def do_undo(self):
        """Rolls back to the last card played."""
        self.app.undo_last_turn()

    def do_us_card(self, card_number):
        """Plays the given card as the US when it's the US action phase."""
        self.app.play_us_card(card_number)

    def do_war_of_ideas(self, ignored):
        """Carries out a "War of Ideas" action in a selected country."""
        self.app.war_of_ideas()

    def do_withdraw(self, ignored):
        """Withdraws troops from a selected country"""
        self.app.withdraw_troops()

