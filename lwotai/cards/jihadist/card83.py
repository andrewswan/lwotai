from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card83(JihadistCard):

    def __init__(self):
        super(Card83, self).__init__(83, "Kashmir", 3, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Indo-Pakistani Talks" not in app.markers

    def play_as_jihadist(self, app):
        app.place_cells("Pakistan", 1)
        pakistan = app.get_country("Pakistan")
        if pakistan.is_ally():
            pakistan.make_neutral()
        elif pakistan.is_neutral():
            pakistan.make_adversary()
        app.output_to_history("Pakistan Alignment shifted to %s." % pakistan.alignment())
        app.output_to_history(pakistan.summary(), True)
