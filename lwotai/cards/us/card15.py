from lwotai.cards.us.us_card import USCard


class Card15(USCard):

    def __init__(self):
        super(Card15, self).__init__(15, "Ethiopia Strikes", 2, True, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Somalia").is_islamist_rule() or app.get_country("Sudan").is_islamist_rule()

    def play_event(self, side, app):
        if app.get_country("Somalia").is_islamist_rule() or app.get_country("Sudan").is_islamist_rule():
            if not app.get_country("Somalia").is_islamist_rule():
                target_country = "Sudan"
            elif not app.get_country("Sudan").is_islamist_rule():
                target_country = "Somalia"
            else:
                print "Both Somalia and Sudan are under Islamist Rule."
                if app.get_yes_no_from_user("Do you want Somalia to be set to Poor Neutral? (y/n): "):
                    target_country = "Somalia"
                else:
                    target_country = "Sudan"
            self._overthrow_islamist_rule(app, target_country)
            print ""
        else:
            return False

    @staticmethod
    def _overthrow_islamist_rule(app, target_country_name):
        target_country = app.get_country(target_country_name)
        target_country.make_poor()
        target_country.make_neutral()
        app.output_to_history("%s now Poor Neutral." % target_country.name, False)
        app.output_to_history(target_country.summary(), True)
