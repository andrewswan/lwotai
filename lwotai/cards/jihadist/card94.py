import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card94(JihadistCard):

    def __init__(self):
        super(Card94, self).__init__(94, "The door of Itjihad was closed", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_yes_no_from_user(
            "Was a country tested or improved to Fair or Good this or last Action Phase.? (y/n): ")

    def play_as_jihadist(self, app):
        target_country = None
        while not target_country:
            country_name = app.get_country_from_user(
                "Choose a country tested or improved to Fair or Good this or last Action Phase: ", "XXX", None)
            if country_name == "":
                print ""
            elif app.get_country(country_name).is_fair() or app.get_country(country_name).is_good():
                target_country = app.get_country(country_name)
            else:
                print "%s is neither Fair nor Good."
        app.worsen_governance(target_country.name)
        app.output_to_history("%s Governance worsened." % target_country.name, False)
        app.output_to_history(target_country.summary())
