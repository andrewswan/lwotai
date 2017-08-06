from lwotai.scenario.scenario import Scenario


class Scenario4(Scenario):

    def __init__(self):
        Scenario.__init__(self, "Mission Accomplished?")

    def set_up(self, game):
        game.cells = 5
        game.funding = 5
        game.prestige = 3
        game.startYear = 2003
        game.troops = 0
        game.turn = 1
        game.map["Afghanistan"].make_poor()
        game.map["Afghanistan"].make_ally()
        game.map["Afghanistan"].sleeperCells = 1
        game.map["Afghanistan"].troopCubes = 5
        game.map["Afghanistan"].regimeChange = 1
        game.map["Central Asia"].make_fair()
        game.map["Central Asia"].make_neutral()
        game.map["Gulf States"].make_fair()
        game.map["Gulf States"].make_ally()
        game.map["Gulf States"].troopCubes = 2
        game.map["Indonesia/Malaysia"].make_fair()
        game.map["Indonesia/Malaysia"].make_neutral()
        game.map["Indonesia/Malaysia"].sleeperCells = 1
        game.map["Iran"].sleeperCells = 1
        game.map["Iraq"].make_poor()
        game.map["Iraq"].make_ally()
        game.map["Iraq"].troopCubes = 6
        game.map["Iraq"].sleeperCells = 3
        game.map["Iraq"].regimeChange = 1
        game.map["Libya"].make_poor()
        game.map["Libya"].make_adversary()
        game.map["Pakistan"].make_fair()
        game.map["Pakistan"].make_ally()
        game.map["Pakistan"].sleeperCells = 1
        game.map["Pakistan"].markers.append("FATA")
        game.map["Philippines"].posture = "Soft"
        game.map["Philippines"].troopCubes = 2
        game.map["Philippines"].sleeperCells = 1
        game.map["Saudi Arabia"].make_poor()
        game.map["Saudi Arabia"].make_ally()
        game.map["Saudi Arabia"].sleeperCells = 1
        game.map["Somalia"].besieged = 1
        game.map["Syria"].make_fair()
        game.map["Syria"].make_adversary()
        game.map["Syria"].sleeperCells = 1
        game.map["United Kingdom"].posture = "Hard"
        game.markers.append("Abu Sayyaf")
        game.markers.append("Enhanced Measures")
        game.markers.append("NEST")
        game.markers.append("Patriot Act")
        game.markers.append("Renditions")
        game.markers.append("Wiretapping")
        possibles = []
        for country in game.map:
            if game.map[country].schengen:
                game.testCountry(country)
        print ""
        print "Remove the cards Patriot Act, Tora Bora, NEST, Abu Sayyaf, KSM and Iraqi WMD from the game."
        print ""
