from lwotai.cards.jihadist.jihadist_card import JihadistCard
from lwotai.postures.posture import SOFT


class Card55(JihadistCard):

    def __init__(self):
        super(Card55, self).__init__(55, "Uyghur Jihad", 1, True, False, False, True)

    def play_as_jihadist(self, app):
        app.test_country("China")
        if app.cells > 0:
            if app.get_posture("China") == SOFT:
                app.place_cell("China")
            else:
                app.place_cell("Central Asia")
        else:
            app.output_to_history("No cells to place.", True)
