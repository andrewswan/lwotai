from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card61(JihadistCard):

    def __init__(self):
        super(Card61, self).__init__(61, "Detainee Release", 2, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if "GTMO" in app.lapsing or "Renditions" in app.markers:
            return False
        return app.get_yes_no_from_user("Did the US Disrupt during this or the last Action Phase? (y/n): ")

    def play_as_jihadist(self, app):
        if app.cells > 0:
            target_name = None
            while not target_name:
                country_name = app.get_country_from_user(
                    "Choose a country where Disrupt occured this or last Action Phase: ", "XXX", None)
                if country_name == "":
                    print ""
                    return
                else:
                    target_name = country_name
                    break
            app.place_cell(target_name)
        app.output_to_history("Draw a card for the Jihadist and put it on the top of their hand.", True)
