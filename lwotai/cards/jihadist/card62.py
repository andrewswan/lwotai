from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card62(JihadistCard):

    def __init__(self):
        super(Card62, self).__init__(62, "Ex-KGB", 2, False, False, False, False)

    def play_event(self, _side, app):
        if "CTR" in app.get_country("Russia").markers:
            app.get_country("Russia").markers.remove("CTR")
            app.output_to_history("CTR removed from Russia.", True)
        else:
            # See whether changing Central Asia posture would shift World Posture marker (rule 9.6)
            caucasus_posture_before = app.get_posture("Caucasus")
            net_hard_countries_before = app.map.get_net_hard_countries()
            if app.us().is_hard():
                app.get_country("Caucasus").make_soft()
            else:
                app.get_country("Caucasus").make_hard()
            net_hard_countries_after = app.map.get_net_hard_countries()
            app.set_posture("Caucasus", caucasus_posture_before)
            target_caucasus = (net_hard_countries_before != net_hard_countries_after)
            if target_caucasus:
                # Set to opposite posture of US
                if app.us().is_hard():
                    app.get_country("Caucasus").make_soft()
                else:
                    app.get_country("Caucasus").make_hard()
                app.output_to_history("Caucasus posture now %s" % app.get_posture("Caucasus"), False)
                app.output_to_history(app.get_country("Caucasus").summary())
            else:
                # Test and shift Central Asia 1 box toward Adversary
                app.test_country("Central Asia")
                central_asia = app.get_country("Central Asia")
                if central_asia.is_ally():
                    central_asia.make_neutral()
                    app.output_to_history("Central Asia worsened to %s." % central_asia.alignment())
                elif central_asia.is_neutral():
                    central_asia.make_adversary()
                    app.output_to_history("Central Asia worsened to %s." % central_asia.alignment())
                app.output_to_history(central_asia.summary())
