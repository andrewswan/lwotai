import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card82(JihadistCard):

    def __init__(self):
        super(Card82, self).__init__(82, "Jihadist Videos", 3, False, False, False, True)

    def play_as_jihadist(self, app):
        possibles = app.find_countries(lambda c: c.total_cells() == 0)
        random.shuffle(possibles)
        for i in range(3):
            app.test_country(possibles[i].name)
            # number of available cells does not matter for Jihadist Videos
            rolls = [random.randint(1, 6)]
            app.execute_recruit(possibles[i].name, 1, rolls, False, True)
