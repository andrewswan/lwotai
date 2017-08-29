from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card112(UnassociatedCard):

    def __init__(self):
        super(Card112, self).__init__(112, "Bin Ladin", 3, False, False, False, False)

    def _really_playable(self, side, app, _ignore_itjihad):
        if side == "US":
            if "FATA" in app.get_country("Pakistan").markers:
                return False
            if "Al-Anbar" in app.markers:
                return False
            return app.num_islamist_rule() == 0
        else:
            return True

    def do_play_event(self, side, app):
        if side == "US":
            app.change_funding(-4)
            app.change_prestige(1)
            app.output_to_history("Remove card from game.", False)
        else:
            prestige_change = -4 if app.num_islamist_rule() > 0 else -2
            app.change_prestige(prestige_change)
