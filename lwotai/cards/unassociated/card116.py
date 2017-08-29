from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card116(UnassociatedCard):

    def __init__(self):
        super(Card116, self).__init__(116, "KSM", 3, False, False, False, False)

    def _really_playable(self, side, app, _ignore_itjihad):
        if side == "US":
            return app.contains_country(lambda c: c.plots > 0 and (c.is_non_muslim() or c.is_ally()))
        else:
            return True

    def do_play_event(self, side, app):
        if side == "US":
            for country in app.get_countries():
                if country.plots > 0:
                    if country.is_ally() or country.is_non_muslim():
                        num_plots = country.plots
                        country.plots = 0
                        app.output_to_history("%d Plots removed from %s." % (num_plots, country.name), False)
            app.output_to_history("US draws 2 cards.")
        else:
            if app.execute_plot(1, False, [1], False, False, True) == 1:
                app.output_to_history("No plots could be placed.")
