from lwotai.cards.us.us_card import USCard


class Card33(USCard):

    def __init__(self):
        super(Card33, self).__init__(33, "Benazir Bhutto", 3, True, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if "Bhutto Shot" in app.markers or app.get_country("Pakistan").is_islamist_rule():
            return False
        for country in app.get_country("Pakistan").links:
            if country.is_islamist_rule():
                return False
        return True

    def play_as_us(self, app):
        app.markers.append("Benazir Bhutto")
        app.output_to_history("Benazir Bhutto in Play.", False)
        pakistan = app.get_country("Pakistan")
        if pakistan.is_poor():
            pakistan.make_fair()
            app.output_to_history("Pakistan now Fair governance.", False)
        app.output_to_history("No Jihads in Pakistan.", False)
        app.output_to_history(pakistan.summary(), True)
