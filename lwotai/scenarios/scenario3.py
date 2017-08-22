import random

from lwotai.scenarios.scenario import Scenario


class Scenario3(Scenario):

    def __init__(self):
        Scenario.__init__(self, "Anaconda")

    def set_up(self, game):
        game.cells = 13
        game.funding = 6
        game.prestige = 8
        game.startYear = 2002
        game.troops = 5
        game.turn = 1
        game.map["Afghanistan"].make_poor()
        game.map["Afghanistan"].make_ally()
        game.map["Afghanistan"].sleeperCells = 1
        game.map["Afghanistan"].troopCubes = 6
        game.map["Afghanistan"].regimeChange = 1
        game.map["Central Asia"].make_poor()
        game.map["Central Asia"].make_ally()
        game.map["Gulf States"].make_fair()
        game.map["Gulf States"].make_ally()
        game.map["Gulf States"].troopCubes = 2
        game.map["Iraq"].make_poor()
        game.map["Iraq"].make_adversary()
        game.map["Libya"].make_poor()
        game.map["Libya"].make_adversary()
        game.map["Pakistan"].make_poor()
        game.map["Pakistan"].make_ally()
        game.map["Pakistan"].sleeperCells = 1
        game.map["Pakistan"].markers.append("FATA")
        game.map["Saudi Arabia"].make_poor()
        game.map["Saudi Arabia"].make_ally()
        game.map["Saudi Arabia"].troopCubes = 2
        game.map["Somalia"].make_besieged()
        game.map["Syria"].make_fair()
        game.map["Syria"].make_adversary()
        game.markers.append("Patriot Act")
        possibles = []
        for country in game.map:
            if country != "United States":
                possibles.append(country)
        random.shuffle(possibles)
        for i in range(3):
            game.test_country(possibles[i])
            game.place_cells(possibles[i], 1)
        print "Remove the 'Patriot Act' and 'Tora Bora' cards (43 and 109) from the game."
        print ""
