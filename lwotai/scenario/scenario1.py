from lwotai.scenario.scenario import Scenario


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
        game.map["Afghanistan"].make_islamist_rule()
        game.map["Afghanistan"].make_adversary()
        game.map["Afghanistan"].sleeperCells = 4
        game.map["Gulf States"].make_fair()
        game.map["Gulf States"].make_ally()
        game.map["Gulf States"].troopCubes = 2
        game.map["Iraq"].make_poor()
        game.map["Iraq"].make_adversary()
        game.map["Libya"].make_poor()
        game.map["Libya"].make_adversary()
        game.map["Pakistan"].make_fair()
        game.map["Pakistan"].make_neutral()
        game.map["Saudi Arabia"].make_poor()
        game.map["Saudi Arabia"].make_ally()
        game.map["Saudi Arabia"].troopCubes = 2
        game.map["Somalia"].besieged = 1
        game.map["Syria"].make_fair()
        game.map["Syria"].make_adversary()
        game.map["United States"].posture = "Hard"
