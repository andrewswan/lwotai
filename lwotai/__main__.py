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
from lwotai.command import Command
from lwotai.ideologies.ideologies import choose_ideology
from lwotai.labyrinth import Labyrinth
from lwotai.saver import Saver
from lwotai.scenarios.scenarios import scenario_names
from lwotai.utils import Utils

# Please observe semantic versioning (see http://semver.org) when changing this version number.
RELEASE = "2.0.0"


def _create_game():
    """Factory function for a new game"""
    print ""
    scenario_number = Utils.choose_option("Choose Scenario", scenario_names())
    print ""
    ideology_number = choose_ideology()
    print ""
    ai_rolls = Utils.getUserYesNoResponse("Do you want the program to roll dice for you?")
    return Labyrinth(scenario_number, ideology_number, ai_rolls=ai_rolls)


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
    if saver.suspended_game_exists() and Utils.getUserYesNoResponse("Resume suspended game?"):
        app = saver.load_suspend_file()
    else:
        app = _create_game()
        saver.save_turn_file(app, 0)

    command = Command(app, saver)

    while True:
        command.cmdloop()
        # The user has quit, or wants to undo or rollback; prevents
        # issues dealing with save/reloading within class instance.
        if app.undo:
            print "Undo to last turn"
            app = saver.load_undo_file()
        elif app.roll_turn >= 0:
            print "Rolling back to turn " + str(app.roll_turn)
            app = saver.load_turn_file(app.roll_turn)
            if not app:
                break
        else:
            break


if __name__ == "__main__":
    main()
