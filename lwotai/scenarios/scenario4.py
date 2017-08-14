from lwotai.scenarios.scenario import Scenario


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
        game.get_country("Afghanistan").make_poor()
        game.get_country("Afghanistan").make_ally()
        game.get_country("Afghanistan").sleeperCells = 1
        game.get_country("Afghanistan").troopCubes = 5
        game.get_country("Afghanistan").regimeChange = 1
        game.get_country("Central Asia").make_fair()
        game.get_country("Central Asia").make_neutral()
        game.get_country("Gulf States").make_fair()
        game.get_country("Gulf States").make_ally()
        game.get_country("Gulf States").troopCubes = 2
        game.get_country("Indonesia/Malaysia").make_fair()
        game.get_country("Indonesia/Malaysia").make_neutral()
        game.get_country("Indonesia/Malaysia").sleeperCells = 1
        game.get_country("Iran").sleeperCells = 1
        game.get_country("Iraq").make_poor()
        game.get_country("Iraq").make_ally()
        game.get_country("Iraq").troopCubes = 6
        game.get_country("Iraq").sleeperCells = 3
        game.get_country("Iraq").regimeChange = 1
        game.get_country("Libya").make_poor()
        game.get_country("Libya").make_adversary()
        game.get_country("Pakistan").make_fair()
        game.get_country("Pakistan").make_ally()
        game.get_country("Pakistan").sleeperCells = 1
        game.get_country("Pakistan").markers.append("FATA")
        game.get_country("Philippines").posture = "Soft"
        game.get_country("Philippines").troopCubes = 2
        game.get_country("Philippines").sleeperCells = 1
        game.get_country("Saudi Arabia").make_poor()
        game.get_country("Saudi Arabia").make_ally()
        game.get_country("Saudi Arabia").sleeperCells = 1
        game.get_country("Somalia").besieged = 1
        game.get_country("Syria").make_fair()
        game.get_country("Syria").make_adversary()
        game.get_country("Syria").sleeperCells = 1
        game.get_country("United Kingdom").posture = "Hard"
        game.markers.append("Abu Sayyaf")
        game.markers.append("Enhanced Measures")
        game.markers.append("NEST")
        game.markers.append("Patriot Act")
        game.markers.append("Renditions")
        game.markers.append("Wiretapping")
        for country in game.get_countries():
            if country.schengen:
                game.test_country(country.name)
        print ""
        print "Remove the cards Patriot Act, Tora Bora, NEST, Abu Sayyaf, KSM and Iraqi WMD from the game."
        print ""
