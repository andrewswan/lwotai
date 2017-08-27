from lwotai.cards.abstract_card import AbstractCard


class Card14(AbstractCard):

    def __init__(self):
        super(Card14, self).__init__(14, "US", "Covert Action", 2, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.contains_country(lambda c: c.is_adversary())

    def play_event(self, side, app):
        adversary_names = [country.name for country in app.map.values() if country.is_adversary()]
        target_country = None
        if not adversary_names:
            return False
        elif len(adversary_names) == 1:
            target_country = adversary_names[0]
        else:
            while not target_country:
                country_name = app.get_country_from_user(
                    "Choose an Adversary country to attempt Covert Action (? for list): ", "XXX",
                    app.list_adversary_countries)
                if country_name == "":
                    print ""
                    return
                elif app.get_country(country_name).is_adversary():
                    target_country = country_name
                else:
                    print "%s is not an Adversary." % country_name
                    print ""
        action_roll = app.get_roll("covert action")
        if action_roll >= 4:
            app.get_country(target_country).make_neutral()
            app.output_to_history("Covert Action successful, %s now Neutral." % target_country, False)
            app.output_to_history(app.get_country(target_country).summary(), True)
        else:
            app.output_to_history("Covert Action fails.", True)
