from lwotai.cards.abstract_card import AbstractCard


class Card26(AbstractCard):

    def __init__(self):
        super(Card26, self).__init__(26, "US", "Quartet", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return "Abbas" in app.markers and app.troops >= 5 and\
            not app.contains_country(lambda c: c.is_islamist_rule() and app.is_adjacent(c.name, "Israel"))

    def play_event(self, side, app):
        if "Abbas" not in app.markers or app.troops < 5:
            return False
        for country in app.get_countries():
            if app.is_adjacent(country.name, "Israel") and country.is_islamist_rule():
                return False
        app.change_prestige(2)
        app.change_funding(-3)
        app.output_to_history("", False)
