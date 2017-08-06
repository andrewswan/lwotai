"""
LWOTai - A Python implementation of the Single-Player AI for Labyrinth: the War on Terror by GMT Games.
Mike Houser, 2011

Thanks to Dave Horn for implementing the Save and Undo system.

1. A save game is created after every single command whether you want it or not. If someone screws up and closes the
   window, PC battery dies, crashes, whatever, no problem, load it up again and you will be asked if you want to load
   the suspended game.

2. Rollback files are created at the beginning of each turn. You can roll back to any previous turn using the 'roll' or
   'rollback' command. You will be prompted to enter the turn to which you want to roll back.

3. An undo file is created after every card played. The player can undo to the last card at any time (with two
   exceptions) by typing 'undo'. The exceptions are:
   - when you load from a previously suspended game, or
   - after executing a rollback. The undo file is removed at that exact point, to prevent the player from undoing
     themselves to some other game from the past!

Thanks to Peter Shaw for implementing the Adjust system and for a bunch of bug fixes and cleanup.
"""

from command import Command
from labyrinth import Labyrinth
from scenario.scenario import scenario_names
from saver import Saver
from utils import Utils

# Please observe semantic versioning (see http://semver.org) when changing this version number.
RELEASE = "2.0.0"


def _create_game():
    """Factory function for a new game"""
    print ""
    scenario_number = Utils.choose_option("Choose Scenario", scenario_names())
    print ""
    ideology_number = Utils.choose_option("Choose Jihadist Ideology",
                                   ["Normal",
                                    "Coherent: Plot success places 2 Plots",
                                    "Attractive: ...and Recruit success places 2 cells",
                                    "Potent: ...and Major Jihad if 3 or more cells than troops",
                                    "Infectious: ...and US plays all its cards (not enforced by program)",
                                    "Virulent: ...and Jihad failure does not remove cells"])
    return Labyrinth(scenario_number, ideology_number)


def main():
    """The main function that runs the game"""
    print ""
    print "Labyrinth: The War on Terror AI Player"
    print ""
    print "Release", RELEASE
    print ""
    saver = Saver()
    saver.new_session()
    
    # Ask user if they want to continue previous game                    
    if saver.suspended_game_exists() and Utils.getUserYesNoResponse("Resume suspended game? (y/n): "):
        app = saver.load_game()
    else:
        app = _create_game()
        saver.save_rollback_file(app, 0)

    command = Command(app, saver)

    while True:
        command.cmdloop()
        # The user has quit, or wants to undo or rollback - prevents issues dealing with save/reloading within class instance
        if app.undo:
            print "Undo to last turn"
            app = saver.load_undo_file()
        elif app.roll_turn >= 0:
            print "Rolling back to turn " + str(app.roll_turn)
            app = saver.roll_back(app.roll_turn)
        else:
            break


if __name__ == "__main__":
    main()
