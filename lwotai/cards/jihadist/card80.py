from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card80(JihadistCard):

    def __init__(self):
        super(Card80, self).__init__(80, "FATA", 3, False, True, False, True)

    def play_as_jihadist(self, app):
        app.test_country("Pakistan")
        if app.get_country("Pakistan").markers.count("FATA") == 0:
            app.get_country("Pakistan").markers.append("FATA")
            app.output_to_history("FATA marker added in Pakistan", True)
        app.place_cells("Pakistan", 1)
