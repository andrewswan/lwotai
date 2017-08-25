from unittest import TestCase

from lwotai.ideologies.normal import Normal
from lwotai.ideologies.virulent import Virulent


class IdeologiesTest(TestCase):

    def test_normal_name(self):
        normal = Normal()
        self.assertEqual("Normal", normal.name())

    def test_virulent_string_representation(self):
        ideology = Virulent()
        self.assertEqual("Virulent", "%s" % ideology)
