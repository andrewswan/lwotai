from lwotai.cards.us.us_card import USCard


class Card3(USCard):

    def __init__(self):
        super(Card3, self).__init__(3, "CTR", 1, False, True, False)

    def _really_playable(self, side, app, ignore_itjihad):
        return app.us().is_soft()

    def play_as_us(self, app):
        app.get_country("Russia").markers.append("CTR")    # 20150616PS
        app.output_to_history("CTR Marker added Russia", True)    # 20150616PS
        central_asia = app.get_country("Central Asia")
        if central_asia.is_ally() or central_asia.is_neutral():
            central_asia.markers.append("CTR")    # 20150616PS
            app.output_to_history("CTR Marker added in Central Asia", True)    # 20150616PS
