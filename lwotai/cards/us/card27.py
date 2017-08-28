from lwotai.cards.us.us_card import USCard


class Card27(USCard):

    def __init__(self):
        super(Card27, self).__init__(27, "Saddam Captured", 2, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").troops() > 0

    def play_event(self, side, app):
        if not app.get_country("Iraq").troops():
            return False
        app.markers.append("Saddam Captured")
        app.get_country("Iraq").add_aid(1)
        app.output_to_history("Aid added in Iraq", False)
        app.change_prestige(1)
        app.output_to_history(app.get_country("Iraq").summary(), True)
