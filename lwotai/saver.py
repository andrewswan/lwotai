"""
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
"""

import os
import sys

try:
    import cPickle as pickle
except ImportError:
    import pickle


class Saver:
    """Saves and loads the game"""

    SUSPEND_FILE = "suspend.lwot"
    UNDO_FILE = "undo.lwot"
    ROLLBACK_FILE = "turn."

    def __init__(self):
        pass

    def new_session(self):
        """The user is starting a new game session"""
        self._delete_undo_file_if_exists()

        # Delete previous turns' save files, if any
        for the_file in os.listdir(os.curdir):
            if "turn." in the_file and ".lwot" in the_file:
                os.remove(the_file)

    def suspended_game_exists(self):
        """Indicates whether a saved game exists"""
        return os.path.exists(self.SUSPEND_FILE)

    def load_game(self):
        """Loads the game; returns a Labyrinth object"""
        f = open(self.SUSPEND_FILE,'rb')
        app = pickle.load(f)
        app.stdout = sys.stdout
        app.undo = False
        f.close()
        return app

    def save_rollback_file(self, app, turn_number):
        """Saves a rollback file at the start of the given turn"""
        turn_file = self.ROLLBACK_FILE + str(turn_number) + ".lwot"
        self._save_game(app, turn_file)

    def roll_back(self, turn_number):
        """Returns the saved game as it was at the given turn number"""
        turn_file = self.ROLLBACK_FILE + str(turn_number) + '.lwot'
        f = open(turn_file, 'rb')
        app = pickle.load(f)
        app.stdout = sys.stdout
        f.close()
        # rollback invalidates undo save so delete it
        self._delete_undo_file_if_exists()
        return app

    def load_undo_file(self):
        """Loads the game from the 'undo' file (returns the loaded game)"""
        f = open(self.UNDO_FILE, 'rb')
        app = pickle.load(f)
        app.stdout = sys.stdout
        f.close()
        return app

    def _delete_undo_file_if_exists(self):
        if os.path.exists(self.UNDO_FILE):
            os.remove(self.UNDO_FILE)

    def save_undo_file(self, app):
        self._save_game(app, self.UNDO_FILE)

    def save_turn_file(self, app):
        """Saves the given app at its current turn number"""
        self._save_game(app, self.ROLLBACK_FILE + str(app.turn) + ".lwot")

    def save_suspend_file(self, app):
        self._save_game(app, self.SUSPEND_FILE)

    @staticmethod
    def _save_game(app, save_file_name):
        """Saves the given app to the given file"""
        save_file = open(save_file_name, 'wb')
        pickle.dump(app, save_file, 2)
        save_file.close()
