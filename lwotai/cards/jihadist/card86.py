import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card86(JihadistCard):

    def __init__(self):
        super(Card86, self).__init__(86, "Lebanon War", 3, False, False, False, True)

    def play_as_jihadist(self, app):
        app.output_to_history("US discards a random card.", False)
        app.change_prestige(-1, False)
        possibles = app.find_countries(lambda c: c.is_shia_mix())
        target = random.choice(possibles)
        app.place_cells(target.name, 1)
