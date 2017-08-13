import unittest

from labyrinth_test_case import LabyrinthTestCase
from lwotai.labyrinth import Labyrinth


class Card51(LabyrinthTestCase):
    """FREs"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["51"].playable("Jihadist", app, False))    
        iraq.changeTroops(1)
        self.assertTrue(app.deck["51"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["51"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        iraq = app.get_country("Iraq")
        iraq.changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.markers.append("Saddam Captured")
        app.testCountry("Iraq")
        iraq.changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.cells = 3
        app.testCountry("Iraq")
        iraq.changeTroops(1)
        app.deck["51"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 3)


class Card52(LabyrinthTestCase):
    """IEDs"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["52"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        iraq.sleeperCells = 1
        self.assertTrue(app.deck["52"].playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["52"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["52"].playEvent("Jihadist", app)


class Card53(LabyrinthTestCase):
    """Madrassas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["53"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["53"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["53"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario, ["1"])
        app.deck["53"].playEvent("Jihadist", app)


class Card54(LabyrinthTestCase):
    """Moqtada al-Sadr"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["54"].playable("Jihadist", app, False))
        iraq.changeTroops(1)
        self.assertTrue(app.deck["54"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["54"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.deck["54"].playEvent("Jihadist", app)
        self.assertTrue("Sadr" in iraq.markers)


class Card55(LabyrinthTestCase):
    """Uyghur Jihad"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["55"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["55"].putsCell())

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
            app.deck["55"].playEvent("Jihadist", app)
            self.assertTrue(app.get_country("China").posture != "")
            if app.get_country("China").posture == "Soft":
                self.assertTrue(app.get_country("China").sleeperCells == 1)
            else:
                self.assertTrue(app.get_country("Central Asia").is_governed())
                self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)


class Card56(LabyrinthTestCase):
    """Vieira de Mello Slain"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["56"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        self.assertFalse(app.deck["56"].playable("Jihadist", app, False))    
        iraq.sleeperCells = 1
        self.assertTrue(app.deck["56"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["56"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["56"].playEvent("Jihadist", app)
        self.assertTrue("Vieira de Mello Slain" in app.markers)
        self.assertTrue(app.prestige == 6)


class Card57(LabyrinthTestCase):
    """Abu Sayyaf"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["57"].playable("Jihadist", app, False))    
        app.markers.append("Moro Talks")
        self.assertFalse(app.deck["57"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["57"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["57"].playEvent("Jihadist", app)
        self.assertTrue("Abu Sayyaf" in app.markers)
        self.assertTrue(app.get_country("Philippines").is_governed())
        self.assertTrue(app.get_country("Philippines").sleeperCells == 1)
        app.get_country("Philippines").sleeperCells = 3
        app.placePlots("Philippines", 0, [1, 5, 1])
        self.assertTrue(app.prestige == 5)


class Card58(LabyrinthTestCase):
    """Al-Anbar"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["58"].playable("Jihadist", app, False))    
        app.markers.append("Anbar Awakening")
        self.assertFalse(app.deck["58"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["58"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        self.assertTrue(iraq.sleeperCells == 1)
        app.testCountry("Iraq")
        iraq.sleeperCells = 3
        iraq.troopCubes = 3
        app.handle_disrupt("Iraq")
        self.assertTrue(iraq.sleeperCells == 2)
        self.assertTrue(iraq.activeCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Syria")
        app.get_country("Syria").sleeperCells = 3
        app.get_country("Syria").troopCubes = 3
        app.handle_disrupt("Syria")
        self.assertTrue(app.get_country("Syria").sleeperCells == 2)
        self.assertTrue(app.get_country("Syria").activeCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 3
        app.get_country("Afghanistan").troopCubes = 3
        app.handle_disrupt("Afghanistan")
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").activeCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["58"].playEvent("Jihadist", app)
        self.assertTrue("Al-Anbar" in app.markers)
        app.testCountry("Iraq")
        iraq.cadre = 1
        iraq.troopCubes = 3
        app.handle_disrupt("Iraq")
        self.assertTrue(iraq.cadre == 1)


class Card59(LabyrinthTestCase):
    """Amerithrax"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["59"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["59"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["59"].playEvent("Jihadist", app)


class Card60(LabyrinthTestCase):
    """Bhutto Shot"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["60"].playable("Jihadist", app, False))
        app.get_country("Pakistan").sleeperCells = 1
        self.assertTrue(app.deck["60"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["60"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["60"].playEvent("Jihadist", app)
        self.assertTrue("Bhutto Shot" in app.markers)


class Card61(LabyrinthTestCase):
    """Detainee Release"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.lapsing.append("GTMO")
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.markers.append("Renditions")
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["61"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["61"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["61"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        app.deck["61"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 1)


class Card62(LabyrinthTestCase):
    """Ex-KGB"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["62"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["62"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Russia").markers.append("CTR")
        app.get_country("Caucasus").posture = "Hard"
        app.get_country("Spain").posture = "Soft"
        app.get_country("Germany").posture = "Soft"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").posture == "Hard")
        self.assertTrue(app.get_country("Central Asia").is_ungoverned())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Caucasus").posture = "Hard"
        app.get_country("Spain").posture = "Soft"
        app.get_country("Germany").posture = "Soft"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").posture == "Soft")
        self.assertTrue(app.get_country("Central Asia").is_ungoverned())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Caucasus").posture = "Hard"
        app.get_country("Spain").posture = "Hard"
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").posture == "Hard")
        self.assertTrue(app.get_country("Central Asia").is_governed())
        self.assertTrue(app.get_country("Central Asia").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Caucasus").posture = "Hard"
        app.get_country("Spain").posture = "Hard"
        app.testCountry("Central Asia")
        app.get_country("Central Asia").make_ally()
        app.deck["62"].playEvent("Jihadist", app)
        self.assertTrue("CTR" not in app.get_country("Russia").markers)
        self.assertTrue(app.get_country("Caucasus").posture == "Hard")
        self.assertTrue(app.get_country("Central Asia").is_governed())
        self.assertTrue(app.get_country("Central Asia").is_neutral())


class Card63(LabyrinthTestCase):
    """Gaza War"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["63"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["63"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["63"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 6)
        self.assertTrue(app.prestige == 6)


class Card64(LabyrinthTestCase):
    """Hariri Killed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["64"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["64"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_good()
        app.get_country("Syria").make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_fair())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_fair()
        app.get_country("Syria").make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_poor())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_poor()
        app.get_country("Syria").make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_poor())
        self.assertTrue(app.get_country("Syria").is_adversary())

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Syria").make_islamist_rule()
        app.get_country("Syria").make_ally()
        app.deck["64"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Syria").is_islamist_rule())
        self.assertTrue(app.get_country("Syria").is_adversary())


class Card65(LabyrinthTestCase):
    """HEU"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        self.assertTrue(app.deck["65"].playable("Jihadist", app, False))
        app.get_country("Russia").markers.append("CTR")
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        self.assertTrue(app.deck["65"].playable("Jihadist", app, False))
        app.get_country("Central Asia").markers.append("CTR")
        self.assertFalse(app.deck["65"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["65"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        app.executeCardHEU("Russia", 1)
        self.assertTrue(app.get_country("Russia").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        app.executeCardHEU("Russia", 3)
        self.assertTrue(app.get_country("Russia").sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        app.executeCardHEU("Central Asia", 1)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        app.executeCardHEU("Central Asia", 4)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 0)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Russia").sleeperCells = 1
        app.deck["65"].playEvent("Jihadist", app)


class Card66(LabyrinthTestCase):
    """Homegrown"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["66"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["66"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["66"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("United Kingdom").posture != "")
        self.assertTrue(app.get_country("United Kingdom").sleeperCells == 1)


class Card67(LabyrinthTestCase):
    """Islamic Jihad Union"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["67"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["67"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["67"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck["67"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 0)


class Card68(LabyrinthTestCase):
    """Jemaah Islamiya"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["68"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["68"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["68"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Indonesia/Malaysia").sleeperCells == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck["68"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Indonesia/Malaysia").sleeperCells == 1)


class Card69(LabyrinthTestCase):
    """Kazakh Strain"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        self.assertTrue(app.deck["69"].playable("Jihadist", app, False))
        app.get_country("Central Asia").markers.append("CTR")
        self.assertFalse(app.deck["69"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["69"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        app.executeCardHEU("Central Asia", 1)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Central Asia")
        app.get_country("Central Asia").sleeperCells = 1
        app.executeCardHEU("Central Asia", 4)
        self.assertTrue(app.get_country("Central Asia").sleeperCells == 0)

        app.deck["69"].playEvent("Jihadist", app)


class Card70(LabyrinthTestCase):
    """Lashkar-e-Tayyiba"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["70"].playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck["70"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["70"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["70"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue(app.get_country("India").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.deck["70"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue(app.get_country("India").sleeperCells == 0)


class Card71(LabyrinthTestCase):
    """Kazakh Strain"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        self.assertTrue(app.deck["71"].playable("Jihadist", app, False))
        app.get_country("Russia").markers.append("CTR")
        self.assertFalse(app.deck["71"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["71"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        app.executeCardHEU("Russia", 1)
        self.assertTrue(app.get_country("Russia").sleeperCells == 1)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Russia")
        app.get_country("Russia").sleeperCells = 1
        app.executeCardHEU("Russia", 4)
        self.assertTrue(app.get_country("Russia").sleeperCells == 0)

        app.deck["71"].playEvent("Jihadist", app)


class Card72(LabyrinthTestCase):
    """Opium"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["72"].playable("Jihadist", app, False))
        app.get_country("Afghanistan").sleeperCells = 1
        self.assertTrue(app.deck["72"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["72"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 14
        app.testCountry("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 14
        app.testCountry("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.get_country("Afghanistan").make_islamist_rule()
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 15)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 2
        app.testCountry("Afghanistan")
        app.get_country("Afghanistan").sleeperCells = 1
        app.deck["72"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 3)


class Card73(LabyrinthTestCase):
    """Pirates"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["73"].playable("Jihadist", app, False))
        app.get_country("Somalia").make_islamist_rule()
        self.assertTrue(app.deck["73"].playable("Jihadist", app, False))
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["73"].playable("Jihadist", app, False))
        app.get_country("Yemen").make_islamist_rule()
        self.assertTrue(app.deck["73"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["73"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["73"].playEvent("Jihadist", app)
        self.assertTrue("Pirates" in app.markers)
        app.end_turn()
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Somalia").make_islamist_rule()
        app.deck["73"].playEvent("Jihadist", app)
        app.end_turn()
        self.assertTrue(app.funding == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Yemen").make_islamist_rule()
        app.deck["73"].playEvent("Jihadist", app)
        app.end_turn()
        self.assertTrue(app.funding == 5)


class Card74(LabyrinthTestCase):
    """Schengen Visas"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["74"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["74"].putsCell())

    def test_event_when_no_cells_on_map(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.cells = 15
        messages_before = len(app.history)
        app.deck["74"].playEvent("Jihadist", app)
        self.assert_new_messages(app, messages_before,
                ['Card played for Event.', 'No cells to travel.'])


class Card75(LabyrinthTestCase):
    """Schroeder & Chirac"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["75"].playable("Jihadist", app, False))
        app.get_country("United States").posture = "Soft"
        self.assertFalse(app.deck["75"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["75"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck["75"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Germany").posture == "Soft")
        self.assertTrue(app.get_country("France").posture == "Soft")
        self.assertTrue(app.prestige == 6)


class Card76(LabyrinthTestCase):
    """Abu Ghurayb"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["76"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        self.assertFalse(app.deck["76"].playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertTrue(app.deck["76"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["76"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        iraq.sleeperCells = 1
        app.deck["76"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 5)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        iraq.sleeperCells = 1
        app.testCountry("Pakistan")
        app.testCountry("Lebanon")
        app.get_country("Lebanon").make_ally()
        app.deck["76"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Lebanon").is_neutral())
        self.assertTrue(app.prestige == 5)


class Card77(LabyrinthTestCase):
    """Al Jazeera"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Saudi Arabia")
        app.get_country("Saudi Arabia").troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Jordan")
        app.get_country("Jordan").troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Gulf States")
        app.get_country("Gulf States").troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["77"].playable("Jihadist", app, False))
        app.testCountry("Yemen")
        app.get_country("Yemen").troopCubes = 1
        self.assertTrue(app.deck["77"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["77"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Yemen")
        app.get_country("Yemen").troopCubes = 1
        app.deck["77"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Yemen").is_adversary())


class Card78(LabyrinthTestCase):
    """Axis of Evil"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["78"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["78"].putsCell())

    def test_event(self):
        for i in range(100):
            app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
            app.get_country("United States").posture = "Soft"
            app.deck["78"].playEvent("Jihadist", app)
            self.assertTrue(app.get_country("United States").posture == "Hard")
            self.assertTrue(app.prestige != 7)


class Card79(LabyrinthTestCase):
    """Clean Operatives"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["79"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["79"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck["79"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("United States").sleeperCells == 2)


class Card80(LabyrinthTestCase):
    """FATA"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["80"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["80"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck["80"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)
        self.assertTrue("FATA" in app.get_country("Pakistan").markers)


class Card81(LabyrinthTestCase):
    """Foreign Fighters"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["81"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        self.assertFalse(app.deck["81"].playable("Jihadist", app, False))
        iraq.regimeChange = 1
        self.assertTrue(app.deck["81"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["81"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        app.deck["81"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 5)
        self.assertTrue(iraq.besieged == 1)
        self.assertTrue(iraq.aid == 0)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        iraq.aid = 1
        app.deck["81"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 5)
        self.assertTrue(iraq.besieged == 0)
        self.assertTrue(iraq.aid == 0)


class Card82(LabyrinthTestCase):
    """Jihadist Videos"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["82"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["82"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck["82"].playEvent("Jihadist", app)


class Card83(LabyrinthTestCase):
    """Kashmir"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["83"].playable("Jihadist", app, False))
        app.markers.append("Indo-Pakistani Talks")
        self.assertFalse(app.deck["83"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["83"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.testCountry("Pakistan")
        app.deck["83"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Pakistan").is_adversary())
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)


class Card84(LabyrinthTestCase):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["84"].playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck["84"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["84"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Enhanced Measures")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Renditions")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Wiretapping")
        app.deck["84"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card85(LabyrinthTestCase):
    """Leak"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Enhanced Measures")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Renditions")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["85"].playable("Jihadist", app, False))
        app.markers.append("Wiretapping")
        self.assertTrue(app.deck["85"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["85"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Enhanced Measures")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Enhanced Measures" in app.markers)
        self.assertTrue("Enhanced Measures" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Renditions")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Renditions" in app.markers)
        self.assertTrue("Renditions" not in app.markers)

        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.markers.append("Wiretapping")
        app.deck["85"].playEvent("Jihadist", app)
        self.assertTrue("Leak-Wiretapping" in app.markers)
        self.assertTrue("Wiretapping" not in app.markers)
        self.assertTrue(app.prestige != 7)


class Card86(LabyrinthTestCase):
    """Lebanon War"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["86"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["86"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.deck["86"].playEvent("Jihadist", app)
        self.assertTrue(app.prestige == 6)


class Card87(LabyrinthTestCase):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.make_islamist_rule()
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertFalse(app.deck["87"].playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertTrue(app.deck["87"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["87"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.deck["87"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 0)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.deck["87"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 1)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 0)
        self.assertTrue(app.get_country("United States").sleeperCells == 0)
        self.assertTrue(app.get_country("United States").activeCells == 0)
        self.assertTrue(app.get_country("United States").plots == 2)


class Card88(LabyrinthTestCase):
    """Martyrdom Operation"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.make_islamist_rule()
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertFalse(app.deck["88"].playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertTrue(app.deck["88"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["88"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.deck["88"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 0)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.deck["88"].playEvent("Jihadist", app)
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
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.make_islamist_rule()
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertFalse(app.deck["89"].playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertTrue(app.deck["89"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["89"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.deck["89"].playEvent("Jihadist", app)
        self.assertTrue(iraq.sleeperCells == 0)
        self.assertTrue(iraq.activeCells == 0)
        self.assertTrue(iraq.plots == 2)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        app.testCountry("Iraq")
        iraq.sleeperCells = 1
        app.get_country("United States").sleeperCells = 1
        app.deck["89"].playEvent("Jihadist", app)
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
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 6
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        iraq.regimeChange = 1
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        iraq.sleeperCells = 1
        self.assertTrue(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 7
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))
        app.prestige = 6
        iraq.regimeChange = 0
        self.assertFalse(app.deck["90"].playable("Jihadist", app, False))    

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["90"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Iraq")
        app.deck["90"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("United States").posture == "Soft")


class Card91(LabyrinthTestCase):
    """Regional al-Qaeda"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        al_qaeda = app.deck["91"]
        self.assertTrue(al_qaeda.playable("Jihadist", app, False))
        for country in app.find_countries(lambda c: c.is_muslim()):
            app.testCountry(country.name)
        self.assertFalse(al_qaeda.playable("Jihadist", app, False))
        iraq.make_ungoverned()
        iraq.alignment = ""
        self.assertFalse(al_qaeda.playable("Jihadist", app, False))
        lebanon = app.get_country("Lebanon")
        lebanon.make_ungoverned()
        lebanon.alignment = ""
        self.assertTrue(al_qaeda.playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["91"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        for country in app.find_countries(lambda c: c.is_muslim()):
            app.testCountry(country.name)
        iraq.make_ungoverned()
        iraq.alignment = ""
        app.get_country("Lebanon").make_ungoverned()
        app.get_country("Lebanon").alignment = ""
        app.deck["91"].playEvent("Jihadist", app)
        self.assertTrue(iraq.is_governed())
        self.assertTrue(iraq.is_aligned())
        self.assertTrue(iraq.sleeperCells == 1)
        self.assertTrue(app.get_country("Lebanon").is_governed())
        self.assertTrue(app.get_country("Lebanon").is_aligned())
        self.assertTrue(app.get_country("Lebanon").sleeperCells == 1)


class Card92(LabyrinthTestCase):
    """Saddam"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        iraq = app.get_country("Iraq")
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        app.testCountry("Iraq")
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        iraq.make_poor()
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))
        iraq.make_adversary()
        self.assertTrue(app.deck["92"].playable("Jihadist", app, False))
        app.markers.append("Saddam Captured")
        self.assertFalse(app.deck["92"].playable("Jihadist", app, False))        

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["92"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["92"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)         


class Card93(LabyrinthTestCase):
    """Taliban"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["93"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["93"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").besieged == 1)         
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.get_country("Afghanistan").make_islamist_rule()
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").besieged == 1)         
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.get_country("Pakistan").make_islamist_rule()
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").besieged == 1)         
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 1)         
        self.assertTrue(app.prestige == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.cells = 1
        app.testCountry("Afghanistan")
        app.testCountry("Pakistan")
        app.deck["93"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Afghanistan").besieged == 1)         
        self.assertTrue(app.get_country("Afghanistan").sleeperCells == 1)         
        self.assertTrue(app.get_country("Pakistan").sleeperCells == 0)         
        self.assertTrue(app.prestige == 6)


class Card94(LabyrinthTestCase):
    """The door of Itjihad was closed"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["n", "y"])
        print "Say No"
        self.assertFalse(app.deck["94"].playable("Jihadist", app, False))
        print "Say Yes"
        self.assertTrue(app.deck["94"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["94"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["Iraq"])
        iraq = app.get_country("Iraq")
        print "Choose Iraq"
        app.testCountry("Iraq")
        iraq.make_fair()
        app.deck["94"].playEvent("Jihadist", app)
        self.assertTrue(iraq.is_poor())


class Card95(LabyrinthTestCase):
    """Wahhabism"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["95"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["95"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Saudi Arabia").make_poor()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 8)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.get_country("Saudi Arabia").make_fair()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 7)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Saudi Arabia")
        app.get_country("Saudi Arabia").make_islamist_rule()
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.testCountry("Saudi Arabia")
        app.get_country("Saudi Arabia").make_islamist_rule()
        app.funding = 2
        app.deck["95"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 9)


class Card96(LabyrinthTestCase):
    """Danish Cartoons"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["96"].playable("US", app, True))
        self.assertTrue(app.deck["96"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["96"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["s", "h"])
        iraq = app.get_country("Iraq")
        app.deck["96"].playEvent("US", app)
        self.assertTrue(app.get_country("Scandinavia").posture == "Soft")
        app.testCountry("Iraq")
        iraq.make_islamist_rule()
        app.deck["96"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Scandinavia").posture == "Hard")


class Card97(LabyrinthTestCase):
    """Fatwa"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario, ["y", "n"])
        print "Say Yes"
        self.assertTrue(app.deck["97"].playable("US", app, True))
        print "Say No"
        self.assertFalse(app.deck["97"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["97"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["97"].playEvent("US", app)
        app.deck["97"].playEvent("Jihadist", app)


class Card98(LabyrinthTestCase):
    """Gaza Withdrawl"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["98"].playable("US", app, True))
        self.assertTrue(app.deck["98"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["98"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["98"].playEvent("US", app)
        self.assertTrue(app.funding == 4)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["98"].playEvent("Jihadist", app)
        self.assertTrue(app.get_country("Israel").sleeperCells == 1)
        self.assertTrue(app.cells == 10)


class Card99(LabyrinthTestCase):
    """HAMAS Elected"""

    def test_playable(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertTrue(app.deck["99"].playable("US", app, True))
        self.assertTrue(app.deck["99"].playable("Jihadist", app, False))

    def test_puts_cell(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        self.assertFalse(app.deck["99"].putsCell())

    def test_event(self):
        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["99"].playEvent("US", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)

        app = Labyrinth(1, 1, self.set_up_blank_test_scenario)
        app.deck["99"].playEvent("Jihadist", app)
        self.assertTrue(app.funding == 4)
        self.assertTrue(app.prestige == 6)


if __name__ == "__main__":
    unittest.main()   