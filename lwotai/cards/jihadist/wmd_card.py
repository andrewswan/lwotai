import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class WmdCard(JihadistCard):
    """Superclass for Jihadist cards that attempt to obtain a WMD"""

    def __init__(self, number, name, ops, remove, mark, lapsing, puts_cell, target_country_names):
        super(WmdCard, self).__init__(number, name, ops, remove, mark, lapsing, puts_cell)
        self.__target_country_names = target_country_names

    def _get_valid_target_countries(self, app):
        return app.find_countries(
            lambda c: c.name in self.__target_country_names and c.total_cells() > 0 and "CTR" not in c.markers)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return len(self._get_valid_target_countries(app)) > 0

    def play_as_jihadist(self, app):
        target_country = random.choice(self._get_valid_target_countries(app))
        roll = app.roll_d6()
        if target_country.is_non_recruit_success(roll):
            app.output_to_history("Add a WMD to available Plots.", True)
        else:
            app.remove_cell(target_country.name, "Jihadist")
