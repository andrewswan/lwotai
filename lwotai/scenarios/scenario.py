from lwotai.scenarios.scenario1 import Scenario1
from lwotai.scenarios.scenario2 import Scenario2
from lwotai.scenarios.scenario3 import Scenario3
from lwotai.scenarios.scenario4 import Scenario4


class Scenario:
    """A scenario for the game of Labyrinth."""

    def __init__(self, name):
        self.name = name

    def set_up(self, game):
        """Sets up the given game for this scenario"""
        raise

# To create a new scenario, base it off one of the classes below and append it to this list
SCENARIOS = [
    Scenario1(),
    Scenario2(),
    Scenario3(),
    Scenario4()
]


def get_scenario(number):
    """Returns the scenario with the given number (starting at 1)"""
    return SCENARIOS[number - 1]


def scenario_names():
    """Returns the names of the various scenarios"""
    return [scenario.name for scenario in SCENARIOS]
