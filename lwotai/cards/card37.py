from lwotai.cards.abstract_card import AbstractCard


class Card37(AbstractCard):

    def __init__(self):
        super(Card37, self).__init__(37, "US", "Iraqi WMD", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.us().is_hard() and app.get_country("Iraq").is_adversary()

    def play_event(self, side, app):
        app.markers.append("Iraqi WMD")
        app.output_to_history("Iraqi WMD in Play.", False)
        app.output_to_history("Use this or a later card for Regime Change in Iraq at any Governance.", True)
