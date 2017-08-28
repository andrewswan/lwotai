from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card51(JihadistCard):

    def __init__(self):
        super(Card51, self).__init__(51, "FREs", 1, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").troops() > 0

    def play_event(self, side, app):
        cells_to_move = 2 if "Saddam Captured" in app.markers else 4
        cells_to_move = min(cells_to_move, app.cells)
        app.place_cells("Iraq", cells_to_move)
