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
        game.get_country("Afghanistan").make_poor()
        game.get_country("Afghanistan").make_ally()
        game.get_country("Afghanistan").sleeperCells = 1
        game.get_country("Afghanistan").troopCubes = 6
        game.get_country("Afghanistan").make_regime_change()
        game.get_country("Central Asia").make_poor()
        game.get_country("Central Asia").make_ally()
        game.get_country("Gulf States").make_fair()
        game.get_country("Gulf States").make_ally()
        game.get_country("Gulf States").troopCubes = 2
        game.get_country("Iraq").make_poor()
        game.get_country("Iraq").make_adversary()
        game.get_country("Libya").make_poor()
        game.get_country("Libya").make_adversary()
        game.get_country("Pakistan").make_poor()
        game.get_country("Pakistan").make_ally()
        game.get_country("Pakistan").sleeperCells = 1
        game.get_country("Pakistan").markers.append("FATA")
        game.get_country("Saudi Arabia").make_poor()
        game.get_country("Saudi Arabia").make_ally()
        game.get_country("Saudi Arabia").troopCubes = 2
        game.get_country("Somalia").make_besieged()
        game.get_country("Syria").make_fair()
        game.get_country("Syria").make_adversary()
        game.markers.append("Patriot Act")
        non_us_countries = game.find_countries(lambda c: c.name != "United States")
        random.shuffle(non_us_countries)
        for i in range(3):
            country_name = non_us_countries[i].name
            game.test_country(country_name)
            game.place_cells(country_name, 1)
        print "Remove the 'Patriot Act' and 'Tora Bora' cards (43 and 109) from the game."
        print ""
