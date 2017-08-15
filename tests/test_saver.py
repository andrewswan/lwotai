import unittest

from lwotai.labyrinth import Labyrinth
from lwotai.saver import Saver


class SaverTest(unittest.TestCase):
    """Tests the Saver class"""

    def test_turn_file_can_be_saved_and_loaded(self):
        """Tests that the game can be saved to and loaded from a turn file"""
        # Set up
        saver = Saver()
        game_to_save = Labyrinth(1, 1)
        turn_number = 9999  # so as not to overwrite a real turn file
        game_to_save.turn = turn_number
        saver.save_current_turn_file(game_to_save)

        # Invoke
        loaded_game = saver.load_turn_file(turn_number)

        # Check
        self.assertEqual(loaded_game.backlashInPlay, game_to_save.backlashInPlay)
        self.assertEqual(loaded_game.cells, game_to_save.cells)
        self.assertEqual(loaded_game.funding, game_to_save.funding)
        self.assertEqual(loaded_game.gameOver, game_to_save.gameOver)
        self.assertEqual(loaded_game.history, game_to_save.history)
        self.assertEqual(loaded_game.ideology, game_to_save.ideology)
        self.assertEqual(loaded_game.lapsing, game_to_save.lapsing)
        self.assertEqual(loaded_game.markers, game_to_save.markers)
        self.assertEqual(loaded_game.phase, game_to_save.phase)
        self.assertEqual(loaded_game.prestige, game_to_save.prestige)
        self.assertEqual(loaded_game.roll_turn, game_to_save.roll_turn)
        self.assertEqual(loaded_game.scenario, game_to_save.scenario)
        self.assertEqual(loaded_game.startYear, game_to_save.startYear)
        self.assertEqual(loaded_game.troops, game_to_save.troops)
        self.assertEqual(loaded_game.turn, game_to_save.turn)
        self.assertEqual(loaded_game.undo, game_to_save.undo)
        self.assertEqual(loaded_game.validCountryMarkers, game_to_save.validCountryMarkers)
        self.assertEqual(loaded_game.validGlobalMarkers, game_to_save.validGlobalMarkers)
        self.assertEqual(loaded_game.validLapsingMarkers, game_to_save.validLapsingMarkers)
