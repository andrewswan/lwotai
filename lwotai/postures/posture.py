class Posture(object):
    """The posture of a non-Muslim country"""

    def __init__(self, name):
        self.__name = name

    def __eq__(self, o):
        try:
            return self.__name == o.__name
        except AttributeError:
            return False

    def __ne__(self, o):
        return not self.__eq__(o)

    def __repr__(self):
        return self.__name


# The possible postures in the game (plus None)
HARD = Posture("Hard")
SOFT = Posture("Soft")
