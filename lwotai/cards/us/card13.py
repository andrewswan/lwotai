from lwotai.cards.us.us_card import USCard


class Card13(USCard):

    def __init__(self):
        super(Card13, self).__init__(13, "Anbar Awakening", 2, False, True, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_country("Iraq").troops() > 0 or app.get_country("Syria").troops() > 0

    def play_as_us(self, app):
        if (app.get_country("Iraq").troops() > 0) or (app.get_country("Syria").troops() > 0):
            app.markers.append("Anbar Awakening")
            app.output_to_history("Anbar Awakening in play.", False)
            if app.get_country("Iraq").troops() == 0:
                app.get_country("Syria").add_aid(1)  # 20150131PS changed to add rather than set to 1
                app.output_to_history("Aid in Syria.", False)
            elif app.get_country("Syria").troops() == 0:
                app.get_country("Iraq").add_aid(1)  # 20150131PS changed to add rather than set to 1
                app.output_to_history("Aid in Iraq.", False)
            else:
                print "There are troops in both Iraq and Syria."
                if app.get_yes_no_from_user("Do you want to add the Aid to Iraq? (y/n): "):
                    app.get_country("Iraq").add_aid(1)
                    app.output_to_history("Aid in Iraq.", False)
                else:
                    app.get_country("Syria").add_aid(1)
                    app.output_to_history("Aid in Syria.", False)
            app.change_prestige(1, False)
            print ""
        else:
            return False
