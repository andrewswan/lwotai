from unittest import TestCase

from postures.posture import Posture, HARD, SOFT


class PostureTest(TestCase):
    """Tests the Posture class"""

    def test_two_postures_with_same_name_are_equal(self):
        # Set up
        name = "Foo"
        p1 = Posture(name)
        p2 = Posture(name)

        # Invoke and check
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 != p2)

    def test_two_postures_with_different_names_are_not_equal(self):
        # Set up
        p1 = Posture("p1")
        p2 = Posture("p2")

        # Invoke and check
        self.assertTrue(p1 != p2)
        self.assertFalse(p1 == p2)

    def test_hard_is_a_posture(self):
        self.assertTrue(type(HARD) == Posture)

    def test_soft_is_a_posture(self):
        self.assertTrue(type(SOFT) == Posture)

    def test_hard_is_in_list(self):
        self.assertTrue(Posture("Hard") in [Posture("Hard")])
