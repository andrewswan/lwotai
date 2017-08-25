from lwotai.cards.deck import Deck

from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class DeckTest(LabyrinthTestCase):
    """Deck tests"""

    def test_deck(self):
        """Test Deck"""
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        for i in range(121):
            if i > 0:
                self.assertEqual(i, app.card(i).number)

    def test_initial_size(self):
        # Set up
        deck = Deck()

        # Invoke
        size = len(deck)

        # Check
        self.assertEqual(120, size)
