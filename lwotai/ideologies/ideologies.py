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


def get_ideology(number):
    """Returns the ideology with the given number (starting at 1)"""
    return IDEOLOGIES[number - 1]
