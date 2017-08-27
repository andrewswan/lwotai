from lwotai.cards.abstract_card import AbstractCard


class Card39(AbstractCard):

    def __init__(self):
        super(Card39, self).__init__(39, "US", "Libyan WMD", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.us().is_hard() and app.get_country("Libya").is_adversary() and "Libyan Deal" not in app.markers

    def play_event(self, side, app):
        app.markers.append("Libyan WMD")
        app.output_to_history("Libyan WMD in Play.", False)
        app.output_to_history("Use this or a later card for Regime Change in Libya at any Governance.", True)
