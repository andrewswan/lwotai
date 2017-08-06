from lwotai.scenario.scenario import Scenario
from lwotai.scenario.scenario1 import Scenario1


class Scenario2(Scenario):

    def __init__(self):
        Scenario.__init__(self, "You Can Call Me Al")

    def set_up(self, game):
        Scenario1().set_up(game)
        game.map["United States"].posture = "Soft"
        print "Remove the 'Axis of Evil' card (78) from the game."
        print ""
