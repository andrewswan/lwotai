from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card73(JihadistCard):

    def __init__(self):
        super(Card73, self).__init__(73, "Pirates", 2, True, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Somalia").is_islamist_rule() or app.get_country("Yemen").is_islamist_rule()

    def play_as_jihadist(self, app):
        app.markers.append("Pirates")
        app.output_to_history("Pirates in play.", False)
