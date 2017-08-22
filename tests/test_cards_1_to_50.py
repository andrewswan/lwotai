import unittest

from mockito import when, mock

from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth
from lwotai.randomizer import Randomizer
from lwotai.governance import POOR
from postures.posture import SOFT, HARD


class Card01(LabyrinthTestCase):
    """Backlash"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(1).playable("US", app, True))
        app.get_country("Canada").plots = 1
        self.assertFalse(app.card(1).playable("US", app, True))
        app.get_country("Iraq").plots = 1
        self.assertTrue(app.card(1).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.backlashInPlay)
        app.card(1).playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.get_country("United States").plots = 1
        app.card(1).playEvent("US", app)
        self.assertFalse(app.backlashInPlay)
        app.get_country("Iraq").plots = 1
        app.card(1).playEvent("US", app)
        self.assertTrue(app.backlashInPlay)


class Card02(LabyrinthTestCase):
    """Biometrics"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(2).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse("Biometrics" in app.lapsing)
        app.card(2).playEvent("US", app)
        self.assertTrue("Biometrics" in app.lapsing)
        app.end_turn()
        self.assertFalse("Biometrics" in app.lapsing)

    def testTravelDestination(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.card(2).playEvent("US", app)
        dest = app.travel_destinations(1)
        self.assertTrue("Biometrics" in app.lapsing)
        self.assertEqual(dest, [])
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])

    def testTravelSource(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Gulf States").make_poor()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.card(2).playEvent("US", app)
        dest = app.travel_destinations(1)
        self.assertEqual(dest, [])
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.get_country("Sudan").make_islamist_rule()        
        app.get_country("Sudan").sleeperCells = 4    
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Iraq"])

    def testTravelToGood(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Gulf States").make_good()
        app.get_country("Gulf States").besieged = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.card(2).playEvent("US", app)
        dest = app.travel_destinations(1)
        self.assertEqual(dest, [])
        app.get_country("Iraq").sleeperCells = 1
        dest = app.travel_destinations(1)
        self.assertEqual(dest, ["Gulf States"])
        app.get_country("Sudan").make_islamist_rule()        
        app.get_country("Sudan").sleeperCells = 4    
        sources = app.travel_sources(dest, 1)
        self.assertEqual(sources, ["Iraq"])
        app.handle_travel(1)


class Card03(LabyrinthTestCase):
    """CTR"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(3).playable("US", app, True))
        app.toggle_us_posture()
        self.assertTrue(app.card(3).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.toggle_us_posture()
        self.assertFalse("CTR" in app.get_country("Russia").markers)
        self.assertFalse("CTR" in app.get_country("Central Asia").markers)
        app.get_country("Central Asia").make_adversary()
        app.card(3).playEvent("US", app)
        self.assertTrue("CTR" in app.get_country("Russia").markers)
        self.assertFalse("CTR" in app.get_country("Central Asia").markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.toggle_us_posture()
        self.assertFalse("CTR" in app.get_country("Russia").markers)
        self.assertFalse("CTR" in app.get_country("Central Asia").markers)
        app.get_country("Central Asia").make_neutral()
        app.card(3).playEvent("US", app)
        self.assertTrue("CTR" in app.get_country("Russia").markers)
        self.assertTrue("CTR" in app.get_country("Central Asia").markers)
        print app.get_country("Russia").summary()
        self.assertTrue("Markers: CTR" in app.get_country("Russia").summary())
        self.assertTrue("Markers: CTR" in app.get_country("Central Asia").summary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.toggle_us_posture()
        self.assertFalse("CTR" in app.get_country("Russia").markers)
        self.assertFalse("CTR" in app.get_country("Central Asia").markers)
        app.get_country("Central Asia").make_ally()
        app.card(3).playEvent("US", app)
        self.assertTrue("CTR" in app.get_country("Russia").markers)
        self.assertTrue("CTR" in app.get_country("Central Asia").markers)


class Card04(LabyrinthTestCase):
    """Moro Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(4).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.get_country("Philippines").get_posture() == None)
        self.assertTrue(app.funding == 5)
        app.card(4).playEvent("US", app)
        self.assertTrue("Moro Talks" in app.markers)
        self.assertTrue(app.get_country("Philippines").is_soft() or app.get_country("Philippines").is_hard())
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        self.assertTrue(app.get_country("Philippines").get_posture() == None)
        self.assertTrue(app.funding == 1)
        app.card(4).playEvent("US", app)
        self.assertTrue(app.get_country("Philippines").is_soft() or app.get_country("Philippines").is_hard())
        self.assertTrue(app.funding == 1)


class Card05(LabyrinthTestCase):
    """NEST"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(5).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse("NEST" in app.markers)
        app.card(5).playEvent("US", app)
        self.assertTrue("NEST" in app.markers)


class Card06and07(LabyrinthTestCase):
    """Sanctions"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(6).playable("US", app, True))
        self.assertFalse(app.card(7).playable("US", app, True))
        app.markers.append("Patriot Act")
        self.assertTrue(app.card(6).playable("US", app, True))
        self.assertTrue(app.card(7).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Patriot Act")
        app.card(6).playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Patriot Act")
        app.card(7).playEvent("US", app)
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 2
        app.markers.append("Patriot Act")
        app.card(6).playEvent("US", app)
        self.assertTrue(app.funding == 1)


class Card08and09and10(LabyrinthTestCase):
    """Special Forces"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(8).playable("US", app, True))
        self.assertFalse(app.card(9).playable("US", app, True))
        self.assertFalse(app.card(10).playable("US", app, True))
        app.get_country("Iran").sleeperCells = 1
        self.assertFalse(app.card(8).playable("US", app, True))
        self.assertFalse(app.card(9).playable("US", app, True))
        self.assertFalse(app.card(10).playable("US", app, True))
        app.get_country("Iran").troopCubes = 1
        self.assertTrue(app.card(8).playable("US", app, True))
        self.assertTrue(app.card(9).playable("US", app, True))
        self.assertTrue(app.card(10).playable("US", app, True))
        app.get_country("Iran").troopCubes = 0
        app.get_country("Iraq").troopCubes = 1
        self.assertTrue(app.card(8).playable("US", app, True))
        self.assertTrue(app.card(9).playable("US", app, True))
        self.assertTrue(app.card(10).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.list_countries_with_cell_and_adjacent_troops()
        app.get_country("Iran").sleeperCells = 1
        app.get_country("Iraq").troopCubes = 1
        app.list_countries_with_cell_and_adjacent_troops()


class Card11(LabyrinthTestCase):
    """Abbas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(11).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(11).playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.get_country("Israel").plots = 1
        app.resolve_plot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Syria")
        app.get_country("Syria").make_islamist_rule()
        app.card(11).playEvent("US", app)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.funding == 3)
        self.assertTrue("Abbas" in app.markers)
        app.get_country("Israel").plots = 1
        app.resolve_plot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.test_country("Lebanon")
        app.get_country("Lebanon").make_islamist_rule()
        app.card(11).playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.get_country("Israel").plots = 1
        app.resolve_plot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.troops = 4
        app.card(11).playEvent("US", app)
        self.assertTrue(app.prestige == 7)
        self.assertTrue(app.funding == 5)
        self.assertTrue("Abbas" in app.markers)
        app.get_country("Israel").plots = 1
        app.resolve_plot("Israel", 1, [1], [], [], [], [], False)
        self.assertFalse("Abbas" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.prestige = 12
        app.funding = 2
        app.card(11).playEvent("US", app)
        self.assertTrue(app.prestige == 12)
        self.assertTrue(app.funding == 1)


class Card12(LabyrinthTestCase):
    """Al-Azhar"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(12).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.get_country("Egypt").is_ungoverned())
        app.card(12).playEvent("US", app)
        self.assertTrue(app.get_country("Egypt").is_governed())
        self.assertTrue(app.funding == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.get_country("Egypt").is_ungoverned())
        app.get_country("Pakistan").make_islamist_rule()
        app.card(12).playEvent("US", app)
        self.assertTrue(app.get_country("Egypt").is_governed())
        self.assertTrue(app.funding == 3)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 2
        self.assertTrue(app.get_country("Egypt").is_ungoverned())
        app.card(12).playEvent("US", app)
        self.assertTrue(app.get_country("Egypt").is_governed())
        self.assertTrue(app.funding == 1)


class Card13(LabyrinthTestCase):
    """Anbar Awakening"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(13).playable("US", app, True))
        app.get_country("Iraq").troopCubes = 1
        self.assertTrue(app.card(13).playable("US", app, True))
        app.get_country("Iraq").troopCubes = 0
        app.get_country("Syria").troopCubes = 1
        self.assertTrue(app.card(13).playable("US", app, True))
        app.get_country("Syria").troopCubes = 0
        self.assertFalse(app.card(13).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").troopCubes = 1
        app.card(13).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").troopCubes = 1
        app.card(13).playEvent("US", app)
        self.assertTrue(app.get_country("Syria").aid > 0)
        self.assertTrue("Anbar Awakening" in app.markers)


class Card14(LabyrinthTestCase):
    """Covert Action"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(14).playable("US", app, True))
        app.get_country("Iraq").make_adversary()
        self.assertTrue(app.card(14).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.list_adversary_countries()
        app.get_country("Iraq").make_adversary()
        app.list_adversary_countries()


class Card15(LabyrinthTestCase):
    """Ethiopia Strikes"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(15).playable("US", app, True))
        app.get_country("Somalia").make_islamist_rule()
        self.assertTrue(app.card(15).playable("US", app, True))
        app.get_country("Somalia").make_poor()
        self.assertFalse(app.card(15).playable("US", app, True))
        app.get_country("Sudan").make_islamist_rule()
        self.assertTrue(app.card(15).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Somalia").make_islamist_rule()
        app.get_country("Somalia").make_adversary()
        app.card(15).playEvent("US", app)
        self.assertTrue(app.get_country("Somalia").is_poor())
        self.assertTrue(app.get_country("Somalia").is_neutral())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Sudan").make_islamist_rule()
        app.get_country("Sudan").make_adversary()
        app.card(15).playEvent("US", app)
        self.assertTrue(app.get_country("Sudan").is_poor())
        self.assertTrue(app.get_country("Sudan").is_neutral())


class Card16(LabyrinthTestCase):
    """Euro-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(16).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.execute_card_euro_islam(HARD)
        self.assertTrue(app.get_country("Benelux").is_hard())
        self.assertTrue(app.funding == 4)
        app.get_country("Iraq").make_islamist_rule()
        app.execute_card_euro_islam(SOFT)
        self.assertTrue(app.get_country("Benelux").is_soft())
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.execute_card_euro_islam(HARD)
        self.assertTrue(app.get_country("Benelux").is_hard())
        self.assertTrue(app.funding == 1)


class Card17(LabyrinthTestCase):
    """FSB"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(17).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.get_country("Central Asia").activeCells = 1
        app.get_country("Russia").activeCells = 1
        app.card(17).playEvent("US", app)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.get_country("Russia").activeCells = 1
        app.card(17).playEvent("US", app)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ['y'])
        app.get_country("Central Asia").sleeperCells = 1
        app.card(17).playEvent("US", app)


class Card18(LabyrinthTestCase):
    """Intel Community"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(18).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        history_before = len(app.history)
        app.card(18).playEvent("US", app)
        self.assert_new_messages(app, history_before, [
            'Card played for Event.',
            'Examine Jihadist hand. Do not change order of cards.',
            'Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment, regime_change,'
            ' withdraw, or war_of_ideas).',
            'You may now interrupt this action phase to play another card (Use the u command).'
        ])


class Card19(LabyrinthTestCase):
    """Kemalist Republic"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(19).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(19).playEvent("US", app)
        self.assertTrue(app.get_country("Turkey").is_fair())
        self.assertTrue(app.get_country("Turkey").is_ally())


class Card20(LabyrinthTestCase):
    """King Abdullah"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(20).playable("US", app, True))
        self.assertTrue(app.funding == 5)
        self.assertTrue(app.prestige == 7)

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(20).playEvent("US", app)
        self.assertTrue(app.get_country("Jordan").is_fair())
        self.assertTrue(app.get_country("Jordan").is_ally())
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.funding = 1
        app.prestige = 12
        app.card(20).playEvent("US", app)
        self.assertTrue(app.get_country("Jordan").is_fair())
        self.assertTrue(app.get_country("Jordan").is_ally())
        self.assertTrue(app.funding == 1)
        self.assertTrue(app.prestige == 12)


class Card21(LabyrinthTestCase):
    """Let's Roll"""

    event_owner = "US"

    def test_playable_if_plot_in_ally_country(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        potential_ally = app.get_country("Saudi Arabia")  # only Muslim countries can be allies
        potential_ally.plots = 1
        potential_ally.make_ally()
        self.assert_playable(app, True)
        potential_ally.make_neutral()
        self.assert_playable(app, False)

    def test_playable_if_plot_in_good_country(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        good_country = app.get_country("Canada")  # Canada is always Good
        good_country.plots = 1
        self.assert_playable(app, True)
        good_country.plots = 0
        self.assert_playable(app, False)

    def assert_playable(self, app, expected_value):
        """Asserts that this card is (or is not) playable for the given game state"""
        playable = app.card(21).playable(self.event_owner, app, True)
        self.assertEqual(playable, expected_value)

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").plots = 1
        app.get_country("Spain").make_soft()
        app.execute_card_lets_roll("Canada", "Spain", HARD)
        self.assertTrue(app.get_country("Canada").plots == 0)
        self.assertTrue(app.get_country("Spain").is_hard())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Saudi Arabi", "Spain", "h"])
        app.get_country("Spain").make_soft()
        app.get_country("Saudi Arabia").make_good()
        app.get_country("Saudi Arabia").plots = 1
        app.card(21).playEvent(self.event_owner, app)
        self.assertTrue(app.get_country("Spain").is_hard())
        self.assertTrue(app.get_country("Saudi Arabia").plots == 0)


class Card22(LabyrinthTestCase):
    """Mossad and Shin Bet"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(22).playable("US", app, True))
        app.get_country("Israel").sleeperCells = 1
        self.assertTrue(app.card(22).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(22).playable("US", app, True))
        app.get_country("Jordan").sleeperCells = 1
        self.assertTrue(app.card(22).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(22).playable("US", app, True))
        app.get_country("Lebanon").sleeperCells = 1
        self.assertTrue(app.card(22).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Israel").sleeperCells = 1
        app.get_country("Israel").activeCells = 4
        app.get_country("Jordan").activeCells = 3
        app.get_country("Lebanon").sleeperCells = 2
        app.get_country("Iraq").sleeperCells = 2
        app.card(22).playEvent("US", app)
        self.assertTrue(app.get_country("Israel").sleeperCells == 0)
        self.assertTrue(app.get_country("Israel").activeCells == 0)
        self.assertTrue(app.get_country("Jordan").sleeperCells == 0)
        self.assertTrue(app.get_country("Jordan").activeCells == 0)
        self.assertTrue(app.get_country("Lebanon").sleeperCells == 0)
        self.assertTrue(app.get_country("Lebanon").activeCells == 0)
        self.assertTrue(app.get_country("Iraq").sleeperCells == 2)


class Card23and24and25(LabyrinthTestCase):
    """Predator"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(23).playable("US", app, True))
        app.get_country("Israel").sleeperCells = 1
        self.assertFalse(app.card(23).playable("US", app, True))
        app.get_country("Iran").sleeperCells = 1
        self.assertFalse(app.card(23).playable("US", app, True))
        app.get_country("Jordan").sleeperCells = 1
        self.assertTrue(app.card(23).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(24).playable("US", app, True))
        app.get_country("Israel").sleeperCells = 1
        self.assertFalse(app.card(24).playable("US", app, True))
        app.get_country("Iran").sleeperCells = 1
        self.assertFalse(app.card(24).playable("US", app, True))
        app.get_country("Jordan").sleeperCells = 1
        self.assertTrue(app.card(24).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(25).playable("US", app, True))
        app.get_country("Israel").sleeperCells = 1
        self.assertFalse(app.card(25).playable("US", app, True))
        app.get_country("Iran").sleeperCells = 1
        self.assertFalse(app.card(25).playable("US", app, True))
        app.get_country("Jordan").sleeperCells = 1
        self.assertTrue(app.card(25).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.get_country("Iraq").sleeperCells = 2
        app.card(25).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").sleeperCells == 1)


class Card26(LabyrinthTestCase):
    """Quartet"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(26).playable("US", app, True))
        app.markers.append("Abbas")
        self.assertTrue(app.card(26).playable("US", app, True))
        app.troops = 4
        self.assertFalse(app.card(26).playable("US", app, True))
        app.troops = 5
        self.assertTrue(app.card(26).playable("US", app, True))
        app.get_country("Egypt").make_islamist_rule()
        self.assertFalse(app.card(26).playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Abbas")
        app.card(26).playEvent("US", app)
        self.assertTrue(app.prestige == 9)
        self.assertTrue(app.funding == 2)


class Card27(LabyrinthTestCase):
    """Saddam Captured"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(27).playable("US", app, True))
        app.get_country("Iraq").troopCubes = 1
        self.assertTrue(app.card(27).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").troopCubes = 1
        app.card(27).playEvent("US", app)
        self.assertTrue("Saddam Captured" in app.markers)
        self.assertTrue(app.get_country("Iraq").aid == 1)


class Card28(LabyrinthTestCase):
    """Sharia"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(28).playable("US", app, True))
        app.get_country("Iraq").besieged = 1
        self.assertTrue(app.card(28).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").besieged = 1
        app.card(28).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").besieged == 0)


class Card29(LabyrinthTestCase):
    """Tony Blair"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(29).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").make_hard()

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").make_hard()
        app.execute_non_muslim_woi("Spain", 4)
        self.assertTrue(app.get_country("Spain").is_soft())
        app.execute_non_muslim_woi("France", 5)
        self.assertTrue(app.get_country("France").is_hard())


class Card30(LabyrinthTestCase):
    """UN Nation Building"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(30).playable("US", app, True))
        app.get_country("Iraq").regimeChange = 1
        self.assertTrue(app.card(30).playable("US", app, True))
        app.markers.append("Vieira de Mello Slain")
        self.assertFalse(app.card(30).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["6"])
        app.get_country("United States").make_hard()
        app.get_country("Spain").make_soft()
        app.get_country("France").make_soft()
        app.get_country("Germany").make_soft()
        app.get_country("Canada").make_soft()
        # app.get_country("Iraq").regimeChange = 1
        app.get_country("Pakistan").regimeChange = 1
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_ally()
        app.card(30).playEvent("US", app)
        self.assertTrue(app.get_country("Pakistan").aid == 1)
        self.assertTrue(app.get_country("Pakistan").is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq", "6"])
        app.get_country("United States").make_hard()
        app.get_country("Spain").make_soft()
        app.get_country("France").make_soft()
        app.get_country("Germany").make_soft()
        app.get_country("Canada").make_soft()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_ally()
        app.get_country("Pakistan").regimeChange = 1
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_ally()
        app.card(30).playEvent("US", app)
        self.assertTrue(app.get_country("Pakistan").aid == 0)
        self.assertTrue(app.get_country("Pakistan").is_poor())
        self.assertTrue(app.get_country("Iraq").aid == 1)
        self.assertTrue(app.get_country("Iraq").is_fair())


class Card31(LabyrinthTestCase):
    """Wiretapping"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(31).playable("US", app, True))
        app.get_country("United States").sleeperCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").activeCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").cadre = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").plots = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(31).playable("US", app, True))
        app.get_country("United Kingdom").sleeperCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United Kingdom").activeCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United Kingdom").cadre = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United Kingdom").plots = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(31).playable("US", app, True))
        app.get_country("Canada").sleeperCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").activeCells = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").cadre = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").plots = 1
        self.assertTrue(app.card(31).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Canada").plots = 1
        app.markers.append("Leak-Wiretapping")
        self.assertFalse(app.card(31).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 1
        app.get_country("United States").activeCells = 1
        app.get_country("United States").cadre = 1
        app.get_country("United States").plots = 1
        app.get_country("United Kingdom").sleeperCells = 1
        app.get_country("United Kingdom").activeCells = 1
        app.get_country("United Kingdom").cadre = 1
        app.get_country("United Kingdom").plots = 1
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Canada").activeCells = 1
        app.get_country("Canada").cadre = 1
        app.get_country("Canada").plots = 1
        app.card(31).playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.get_country("United States").sleeperCells == 0)
        self.assertTrue(app.get_country("United States").activeCells == 0)
        self.assertTrue(app.get_country("United States").cadre == 0)
        self.assertTrue(app.get_country("United States").plots == 0)
        self.assertTrue(app.get_country("United Kingdom").sleeperCells == 0)
        self.assertTrue(app.get_country("United Kingdom").activeCells == 0)
        self.assertTrue(app.get_country("United Kingdom").cadre == 0)
        self.assertTrue(app.get_country("United Kingdom").plots == 0)
        self.assertTrue(app.get_country("Canada").sleeperCells == 0)
        self.assertTrue(app.get_country("Canada").activeCells == 0)
        self.assertTrue(app.get_country("Canada").cadre == 0)
        self.assertTrue(app.get_country("Canada").plots == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").sleeperCells = 1
        app.get_country("United States").activeCells = 1
        app.get_country("United States").cadre = 1
        app.get_country("United States").plots = 1
        app.get_country("Canada").sleeperCells = 1
        app.get_country("Canada").activeCells = 1
        app.get_country("Canada").cadre = 1
        app.get_country("Canada").plots = 1
        app.card(31).playEvent("US", app)
        self.assertTrue("Wiretapping" in app.markers)
        self.assertTrue(app.get_country("United States").sleeperCells == 0)
        self.assertTrue(app.get_country("United States").activeCells == 0)
        self.assertTrue(app.get_country("United States").cadre == 0)
        self.assertTrue(app.get_country("United States").plots == 0)
        self.assertTrue(app.get_country("United Kingdom").sleeperCells == 0)
        self.assertTrue(app.get_country("United Kingdom").activeCells == 0)
        self.assertTrue(app.get_country("United Kingdom").cadre == 0)
        self.assertTrue(app.get_country("United Kingdom").plots == 0)
        self.assertTrue(app.get_country("Canada").sleeperCells == 0)
        self.assertTrue(app.get_country("Canada").activeCells == 0)
        self.assertTrue(app.get_country("Canada").cadre == 0)
        self.assertTrue(app.get_country("Canada").plots == 0)


class Card32(LabyrinthTestCase):
    """Back Channel"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "n"])
        app.get_country("United States").make_hard()
        self.assertFalse(app.card(32).playable("US", app, True))
        app.get_country("United States").make_soft()
        self.assertFalse(app.card(32).playable("US", app, True))

        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_adversary()
        app.get_country("Pakistan").make_adversary()
        print "Say yes"
        self.assertTrue(app.card(32).playable("US", app, True))
        print "Say no"
        self.assertFalse(app.card(32).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "y", "Pakistan"])
        app.get_country("United States").make_soft()
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_adversary()
        app.get_country("Pakistan").make_islamist_rule()
        app.get_country("Pakistan").make_adversary()
        self.assertTrue(app.card(32).playable("US", app, True))
        aid_before = app.get_country("Pakistan").aid
        app.card(32).playEvent("US", app)
        aid_after = app.get_country("Pakistan").aid
        self.assertTrue(app.get_country("Iraq").is_adversary())
        self.assertTrue(app.get_country("Pakistan").is_neutral())
        self.assertEqual(aid_after, aid_before + 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "n"])
        app.get_country("United States").make_soft()
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_adversary()
        app.get_country("Pakistan").make_islamist_rule()
        app.get_country("Pakistan").make_adversary()
        self.assertFalse(app.card(32).playable("US", app, True))
        app.card(32).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").is_adversary())
        self.assertTrue(app.get_country("Pakistan").is_adversary())


class Card33(LabyrinthTestCase):
    """Benazir Bhutto"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(33).playable("US", app, True))
        app.markers.append("Bhutto Shot")
        self.assertFalse(app.card(33).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(33).playable("US", app, True))
        app.get_country("Pakistan").make_islamist_rule()
        self.assertFalse(app.card(33).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Afghanistan").make_islamist_rule()
        self.assertFalse(app.card(33).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("India").make_islamist_rule()
        self.assertFalse(app.card(33).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Gulf States").make_islamist_rule()
        self.assertFalse(app.card(33).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Indonesia/Malaysia").make_islamist_rule()
        self.assertFalse(app.card(33).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Pakistan").make_poor()
        app.card(33).playEvent("US", app)
        self.assertTrue(app.get_country("Pakistan").is_fair())

        # no jihad in Pakistan
        app = Labyrinth(1, 1, self.set_up_test_scenario_3)
        app.get_country("Gulf States").activeCells = 0
        app.get_country("Gulf States").sleeperCells = 0
        app.get_country("Pakistan").activeCells = 0
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), False)
        app.get_country("Pakistan").make_fair()
        app.get_country("Pakistan").activeCells = 1
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), [("Pakistan", 1)])
        app.card(33).playEvent("US", app)
        self.assertEqual(app.minor_jihad_in_good_fair_choice(1), False)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertEqual(app.major_jihad_possible(3), [])
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").activeCells = 5
        self.assertEqual(app.major_jihad_possible(3), ["Pakistan"])
        app.card(33).playEvent("US", app)
        self.assertEqual(app.major_jihad_possible(3), [])

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").activeCells = 5
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").activeCells = 5
        self.assertEqual(app.major_jihad_choice(3), "Pakistan")
        app.card(33).playEvent("US", app)
        self.assertEqual(app.major_jihad_possible(3), ["Iraq"])


class Card34(LabyrinthTestCase):
    """Enhanced Measures"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(34).playable("US", app, True))
        app.get_country("Iraq").cadre = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_neutral()
        app.get_country("Iraq").troopCubes = 2
        self.assertTrue(app.card(34).playable("US", app, True))
        app.markers.append("Leak-Enhanced Measures")
        self.assertFalse(app.card(34).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("United States").make_soft()
        app.get_country("Iraq").cadre = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_neutral()
        app.get_country("Iraq").troopCubes = 2
        self.assertFalse(app.card(34).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.get_country("Iraq").cadre = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_neutral()
        app.get_country("Iraq").troopCubes = 2
        app.get_country("Pakistan").cadre = 1
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_neutral()
        app.get_country("Pakistan").troopCubes = 2
        app.card(34).playEvent("US", app)
        self.assertTrue("Enhanced Measures" in app.markers)
        self.assertTrue(app.get_country("Pakistan").cadre == 1)
        self.assertTrue(app.get_country("Iraq").cadre == 0)


class Card35(LabyrinthTestCase):
    """Hajib"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(35).playable("US", app, True))
        app.get_country("Iraq").make_islamist_rule()
        self.assertFalse(app.card(35).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["h"])
        app.card(35).playEvent("US", app)
        self.assertTrue(app.get_country("Turkey").governance_is_better_than(POOR))
        self.assertTrue(app.get_country("Turkey").is_governed())
        self.assertTrue(app.get_country("Turkey").is_aligned())
        print "Say Hard"
        self.assertTrue(app.get_country("France").is_hard())
        self.assertTrue(app.funding == 3)


class Card36(LabyrinthTestCase):
    """Indo-Pakistani Talks"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(36).playable("US", app, True))
        app.get_country("Pakistan").make_islamist_rule()
        self.assertFalse(app.card(36).playable("US", app, True))
        app.get_country("Pakistan").make_poor()
        self.assertFalse(app.card(36).playable("US", app, True))
        app.get_country("Pakistan").make_fair()
        self.assertTrue(app.card(36).playable("US", app, True))
        app.get_country("Pakistan").make_good()
        self.assertTrue(app.card(36).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["s", "1"])
        app.get_country("Pakistan").make_fair()
        app.get_country("Pakistan").make_adversary()
        app.card(36).playEvent("US", app)
        self.assertTrue(app.get_country("Pakistan").is_ally())
        self.assertTrue("Indo-Pakistani Talks" in app.markers)
        self.assertTrue(app.get_country("India").is_soft())
        app.get_country("India").plots = 1
        app.resolve_plots()
        self.assertFalse("Indo-Pakistani Talks" in app.markers)


class Card37(LabyrinthTestCase):
    """Iraqi WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(37).playable("US", app, True))
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_adversary()
        self.assertTrue(app.card(37).playable("US", app, True))
        app.get_country("United States").make_soft()
        self.assertFalse(app.card(37).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(37).playEvent("US", app)
        self.assertTrue("Iraqi WMD" in app.markers)
        app.handle_regime_change("Iraq", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Iraqi WMD" in app.markers)


class Card38(LabyrinthTestCase):
    """Libyan Desl"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(38).playable("US", app, True))
        app.get_country("Libya").make_poor()
        self.assertFalse(app.card(38).playable("US", app, True))
        app.get_country("Iraq").make_ally()
        self.assertTrue(app.card(38).playable("US", app, True))
        app.get_country("Iraq").make_neutral()
        self.assertFalse(app.card(38).playable("US", app, True))
        app.get_country("Syria").make_ally()
        self.assertTrue(app.card(38).playable("US", app, True))
        app.get_country("Libya").make_fair()
        self.assertFalse(app.card(38).playable("US", app, True))
        app.get_country("Libya").make_islamist_rule()
        self.assertFalse(app.card(38).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["france", "s", "Spain", "h"])
        app.get_country("Libya").make_poor()
        app.get_country("Iraq").make_ally()
        app.card(38).playEvent("US", app)
        self.assertTrue("Libyan Deal" in app.markers)
        self.assertTrue(app.prestige == 8)
        self.assertTrue(app.get_country("France").is_soft())
        self.assertTrue(app.get_country("Spain").is_hard())


class Card39(LabyrinthTestCase):
    """Libyan WMD"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(39).playable("US", app, True))
        app.get_country("Libya").make_poor()
        app.get_country("Libya").make_adversary()
        self.assertTrue(app.card(39).playable("US", app, True))
        app.get_country("United States").make_soft()
        self.assertFalse(app.card(39).playable("US", app, True))
        app.get_country("United States").make_hard()
        self.assertTrue(app.card(39).playable("US", app, True))
        app.markers.append("Libyan Deal")
        self.assertFalse(app.card(39).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(39).playEvent("US", app)
        self.assertTrue("Libyan WMD" in app.markers)
        app.handle_regime_change("Libya", "track", 6, 4, (4, 4, 4))
        self.assertFalse("Libyan WMD" in app.markers)


class Card40(LabyrinthTestCase):
    """Mass Turnout"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(40).playable("US", app, True))
        app.get_country("Libya").make_poor()
        app.get_country("Libya").make_adversary()
        self.assertFalse(app.card(40).playable("US", app, True))
        app.get_country("Libya").regimeChange = 1
        self.assertTrue(app.card(40).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Libya").make_poor()
        app.get_country("Libya").make_adversary()
        app.get_country("Libya").regimeChange = 1
        app.card(40).playEvent("US", app)
        self.assertTrue(app.get_country("Libya").is_fair())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Libya").make_fair()
        app.get_country("Libya").make_adversary()
        app.get_country("Libya").regimeChange = 1
        app.get_country("Libya").aid = 1
        app.card(40).playEvent("US", app)
        self.assertTrue(app.get_country("Libya").is_good())
        self.assertTrue(app.get_country("Libya").regimeChange == 0)
        self.assertTrue(app.get_country("Libya").aid == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.get_country("Libya").make_fair()
        app.get_country("Libya").make_adversary()
        app.get_country("Libya").regimeChange = 1
        app.get_country("Libya").aid = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_adversary()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").aid = 1
        app.card(40).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").is_good())
        self.assertTrue(app.get_country("Iraq").regimeChange == 0)
        self.assertTrue(app.get_country("Iraq").aid == 0)


class Card41(LabyrinthTestCase):
    """NATO"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(41).playable("US", app, True))
        app.get_country("Libya").make_poor()
        app.get_country("Libya").make_ally()
        app.get_country("Libya").regimeChange = 1
        self.assertTrue(app.card(41).playable("US", app, True))
        app.get_country("Canada").make_soft()
        self.assertTrue(app.card(41).playable("US", app, True))
        app.get_country("Spain").make_soft()
        self.assertFalse(app.card(41).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Libya", "track", "3"])
        app.get_country("Libya").make_poor()
        app.get_country("Libya").make_ally()
        app.get_country("Libya").regimeChange = 1
        app.get_country("Libya").change_troops(2)
        app.card(41).playEvent("US", app)
        self.assertTrue(app.get_country("Libya").aid == 1)
        self.assertTrue(app.get_country("Libya").troops() == 4)
        self.assertTrue("NATO" in app.get_country("Libya").markers)

        app.get_country("Libya").regimeChange = 0
        print "Deploy 3 from Libya to track:"
        app.deploy_troops()
        self.assertTrue(app.get_country("Libya").troops() == 0)
        self.assertTrue("NATO" not in app.get_country("Libya").markers)        

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.get_country("Libya").make_fair()
        app.get_country("Libya").make_adversary()
        app.get_country("Libya").regimeChange = 1
        app.get_country("Libya").aid = 1
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_adversary()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").aid = 0
        app.card(41).playEvent("US", app)
        self.assertEqual(app.get_country("Iraq").aid, 1)
        self.assertTrue(app.get_country("Iraq").troops() == 2)
        self.assertTrue("NATO" in app.get_country("Iraq").markers)


class Card42(LabyrinthTestCase):
    """Pakistani Offensive"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(42).playable("US", app, True))
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_ally()
        self.assertFalse(app.card(42).playable("US", app, True))
        app.get_country("Pakistan").markers.append("FATA")
        self.assertTrue(app.card(42).playable("US", app, True))
        app.get_country("Pakistan").make_neutral()
        self.assertFalse(app.card(42).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_ally()
        app.get_country("Pakistan").markers.append("FATA")
        app.card(42).playEvent("US", app)
        self.assertTrue("FATA" not in app.get_country("Pakistan").markers)


class Card43(LabyrinthTestCase):
    """Patriot Act"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(43).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.is_adjacent("United States", "Canada"))
        self.assertTrue(app.is_adjacent("United States", "United Kingdom"))
        self.assertTrue(app.is_adjacent("United States", "Philippines"))
        for country in app.get_countries():
            if country.schengen:
                self.assertTrue(app.is_adjacent("United States", country.name))
        app.card(43).playEvent("US", app)
        self.assertTrue("Patriot Act" in app.markers)
        self.assertTrue(app.is_adjacent("United States", "Canada"))
        self.assertFalse(app.is_adjacent("United States", "United Kingdom"))
        self.assertFalse(app.is_adjacent("United States", "Philippines"))
        for country in app.get_countries():
            if country.schengen:
                self.assertFalse(app.is_adjacent("United States", country.name))


class Card44(LabyrinthTestCase):
    """Renditions"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(44).playable("US", app, True))
        app.get_country("United States").make_soft()
        self.assertFalse(app.card(44).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(44).playable("US", app, True))
        app.markers.append("Leak-Renditions")
        self.assertFalse(app.card(44).playable("US", app, True))

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        app.get_country("Iraq").cadre = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_neutral()
        app.get_country("Iraq").troopCubes = 2
        app.get_country("Pakistan").cadre = 1
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_neutral()
        app.get_country("Pakistan").troopCubes = 2
        app.card(44).playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.get_country("Iraq").cadre == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Pakistan"])
        app.get_country("Iraq").cadre = 1
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_neutral()
        app.get_country("Iraq").troopCubes = 2
        app.get_country("Pakistan").cadre = 1
        app.get_country("Pakistan").sleeperCells = 2
        app.get_country("Pakistan").make_poor()
        app.get_country("Pakistan").make_neutral()
        app.get_country("Pakistan").troopCubes = 2
        app.card(44).playEvent("US", app)
        self.assertTrue("Renditions" in app.markers)
        self.assertTrue(app.get_country("Pakistan").cadre == 1)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 0)


class Card45(LabyrinthTestCase):
    """Safer Now"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(45).playable("US", app, True))
        app.get_country("Iraq").make_islamist_rule()
        app.get_country("Iraq").make_adversary()
        self.assertFalse(app.card(45).playable("US", app, True))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(45).playable("US", app, True))
        app.get_country("Iraq").make_good()
        app.get_country("Iraq").make_ally()
        self.assertTrue(app.card(45).playable("US", app, True))
        app.get_country("Iraq").cadre = 1
        self.assertTrue(app.card(45).playable("US", app, True))
        app.get_country("Iraq").plots = 1
        self.assertFalse(app.card(45).playable("US", app, True))
        app.get_country("Iraq").plots = 0
        app.get_country("Iraq").cadre = 0
        app.get_country("Iraq").sleeperCells = 1
        self.assertFalse(app.card(45).playable("US", app, True))
        app.get_country("Iraq").sleeperCells = 0
        app.get_country("Iraq").activeCells = 1
        self.assertFalse(app.card(45).playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["4", "Spain", "h"])
        print "Enter 4 for posture role, Spain and Hard"
        app.card(45).playEvent("US", app)
        self.assertTrue(app.get_country("United States").is_soft())
        self.assertTrue(app.prestige == 10)
        self.assertTrue(app.get_country("Spain").is_hard())


class Card46(LabyrinthTestCase):
    """Sistani"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").regimeChange = 1
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Iraq").cadre = 1
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Iraq").sleeperCells = 1
        self.assertTrue(app.card(46).playable("US", app, True))
        app.get_country("Iraq").sleeperCells = 0
        app.get_country("Iraq").activeCells = 1
        self.assertTrue(app.card(46).playable("US", app, True))    

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Syria").make_fair()
        app.get_country("Syria").make_ally()
        app.get_country("Syria").regimeChange = 1
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Syria").cadre = 1
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Syria").sleeperCells = 1
        self.assertFalse(app.card(46).playable("US", app, True))
        app.get_country("Syria").sleeperCells = 0
        app.get_country("Syria").activeCells = 1
        self.assertFalse(app.card(46).playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_poor()
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").sleeperCells = 1
        app.card(46).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").is_fair())
        app.card(46).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").is_good())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Syria").make_fair()
        app.get_country("Syria").make_ally()
        app.get_country("Syria").regimeChange = 1
        app.get_country("Syria").sleeperCells = 1
        app.card(46).playEvent("US", app)
        self.assertTrue(app.get_country("Iraq").is_good())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Lebanon"])
        app.get_country("Iraq").make_fair()
        app.get_country("Iraq").make_ally()
        app.get_country("Iraq").regimeChange = 1
        app.get_country("Iraq").sleeperCells = 1
        app.get_country("Lebanon").make_fair()
        app.get_country("Lebanon").make_ally()
        app.get_country("Lebanon").regimeChange = 1
        app.get_country("Lebanon").sleeperCells = 1
        print "Choose Lebanon"
        app.card(46).playEvent("US", app)
        self.assertTrue(app.get_country("Lebanon").is_good())


class Card47(LabyrinthTestCase):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(47).playable("US", app, True))    

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(47).playEvent("US", app)
        self.assertTrue("The door of Itjihad was closed" in app.lapsing)
        self.assertFalse(app.card(66).playable("Jihadist", app, False))
        self.assertFalse(app.card(114).playable("Jihadist", app, False))
        app.end_turn()
        self.assertFalse("The door of Itjihad was closed" in app.lapsing)
        self.assertTrue(app.card(66).playable("Jihadist", app, False))
        self.assertTrue(app.card(114).playable("Jihadist", app, False))


class Card48(LabyrinthTestCase):
    """Adam Gadahn"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        app.cells = 0
        self.assertFalse(app.card(48).playable("Jihadist", app, False))
        app.cells = 9
        print "Say No"
        self.assertFalse(app.card(48).playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.card(48).playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(48).puts_cell())

    def test_event(self):
        # Set up
        mock_randomizer = mock(Randomizer())
        when(mock_randomizer).roll_d6(3).thenReturn([1, 3, 2])
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["120"], randomizer=mock_randomizer)
        self.assertTrue(app.num_cells_available() > 0)
        self.assertCells(app, "United States", 0)

        # Invoke
        app.card(48).playEvent("Jihadist", app)

        # Check
        self.assertCells(app, "United States", 2)


class Card49(LabyrinthTestCase):
    """Al-Ittihad al-Islami"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(49).playable("Jihadist", app, False))    
        app.cells = 1
        self.assertTrue(app.card(49).playable("Jihadist", app, False))    
        app.cells = 0
        self.assertTrue(app.card(49).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(49).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(49).playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Somalia").sleeperCells == 1)


class Card50(LabyrinthTestCase):
    """Ansar al-Islam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.card(50).playable("Jihadist", app, False))    
        app.get_country("Iraq").make_good()
        self.assertFalse(app.card(50).playable("Jihadist", app, False))    
        app.get_country("Iraq").make_fair()
        self.assertTrue(app.card(50).playable("Jihadist", app, False))    
        app.get_country("Iraq").make_poor()
        self.assertTrue(app.card(50).playable("Jihadist", app, False))    
        app.get_country("Iraq").make_islamist_rule()
        self.assertTrue(app.card(50).playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.card(50).puts_cell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.card(50).playEvent("Jihadist", app)
        app.get_country("Iraq").make_fair()
        self.assertTrue(app.get_country("Iraq").sleeperCells == 1 or app.get_country("Iran").sleeperCells == 1)


if __name__ == "__main__":
    unittest.main()   