from lwotai.cards.abstract_card import AbstractCard


class Card31(AbstractCard):

    def __init__(self):
        super(Card31, self).__init__(31, "US", "Wiretapping", 2, False, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if "Leak-Wiretapping" in app.markers:
            return False
        for country_name in ["United States", "United Kingdom", "Canada"]:
            country = app.get_country(country_name)
            if country.total_cells() or country.cadre or country.plots:
                return True
        return False

    def play_event(self, side, app):
        if "Leak-Wiretapping" in app.markers:
            return False
        for country in ["United States", "United Kingdom", "Canada"]:
            if app.get_country(country).activeCells > 0:
                num = app.get_country(country).activeCells
                if num > 0:
                    app.get_country(country).activeCells -= num
                    app.cells += num
                    app.output_to_history("%d Active Cell(s) removed from %s." % (num, country), False)
            if app.get_country(country).sleeperCells > 0:
                num = app.get_country(country).sleeperCells
                if num > 0:
                    app.get_country(country).sleeperCells -= num
                    app.cells += num
                    app.output_to_history("%d Sleeper Cell(s) removed from %s." % (num, country), False)
            if app.get_country(country).cadre > 0:
                num = app.get_country(country).cadre
                if num > 0:
                    app.get_country(country).cadre = 0
                    app.output_to_history("Cadre removed from %s." % country, False)
            if app.get_country(country).plots > 0:
                num = app.get_country(country).plots
                if num > 0:
                    app.get_country(country).plots -= num
                    app.output_to_history("%d Plots remove(d) from %s." % (num, country), False)
        app.markers.append("Wiretapping")
        app.output_to_history("Draw a card.")
        app.output_to_history("Wiretapping in Play.")
