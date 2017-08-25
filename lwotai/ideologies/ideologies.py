from lwotai.utils import Utils

from lwotai.ideologies.attractive import Attractive
from lwotai.ideologies.coherent import Coherent
from lwotai.ideologies.infectious import Infectious
from lwotai.ideologies.normal import Normal
from lwotai.ideologies.potent import Potent
from lwotai.ideologies.virulent import Virulent


IDEOLOGIES = [
    Normal(),
    Coherent(),
    Attractive(),
    Potent(),
    Infectious(),
    Virulent()
]


def choose_ideology():
    """Prompts the user to choose an ideology (returns a 1-indexed number)"""
    descriptions = ["%s: %s" % (i.name(), i.difference()) for i in IDEOLOGIES]
    return Utils.choose_option("Choose Jihadist Ideology", descriptions)


def get_ideology(number):
    """Returns the ideology with the given number (starting at 1)"""
    return IDEOLOGIES[number - 1]
