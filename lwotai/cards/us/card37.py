from lwotai.cards.us.us_card import USCard


class Card37(USCard):

    def __init__(self):
        super(Card37, self).__init__(37, "Iraqi WMD", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.us().is_hard() and app.get_country("Iraq").is_adversary()

    def play_as_us(self, app):
        app.markers.append("Iraqi WMD")
        app.output_to_history("Iraqi WMD in Play.", False)
        app.output_to_history("Use this or a later card for Regime Change in Iraq at any Governance.", True)
