from attractive import Attractive
from coherent import Coherent
from infectious import Infectious
from normal import Normal
from potent import Potent
from virulent import Virulent


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
