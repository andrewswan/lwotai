from lwotai.cards.us.us_card import USCard


class Card17(USCard):

    def __init__(self):
        super(Card17, self).__init__(17, "FSB", 2, False, False, False)

    def play_event(self, side, app):
        app.output_to_history("Examine Jihadist hand for Loose Nukes, HEU, or Kazakh Strain.", False)
        has_wmd_card = app.get_yes_no_from_user(
            "Does the Jihadist hand have Loose Nukes, HEU, or Kazakh Strain? (y/n): ")
        if has_wmd_card:
            app.output_to_history("Discard Loose Nukes, HEU, or Kazakh Strain from the Jihadist hand.", False)
        else:
            russia_cells = app.get_country("Russia").total_cells(True)
            central_asia_cells = app.get_country("Central Asia").total_cells(True)
            if russia_cells > 0 or central_asia_cells > 0:
                if russia_cells == 0:
                    app.remove_cell("Central Asia", side)    # 20150131PS added side
                    app.output_to_history(app.get_country("Central Asia").summary(), True)
                elif central_asia_cells == 0:
                    app.remove_cell("Russia", side)    # 20150131PS added side
                    app.output_to_history(app.get_country("Russia").summary(), True)
                else:
                    is_russia = app.get_yes_no_from_user("There are cells in both Russia and Central Asia."
                                                         " Do you want to remove a cell in Russia? (y/n): ")
                    if is_russia:
                        app.remove_cell("Russia", side)    # 20150131PS added side
                        app.output_to_history(app.get_country("Russia").summary(), True)
                    else:
                        app.remove_cell("Central Asia", side)    # 20150131PS added side
                        app.output_to_history(app.get_country("Central Asia").summary(), False)
            else:
                app.output_to_history("There are no cells in Russia or Central Asia.", False)
        app.output_to_history("Shuffle Jihadist hand.", True)
