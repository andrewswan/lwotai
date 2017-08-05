from lwotai.randomizer import Randomizer
from unittest import TestCase


class RandomizerTest(TestCase):

    def setUp(self):
        self.randomizer = Randomizer()

    def test_pick_no_items_from_empty_list(self):
        # Invoke
        picks = self.randomizer.pick(0, [])

        # Check
        self.assertEqual(picks, [])

    def test_pick_no_items_from_single_item_list(self):
        # Invoke
        picks = self.randomizer.pick(0, ['Bob'])

        # Check
        self.assertEqual(picks, [])

    def test_pick_one_items_from_single_item_list(self):
        # Invoke
        item = 'Bob'
        pick = self.randomizer.pick_one([item])

        # Check
        self.assertEqual(pick, item)

    def test_pick_single_item_from_single_item_list(self):
        # Invoke
        picks = self.randomizer.pick(1, ['Bob'])

        # Check
        self.assertEqual(picks, ['Bob'])

    def test_pick_one_item_from_two_item_list(self):
        # Set up
        options = ['Bob', 'Carl']

        # Invoke
        picks = self.randomizer.pick(1, options)

        # Check
        self.assertEqual(1, len(picks))
        self.assertTrue(picks[0] in options)

    def test_roll_d6(self):
        # Invoke
        roll_count = 1000
        rolls = self.randomizer.roll_d6(roll_count)

        # Check
        self.assertEqual(len(rolls), roll_count)
        for roll in rolls:
            self.assertIn(roll, [1, 2, 3, 4, 5, 6])
