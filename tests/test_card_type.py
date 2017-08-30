from unittest import TestCase

from lwotai.cards.jihadist.card60 import Card60
from lwotai.cards.unassociated.card120 import Card120
from lwotai.cards.us.card1 import Card1


class CardTypeTest(TestCase):

    def test_unassociated_card_is_unassociated(self):
        self.assertTrue(Card120().is_unassociated())

    def test_us_card_is_not_unassociated(self):
        self.assertFalse(Card1().is_unassociated())

    def test_jihadist_card_is_not_unassociated(self):
        self.assertFalse(Card60().is_unassociated())
