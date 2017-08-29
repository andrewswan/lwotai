from lwotai.cards.us.us_card import USCard


class Card29(USCard):

    def __init__(self):
        super(Card29, self).__init__(29, "Tony Blair", 2, True, False, False)

    def play_as_us(self, app):
        app.set_posture("United Kingdom", app.us_posture())
        app.output_to_history("United Kingdom posture now %s" % app.get_posture("United Kingdom"), False)
        print "You may roll War of Ideas in up to 3 Schengen countries."
        for i in range(3):
            target_name = ""
            finished_picking = False
            while not target_name:
                country_name = app.get_country_from_user(
                    "Choose Schengen country to make a WoI roll (done to stop rolling) (? for list)?: ", "done",
                    app.list_schengen_countries)
                if country_name == "":
                    print ""
                    return
                elif country_name == "done":
                    finished_picking = True
                    break
                else:
                    if not app.get_country(country_name).schengen:
                        print "%s is not a Schengen country." % country_name
                        print ""
                        return
                    else:
                        target_name = country_name
                        posture_roll = app.get_roll("posture")
                        app.execute_non_muslim_woi(target_name, posture_roll)
            if finished_picking:
                break
        app.output_to_history("", False)
