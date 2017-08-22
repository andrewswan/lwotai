from lwotai.scenarios.scenario import Scenario


class Scenario1(Scenario):

    def __init__(self):
        Scenario.__init__(self, "Let's Roll!")

    def set_up(self, game):
        game.cells = 11
        game.funding = 9
        game.phase = "Jihadist Action Phase"
        game.prestige = 7
        game.startYear = 2001
        game.troops = 11
        game.turn = 1
        game.get_country("Afghanistan").make_islamist_rule()
        game.get_country("Afghanistan").make_adversary()
        game.get_country("Afghanistan").sleeperCells = 4
        game.get_country("Gulf States").make_fair()
        game.get_country("Gulf States").make_ally()
        game.get_country("Gulf States").troopCubes = 2
        game.get_country("Iraq").make_poor()
        game.get_country("Iraq").make_adversary()
        game.get_country("Libya").make_poor()
        game.get_country("Libya").make_adversary()
        game.get_country("Pakistan").make_fair()
        game.get_country("Pakistan").make_neutral()
        game.get_country("Saudi Arabia").make_poor()
        game.get_country("Saudi Arabia").make_ally()
        game.get_country("Saudi Arabia").troopCubes = 2
        game.get_country("Somalia").make_besieged()
        game.get_country("Syria").make_fair()
        game.get_country("Syria").make_adversary()
        game.us().make_hard()
