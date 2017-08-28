from lwotai.cards.us.us_card import USCard


class Card32(USCard):

    def __init__(self):
        super(Card32, self).__init__(32, "Back Channel", 3, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if app.us().is_hard() or not app.num_adversary():
            return False
        app.list_adversary_countries()
        return app.get_yes_no_from_user(
            "Do you have a card with a value that exactly matches an Adversary's Resources? (y/n): ")

    def play_event(self, side, app):
        if app.us().is_hard():
            return False
        num_adversaries = app.num_adversary()
        if num_adversaries <= 0:
            return False
        if app.get_yes_no_from_user("Do you want to discard a card with a value that exactly matches"
                                    " an Adversary's Resources? (y/n): "):
            while True:
                country_name = app.get_country_from_user(
                    "Choose an Adversary country (? for list): ", "XXX", app.list_adversary_countries)
                if country_name == "":
                    print ""
                    return False
                else:
                    adversary = app.get_country(country_name)
                    if not adversary.is_adversary():
                        print "%s is not an Adversary country." % country_name
                        print ""
                    else:
                        adversary.make_neutral()
                        app.output_to_history("%s now Neutral" % country_name, False)
                        adversary.add_aid(1)
                        app.output_to_history("Aid added to %s." % country_name, False)
                        app.output_to_history(adversary.summary())
                        break
