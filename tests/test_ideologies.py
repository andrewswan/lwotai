from unittest import TestCase
from lwotai.ideologies.normal import Normal


class IdeologiesTest(TestCase):

    def test_normal(self):
        normal = Normal()
        self.assertEqual("Normal", normal.name)
