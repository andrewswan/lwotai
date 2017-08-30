from unittest import TestCase

from mockito import mock

from lwotai.cards.jihadist.card49 import Card49
from lwotai.cards.us.card2 import Card2
from lwotai.labyrinth import Labyrinth


class CardPlayableTest(TestCase):
    """Tests the generic 'is playable' methods"""

    def _assert_playable_us_event(self, card, app, expected_result):
        self.assertEqual(expected_result, card.is_playable_us_event(app))

    def _assert_playable_non_us_event(self, card, app, expected_result):
        self.assertEqual(expected_result, card.is_playable_non_us_event(app))

    def test_always_playable_us_card_is_playable_us_event(self):
        self._assert_playable_us_event(Card2(), None, True)

    def test_always_playable_us_card_is_not_playable_non_us_event(self):
        self._assert_playable_non_us_event(Card2(), None, False)

    def test_always_playable_jihadist_card_is_not_a_playable_us_event(self):
        self._assert_playable_us_event(Card49(), None, False)

    def test_always_playable_jihadist_card_is_playable_non_us_event(self):
        app = mock(Labyrinth)
        app.lapsing = []
        self._assert_playable_non_us_event(Card49(), app, True)
