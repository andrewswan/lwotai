from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card72(JihadistCard):

    def __init__(self):
        super(Card72, self).__init__(72, "Opium", 2, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Afghanistan").total_cells() > 0

    def play_as_jihadist(self, app):
        cells_to_place = min(app.cells, 3)
        if app.get_country("Afghanistan").is_islamist_rule():
            cells_to_place = app.cells
        app.place_cells("Afghanistan", cells_to_place)
