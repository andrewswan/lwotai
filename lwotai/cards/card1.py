from cards.abstract_card import AbstractCard


class Card1(AbstractCard):

    def __init__(self):
        super(Card1, self).__init__(1, "US", "Backlash", 1, False, False, False)

    def _really_playable(self, side, app, ignore_itjihad):
        return app.contains_country(lambda c: c.plots > 0 and not c.is_non_muslim())

    def play_event(self, side, app):
        for country in app.get_countries():
            if country.plots > 0 and not country.is_non_muslim():
                app.output_to_history(
                    "Plot in Muslim country found. Select the plot during plot phase. Backlash in play")
                app.backlashInPlay = True
                return True
        return False

