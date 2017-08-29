from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card111(UnassociatedCard):

    def __init__(self):
        super(Card111, self).__init__(111, "Zawahiri", 2, False, False, False, False)

    def _really_playable(self, side, app, _ignore_itjihad):
        if side == "US":
            if "FATA" in app.get_country("Pakistan").markers:
                return False
            if "Al-Anbar" in app.markers:
                return False
            return app.num_islamist_rule() == 0
        else:
            return True

    def play_event(self, side, app):
        if side == "US":
            app.change_funding(-2)
        else:
            prestige_change = -3 if app.num_islamist_rule() > 0 else -1
            app.change_prestige(prestige_change)
