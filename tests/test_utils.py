import __builtin__
from unittest import TestCase

from lwotai.utils import Utils


class UtilsTest(TestCase):
    """Tests the utils module. Does not contain test-time utility methods."""

    def test_choose_option_with_numeric_input(self):
        # Set up
        dogs = ['Boxer', 'Chow', 'Pug']
        original_raw_input = __builtin__.raw_input
        __builtin__.raw_input = lambda _: "1"

        # Invoke
        dog_number = Utils.choose_option("Fave dog?", dogs)

        # Check
        self.assertEqual(1, dog_number)
        __builtin__.raw_input = original_raw_input
