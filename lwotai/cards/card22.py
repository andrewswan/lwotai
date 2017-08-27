from lwotai.cards.abstract_card import AbstractCard


class Card22(AbstractCard):

    def __init__(self):
        super(Card22, self).__init__(22, "US", "Mossad and Shin Bet", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        for country_name in ["Israel", "Jordan", "Lebanon"]:
            if app.get_country(country_name).total_cells():
                return True
        return False

    def play_event(self, side, app):
        for country_name in ["Israel", "Jordan", "Lebanon"]:
            app.remove_all_cells_from_country(country_name)
        app.output_to_history("", False)
