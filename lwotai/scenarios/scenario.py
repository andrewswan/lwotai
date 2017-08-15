class Scenario(object):
    """A scenario for the game of Labyrinth."""

    def __init__(self, name):
        self.name = name

    def __eq__(self, o):
        return self.name == o.name

    def __ne__(self, o):
        return self.name != o.name

    def set_up(self, game):
        """Sets up the given game for this scenario"""
        pass
