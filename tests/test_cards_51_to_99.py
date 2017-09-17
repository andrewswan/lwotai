import unittest

from mockito import mock, when, verify, ANY

from labyrinth_test_case import LabyrinthTestCase
from lwotai.cards.card import Card
from lwotai.cards.jihadist.card53 import Card53
from lwotai.labyrinth import Labyrinth
from lwotai.randomizer import Randomizer
from postures.posture import HARD


class Card51(LabyrinthTestCase):
    """FREs"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(51).playable("Jihadist", app, False))    
        iraq.change_troops(1)
        self.assertTrue(app.deck.get(51).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(51).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        iraq = app.get_country("Iraq")
        iraq.change_troops(1)
        app.deck.get(51).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.markers.append("Saddam Captured")
        app.test_country("Iraq")
        iraq.change_troops(1)
        app.deck.get(51).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.cells = 3
        app.test_country("Iraq")
        iraq.change_troops(1)
        app.deck.get(51).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 3)


class Card52(LabyrinthTestCase):
    """IEDs"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(52).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_regime_change()
        iraq.sleeperCells = 1
        self.assertTrue(app.deck.get(52).playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(52).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(52).play_event("Jihadist", app)


class Card53Test(LabyrinthTestCase):
    """Madrassas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck.get(53).playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck.get(53).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(53).puts_cell())

    @staticmethod
    def test_recruits_with_one_op_if_no_next_card():
        # Set up
        card = Card53()
        app = mock(Labyrinth)
        when(app).get_card_num_from_user(ANY(str)).thenReturn("n")
        when(app).handle_recruit(1, True).thenReturn(0)
        when(app).output_to_history(ANY(str), ANY(bool))

        # Invoke
        card.play_as_jihadist(app)

        # Check
        verify(app).handle_recruit(1, True)
        verify(app).output_to_history("No cards left to recruit.", True)

    @staticmethod
    def test_recruits_twice_if_there_is_a_next_card():
        # Set up
        card = Card53()
        app = mock(Labyrinth)
        when(app).get_card_num_from_user(ANY(str)).thenReturn(20)
        when(app).handle_recruit(ANY(int), ANY(bool)).thenReturn(0)
        when(app).output_to_history(ANY(str), ANY(bool))
        next_card = mock(Card)
        next_card.ops = 3
        when(app).get_card(20).thenReturn(next_card)

        # Invoke
        card.play_as_jihadist(app)

        # Check
        verify(app).handle_recruit(1, True)
        verify(app).handle_recruit(3, True)


class Card54(LabyrinthTestCase):
    """Moqtada al-Sadr"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(54).playable("Jihadist", app, False))
        iraq.change_troops(1)
        self.assertTrue(app.deck.get(54).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(54).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.deck.get(54).play_event("Jihadist", app)
        self.assertTrue("Sadr" in iraq.markers)


class Card55(LabyrinthTestCase):
    """Uyghur Jihad"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(55).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(55).puts_cell())

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
            app.deck.get(55).play_event("Jihadist", app)
            self.assertTrue(app.get_country("China").get_posture())
            if app.get_country("China").is_soft():
                self.assertTrue(app.get_country("China").sleeperCells == 1)
            else:
                self.assertTrue(app.get_country("Central Asia").is_governed())
                self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)


class Card56(LabyrinthTestCase):
    """Vieira de Mello Slain"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(56).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_regime_change()
        self.assertFalse(app.deck.get(56).playable("Jihadist", app, False))    
        iraq.sleeperCells = 1
        self.assertTrue(app.deck.get(56).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(56).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(56).play_event("Jihadist", app)
        self.assertTrue("Vieira de Mello Slain" in app.markers)
        self.assertTrue(app.prestige == 6)


class Card57(LabyrinthTestCase):
    """Abu Sayyaf"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(57).playable("Jihadist", app, False))    
        app.markers.append("Moro Talks")
        self.assertFalse(app.deck.get(57).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(57).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(57).play_event("Jihadist", app)
        self.assertTrue("Abu Sayyaf" in app.markers)
        self.assertTrue(app.get_country("Philippines").is_governed())
        self.assertTrue(app.get_country("Philippines").sleeperCells == 1)
        app.get_country("Philippines").sleeperCells = 3
        app.place_plots("Philippines", 0, [1, 5, 1])
        self.assertTrue(app.prestige == 5)


class Card58(LabyrinthTestCase):
    """Al-Anbar"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(58).playable("Jihadist", app, False))    
        app.markers.append("Anbar Awakening")
        self.assertFalse(app.deck.get(58).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(58).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.deck.get(58).play_event("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        self.assertTrue(iraq.sleeperCells == 1)
        app.test_country("Iraq")
        iraq.sleeperCells = 3
        iraq.troopCubes = 3
        app.handle_disrupt("Iraq")
        self.assertTrue(iraq.sleeperCells == 2)
        self.assertTrue(iraq.activeCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(58).play_event("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.test_country("Syria")
        app.get_country("Syria").sleeperCells = 3
        app.get_country("Syria").troopCubes = 3
        app.handle_disrupt("Syria")
        self.assertTrue(app.get_country("Syria").sleeperCells == 2)
        self.assertTrue(app.get_country("Syria").activeCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(58).play_event("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.test_country("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 3
        app.get_country("Afghanistan").troopCubes = 3
        app.handle_disrupt("Afghanistan")
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").activeCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(58).play_event("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.test_country("Iraq")
        iraq.cadre = 1
        iraq.troopCubes = 3
        app.handle_disrupt("Iraq")
        self.assertTrue(iraq.cadre == 1)


class Card59(LabyrinthTestCase):
    """Amerithrax"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(59).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(59).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(59).play_event("Jihadist", app)


class Card60(LabyrinthTestCase):
    """Bhutto Shot"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(60).playable("Jihadist", app, False))
        app.get_country("Pakistan").sleeperCells = 1
        self.assertTrue(app.deck.get(60).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(60).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(60).play_event("Jihadist", app)
        self.assertTrue("Bhutto Shot" in app.markers)


class Card61(LabyrinthTestCase):
    """Detainee Release"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.lapsing.append("GTMO")
        self.assertFalse(app.deck.get(61).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Renditions")
        self.assertFalse(app.deck.get(61).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck.get(61).playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck.get(61).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(61).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        app.deck.get(61).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 1)


class Card62(LabyrinthTestCase):
    """Ex-KGB"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(62).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(62).puts_cell())

    def test_event_removes_ctr_marker_from_russia(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Russia").markers.append("CTR")
        app.get_country("Caucasus").make_hard()
        app.get_country("Spain").make_soft()
        app.get_country("Germany").make_soft()
        app.deck.get(62).play_event("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").is_hard())
        self.assertTrue(app.get_country("Central Asia").is_ungoverned())

    def test_event_changes_caucasus_posture_if_that_changes_world_posture(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Caucasus").make_hard()
        app.get_country("Spain").make_soft()
        app.get_country("Germany").make_soft()
        app.deck.get(62).play_event("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").is_soft())
        self.assertTrue(app.get_country("Central Asia").is_ungoverned())

    def test_event_shifts_central_asia_from_neutral_to_adversary_if_caucasus_would_not_affect_world_posture(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        caucasus = app.get_country("Caucasus")
        caucasus.make_hard()
        app.get_country("France").make_hard()
        app.get_country("Germany").make_hard()
        app.get_country("Italy").make_hard()
        app.us().make_hard()
        central_asia = app.get_country("Central Asia")
        central_asia.untest()

        # Invoke
        app.deck.get(62).play_event("Jihadist", app)

        # Check
        self.assertFalse("CTR" in app.get_country("Russia").markers)
        self.assertEqual(caucasus.get_posture(), HARD)
        self.assertTrue(central_asia.is_governed())
        self.assertTrue(central_asia.is_adversary())

    def test_event_shifts_central_asia_from_ally_to_neutral_if_caucasus_would_not_affect_world_posture(self):
        # Set up extreme hard world posture
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Central Asia").make_ally()
        app.get_country("Central Asia").make_fair()
        app.get_country("Benelux").make_hard()
        app.get_country("France").make_hard()
        app.get_country("Israel").make_hard()
        app.get_country("Italy").make_hard()
        app.us().make_hard()
        caucasus_posture_before = app.get_posture("Caucasus")

        # Invoke
        app.deck.get(62).play_event("Jihadist", app)

        # Check
        self.assertEqual(app.get_posture("Caucasus"), caucasus_posture_before)
        self.assertTrue(app.get_country("Central Asia").is_governed())
        self.assertTrue(app.get_country("Central Asia").is_neutral())


class Card63(LabyrinthTestCase):
    """Gaza War"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(63).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(63).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(63).play_event("Jihadist", app)
        self.assertTrue(app.funding == 6)
        self.assertTrue(app.prestige == 6)


class Card64(LabyrinthTestCase):
    """Hariri Killed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(64).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(64).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_good()
        app.get_country("Syria").make_ally()
        app.deck.get(64).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_fair())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_fair()
        app.get_country("Syria").make_ally()
        app.deck.get(64).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_poor())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_poor()
        app.get_country("Syria").make_ally()
        app.deck.get(64).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_poor())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_islamist_rule()
        app.get_country("Syria").make_ally()
        app.deck.get(64).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_islamist_rule())
        self.assertTrue(app.get_country("Syria").is_adversary())


class Card65(LabyrinthTestCase):
    """HEU"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(65).playable("Jihadist", app, False))
        app.test_country("Russia")
        app.get_country("Russia").sleeperCells = 1
        self.assertTrue(app.deck.get(65).playable("Jihadist", app, False))
        app.get_country("Russia").markers.append("CTR")
        self.assertFalse(app.deck.get(65).playable("Jihadist", app, False))
        app.test_country("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        self.assertTrue(app.deck.get(65).playable("Jihadist", app, False))
        app.get_country("Central Asia").markers.append("CTR")
        self.assertFalse(app.deck.get(65).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(65).puts_cell())

    def test_success_roll_in_russia(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([1])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Russia")
        russia = app.get_country("Russia")
        russia.sleeperCells = 1

        # Invoke
        app.card(65).play_event("Jihadist", app)

        # Check
        self.assertTrue(russia.sleeperCells == 1)

    def test_failed_roll_in_russia(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([3])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Russia")
        russia = app.get_country("Russia")
        russia.sleeperCells = 1

        # Invoke
        app.card(65).play_event("Jihadist", app)

        # Check
        self.assertTrue(russia.sleeperCells == 0)

    def test_success_roll_in_central_asia(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([1])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Central Asia")
        central_asia = app.get_country("Central Asia")
        central_asia.sleeperCells = 1

        # Invoke
        app.card(65).play_event("Jihadist", app)

        # Check
        self.assertTrue(central_asia.sleeperCells == 1)

    def test_failed_roll_in_central_asia(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([4])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Central Asia")
        central_asia = app.get_country("Central Asia")
        central_asia.sleeperCells = 1

        # Invoke
        app.card(65).play_event("Jihadist", app)

        # Check
        self.assertTrue(central_asia.sleeperCells == 0)


class Card66(LabyrinthTestCase):
    """Homegrown"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(66).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(66).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(66).play_event("Jihadist", app)
        self.assertTrue(app.get_country("United Kingdom").get_posture())
        self.assertTrue(app.get_country("United Kingdom").sleeperCells == 1)


class Card67(LabyrinthTestCase):
    """Islamic Jihad Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(67).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(67).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(67).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck.get(67).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 0)


class Card68(LabyrinthTestCase):
    """Jemaah Islamiya"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(68).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(68).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(68).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Indonesia/Malaysia").sleeperCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck.get(68).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Indonesia/Malaysia").sleeperCells == 1)


class Card69(LabyrinthTestCase):
    """Kazakh Strain"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        self.assertTrue(app.deck.get(69).playable("Jihadist", app, False))
        app.get_country("Central Asia").markers.append("CTR")
        self.assertFalse(app.deck.get(69).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(69).puts_cell())

    def test_success_roll_does_not_remove_sleeper_cell(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([1])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Central Asia")
        central_asia = app.get_country("Central Asia")
        central_asia.sleeperCells = 1

        # Invoke
        app.card(69).play_event("Jihadist", app)

        # Check
        self.assertTrue(central_asia.sleeperCells == 1)

    def test_failed_roll_removes_sleeper_cell(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([4])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Central Asia")
        central_asia = app.get_country("Central Asia")
        central_asia.sleeperCells = 1

        # Invoke
        app.card(69).play_event("Jihadist", app)

        # Check
        self.assertTrue(central_asia.sleeperCells == 0)


class Card70(LabyrinthTestCase):
    """Lashkar-e-Tayyiba"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(70).playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck.get(70).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(70).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(70).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue(app.get_country("India").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck.get(70).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue(app.get_country("India").sleeperCells == 0)


class Card71(LabyrinthTestCase):
    """Loose Nuke"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Russia")
        app.get_country("Russia").sleeperCells = 1
        self.assertTrue(app.deck.get(71).playable("Jihadist", app, False))
        app.get_country("Russia").markers.append("CTR")
        self.assertFalse(app.deck.get(71).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(71).puts_cell())

    def test_success_roll_leaves_sleeper_cell_intact(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([1])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Russia")
        russia = app.get_country("Russia")
        russia.sleeperCells = 1

        # Invoke
        app.card(71).play_event("Jihadist", app)

        # Check
        self.assertTrue(russia.sleeperCells == 1)

    def test_failed_roll_removes_sleeper_cell(self):
        # Set up
        randomizer = mock(Randomizer)
        when(randomizer).roll_d6(1).thenReturn([4])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, randomizer=randomizer)
        app.test_country("Russia")
        russia = app.get_country("Russia")
        russia.sleeperCells = 1

        # Invoke
        app.card(71).play_event("Jihadist", app)

        # Check
        self.assertTrue(russia.sleeperCells == 0)


class Card72(LabyrinthTestCase):
    """Opium"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(72).playable("Jihadist", app, False))
        app.get_country("Afghanistan").sleeperCells = 1
        self.assertTrue(app.deck.get(72).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(72).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 14
        app.test_country("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.deck.get(72).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 14
        app.test_country("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.get_country("Afghanistan").make_islamist_rule()
        app.deck.get(72).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.test_country("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.deck.get(72).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 3)


class Card73(LabyrinthTestCase):
    """Pirates"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(73).playable("Jihadist", app, False))
        app.get_country("Somalia").make_islamist_rule()
        self.assertTrue(app.deck.get(73).playable("Jihadist", app, False))
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(73).playable("Jihadist", app, False))
        app.get_country("Yemen").make_islamist_rule()
        self.assertTrue(app.deck.get(73).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(73).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(73).play_event("Jihadist", app)
        self.assertTrue("Pirates" in app.markers)
        app.end_turn()
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Somalia").make_islamist_rule()
        app.deck.get(73).play_event("Jihadist", app)
        app.end_turn()
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Yemen").make_islamist_rule()
        app.deck.get(73).play_event("Jihadist", app)
        app.end_turn()
        self.assertTrue(app.funding == 5)


class Card74(LabyrinthTestCase):
    """Schengen Visas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(74).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(74).puts_cell())

    def test_event_when_no_cells_on_map(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.cells = 15
        messages_before = len(app.history)
        app.deck.get(74).play_event("Jihadist", app)
        self.assert_new_messages(app, messages_before, ['Card played for Event.', 'No cells to travel.'])


class Card75(LabyrinthTestCase):
    """Schroeder & Chirac"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(75).playable("Jihadist", app, False))
        app.get_country("United States").make_soft()
        self.assertFalse(app.deck.get(75).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(75).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck.get(75).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Germany").is_soft())
        self.assertTrue(app.get_country("France").is_soft())
        self.assertTrue(app.prestige == 6)


class Card76(LabyrinthTestCase):
    """Abu Ghurayb"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(76).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_regime_change()
        self.assertFalse(app.deck.get(76).playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertTrue(app.deck.get(76).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(76).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.make_regime_change()
        iraq.sleeperCells = 1
        app.deck.get(76).play_event("Jihadist", app)
        self.assertTrue(app.prestige == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        iraq.make_regime_change()
        iraq.sleeperCells = 1
        app.test_country("Pakistan")
        app.test_country("Lebanon")
        app.get_country("Lebanon").make_ally()
        app.deck.get(76).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_neutral())
        self.assertTrue(app.prestige == 5)


class Card77(LabyrinthTestCase):
    """Al Jazeera"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(77).playable("Jihadist", app, False))
        app.test_country("Saudi Arabia")
        app.get_country("Saudi Arabia").troopCubes = 1
        self.assertTrue(app.deck.get(77).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(77).playable("Jihadist", app, False))
        app.test_country("Jordan")
        app.get_country("Jordan").troopCubes = 1
        self.assertTrue(app.deck.get(77).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(77).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.troopCubes = 1
        self.assertTrue(app.deck.get(77).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(77).playable("Jihadist", app, False))
        app.test_country("Gulf States")
        app.get_country("Gulf States").troopCubes = 1
        self.assertTrue(app.deck.get(77).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(77).playable("Jihadist", app, False))
        app.test_country("Yemen")
        app.get_country("Yemen").troopCubes = 1
        self.assertTrue(app.deck.get(77).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(77).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Yemen")
        app.get_country("Yemen").troopCubes = 1
        app.deck.get(77).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Yemen").is_adversary())


class Card78(LabyrinthTestCase):
    """Axis of Evil"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(78).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(78).puts_cell())

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
            app.get_country("United States").make_soft()
            app.deck.get(78).play_event("Jihadist", app)
            self.assertTrue(app.get_country("United States").is_hard())
            self.assertTrue(app.prestige != 7)


class Card79(LabyrinthTestCase):
    """Clean Operatives"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(79).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(79).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck.get(79).play_event("Jihadist", app)
        self.assertTrue(app.get_country("United States").sleeperCells == 2)


class Card80(LabyrinthTestCase):
    """FATA"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(80).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(80).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck.get(80).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue("FATA" in app.get_country("Pakistan").markers)


class Card81(LabyrinthTestCase):
    """Foreign Fighters"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(81).playable("Jihadist", app, False))
        app.test_country("Iraq")
        self.assertFalse(app.deck.get(81).playable("Jihadist", app, False))
        iraq.make_regime_change()
        self.assertTrue(app.deck.get(81).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(81).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.make_regime_change()
        app.deck.get(81).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 5)
        self.assertTrue(iraq.is_besieged())
        self.assertTrue(iraq.get_aid() == 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.make_regime_change()
        iraq.set_aid(1)
        app.deck.get(81).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 5)
        self.assertFalse(iraq.is_besieged())
        self.assertTrue(iraq.get_aid() == 0)


class Card82(LabyrinthTestCase):
    """Jihadist Videos"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(82).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(82).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck.get(82).play_event("Jihadist", app)


class Card83(LabyrinthTestCase):
    """Kashmir"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(83).playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck.get(83).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(83).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.test_country("Pakistan")
        app.deck.get(83).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").is_adversary())
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)


class Card84(LabyrinthTestCase):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(84).playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck.get(84).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(84).playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck.get(84).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(84).playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck.get(84).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(84).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Enhanced Measures")
        app.deck.get(84).play_event("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Renditions")
        app.deck.get(84).play_event("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Wiretapping")
        app.deck.get(84).play_event("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card85(LabyrinthTestCase):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(85).playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck.get(85).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(85).playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck.get(85).playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(85).playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck.get(85).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(85).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Enhanced Measures")
        app.deck.get(85).play_event("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Renditions")
        app.deck.get(85).play_event("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Wiretapping")
        app.deck.get(85).play_event("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card86(LabyrinthTestCase):
    """Lebanon War"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(86).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(86).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck.get(86).play_event("Jihadist", app)
        self.assertTrue(app.prestige == 6)


class Card87(LabyrinthTestCase):
    """Martyrdom Operation"""

    def test_playable_if_non_islamist_rule_country_has_cell(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        card87 = app.deck.get(87)

        # Invoke and check
        self.assertTrue(card87.playable("Jihadist", app, False))

    def test_not_playable_if_only_islamist_rule_country_has_cell(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.make_islamist_rule()
        iraq.sleeperCells = 1
        card87 = app.deck.get(87)

        # Invoke and check
        self.assertFalse(card87.playable("Jihadist", app, False))

    def test_not_playable_if_no_country_has_cell(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        iraq = app.get_country("Iraq")
        iraq.make_islamist_rule()
        card87 = app.deck.get(87)

        # Invoke and check
        self.assertFalse(card87.playable("Jihadist", app, False))

    def test_does_not_put_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(87).puts_cell())

    def test_event_places_two_plots_in_non_islamist_rule_country_with_cell(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        card87 = app.card(87)

        # Invoke
        card87.play_event("Jihadist", app)

        # Check
        self.assertEqual(iraq.activeCells, 0)
        self.assertEqual(iraq.sleeperCells, 0)
        self.assertEqual(iraq.cadre, 1)
        self.assertEqual(iraq.plots, 2)

    def test_event_prefers_us_to_other_countries(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        iraq = app.get_country("Iraq")
        us = app.get_country("United States")
        iraq.sleeperCells = 1
        us.sleeperCells = 1
        card87 = app.card(87)

        # Invoke
        card87.play_event("Jihadist", app)

        # Check
        # -- Iraq unaffected
        self.assertEqual(iraq.sleeperCells, 1)
        self.assertEqual(iraq.activeCells, 0)
        self.assertEqual(iraq.plots, 0)
        # -- US plotted in
        self.assertEqual(us.activeCells, 0)
        self.assertEqual(us.sleeperCells, 0)
        self.assertEqual(us.plots, 2)


class Card88(LabyrinthTestCase):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(88).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_islamist_rule()
        self.assertFalse(app.deck.get(88).playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertFalse(app.deck.get(88).playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertTrue(app.deck.get(88).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(88).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        app.deck.get(88).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 0)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.deck.get(88).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 1)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 0)
        self.assertTrue(app.get_country("United States").sleeperCells == 0)
        self.assertTrue(app.get_country("United States").activeCells == 0)
        self.assertTrue(app.get_country("United States").plots == 2)


class Card89(LabyrinthTestCase):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(89).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_islamist_rule()
        self.assertFalse(app.deck.get(89).playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertFalse(app.deck.get(89).playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertTrue(app.deck.get(89).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(89).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        app.deck.get(89).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 0)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.test_country("Iraq")
        iraq.sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.deck.get(89).play_event("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 1)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 0)
        self.assertTrue(app.get_country("United States").sleeperCells == 0)
        self.assertTrue(app.get_country("United States").activeCells == 0)
        self.assertTrue(app.get_country("United States").plots == 2)


class Card90(LabyrinthTestCase):
    """Quagmire"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(90).playable("Jihadist", app, False))
        app.prestige = 6
        self.assertFalse(app.deck.get(90).playable("Jihadist", app, False))
        app.test_country("Iraq")
        iraq.make_regime_change()
        self.assertFalse(app.deck.get(90).playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertTrue(app.deck.get(90).playable("Jihadist", app, False))
        app.prestige = 7
        self.assertFalse(app.deck.get(90).playable("Jihadist", app, False))
        app.prestige = 6
        iraq.remove_regime_change()
        self.assertFalse(app.deck.get(90).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(90).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Iraq")
        app.deck.get(90).play_event("Jihadist", app)
        self.assertTrue(app.get_country("United States").is_soft())


class Card91(LabyrinthTestCase):
    """Regional al-Qaeda"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        al_qaeda = app.deck.get(91)
        self.assertTrue(al_qaeda.playable("Jihadist", app, False))
        for country in app.find_countries(lambda c: c.is_muslim()):
            app.test_country(country.name)
        self.assertFalse(al_qaeda.playable("Jihadist", app, False))
        iraq.untest()
        self.assertFalse(al_qaeda.playable("Jihadist", app, False))
        lebanon = app.get_country("Lebanon")
        lebanon.untest()
        self.assertTrue(al_qaeda.playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(91).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        for country in app.find_countries(lambda c: c.is_muslim()):
            app.test_country(country.name)
        iraq = app.get_country("Iraq")
        iraq.untest()
        lebanon = app.get_country("Lebanon")
        lebanon.untest()
        app.deck.get(91).play_event("Jihadist", app)
        self.assertTrue(iraq.is_governed())
        self.assertTrue(iraq.is_aligned())
        self.assertTrue(iraq.sleeperCells == 1)
        self.assertTrue(lebanon.is_governed())
        self.assertTrue(lebanon.is_aligned())
        self.assertTrue(lebanon.sleeperCells == 1)


class Card92(LabyrinthTestCase):
    """Saddam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck.get(92).playable("Jihadist", app, False))
        app.test_country("Iraq")
        self.assertFalse(app.deck.get(92).playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertFalse(app.deck.get(92).playable("Jihadist", app, False))
        iraq.make_adversary()
        self.assertTrue(app.deck.get(92).playable("Jihadist", app, False))
        app.markers.append("Saddam Captured")
        self.assertFalse(app.deck.get(92).playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(92).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(92).play_event("Jihadist", app)
        self.assertTrue(app.funding == 9)         


class Card93(LabyrinthTestCase):
    """Taliban"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(93).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(93).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Afghanistan")
        app.test_country("Pakistan")
        app.deck.get(93).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").is_besieged())
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Afghanistan")
        app.test_country("Pakistan")
        app.get_country("Afghanistan").make_islamist_rule()
        app.deck.get(93).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").is_besieged())
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Afghanistan")
        app.test_country("Pakistan")
        app.get_country("Pakistan").make_islamist_rule()
        app.deck.get(93).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").is_besieged())
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.test_country("Afghanistan")
        app.test_country("Pakistan")
        app.deck.get(93).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").is_besieged())
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 0)         
        self.assertTrue(app.prestige == 6)


class Card94(LabyrinthTestCase):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck.get(94).playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck.get(94).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(94).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        iraq = app.get_country("Iraq")
        print "Choose Iraq"
        app.test_country("Iraq")
        iraq.make_fair()
        app.deck.get(94).play_event("Jihadist", app)
        self.assertTrue(iraq.is_poor())


class Card95(LabyrinthTestCase):
    """Wahhabism"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(95).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(95).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Saudi Arabia").make_poor()
        app.deck.get(95).play_event("Jihadist", app)
        self.assertTrue(app.funding == 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Saudi Arabia").make_fair()
        app.deck.get(95).play_event("Jihadist", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Saudi Arabia")
        app.get_country("Saudi Arabia").make_islamist_rule()
        app.deck.get(95).play_event("Jihadist", app)
        self.assertTrue(app.funding == 9)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Saudi Arabia")
        app.get_country("Saudi Arabia").make_islamist_rule()
        app.funding = 2
        app.deck.get(95).play_event("Jihadist", app)
        self.assertTrue(app.funding == 9)


class Card96(LabyrinthTestCase):
    """Danish Cartoons"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(96).playable("US", app, True))
        self.assertTrue(app.deck.get(96).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(96).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["s", "h"])
        iraq = app.get_country("Iraq")
        app.deck.get(96).play_event("US", app)
        self.assertTrue(app.get_country("Scandinavia").is_soft())
        app.test_country("Iraq")
        iraq.make_islamist_rule()
        app.deck.get(96).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Scandinavia").is_hard())


class Card97(LabyrinthTestCase):
    """Fatwa"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "n"])
        print "Say Yes"
        self.assertTrue(app.deck.get(97).playable("US", app, True))
        print "Say No"
        self.assertFalse(app.deck.get(97).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(97).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(97).play_event("US", app)
        app.deck.get(97).play_event("Jihadist", app)


class Card98(LabyrinthTestCase):
    """Gaza Withdrawl"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(98).playable("US", app, True))
        self.assertTrue(app.deck.get(98).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(98).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(98).play_event("US", app)
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(98).play_event("Jihadist", app)
        self.assertTrue(app.get_country("Israel").sleeperCells == 1)
        self.assertTrue(app.cells == 10)


class Card99(LabyrinthTestCase):
    """HAMAS Elected"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck.get(99).playable("US", app, True))
        self.assertTrue(app.deck.get(99).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck.get(99).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(99).play_event("US", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck.get(99).play_event("Jihadist", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)


if __name__ == "__main__":
    unittest.main()   