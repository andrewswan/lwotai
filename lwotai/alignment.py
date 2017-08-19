from lwotai.utils import Utils


class Alignment(object):
    """
    The alignment of a country relative to the US.
    :param name the display name of this alignment
    """
    def __init__(self, name):
        self.__name = Utils.require_type(name, str)

    def __eq__(self, o):
        return type(o) == Alignment and self.__name == o.__name

    def __ne__(self, o):
        return not self.__eq__(o)

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name


ADVERSARY = Alignment("Adversary")
ALLY = Alignment("Ally")
NEUTRAL = Alignment("Neutral")
