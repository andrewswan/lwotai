from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card117and118(UnassociatedCard):

    def __init__(self, number):
        super(Card117and118, self).__init__(number, "Oil Price Spike", 3, False, False, True, False)

    def do_play_event(self, side, app):
        app.lapsing.append("Oil Price Spike")
        app.output_to_history(
            "Oil Price Spike in play. Add +1 to the resources of each Oil Exporter country for the turn.",
            False)
        if side == "US":
            app.output_to_history(
                "Select, reveal, and draw a card other than Oil Price Spike from the discard pile or a box.")
        else:
            if app.get_yes_no_from_user("Are there any Jihadist event cards in the discard pile? "):
                app.output_to_history("Draw from the Discard Pile randomly among the highest-value Jihadist-associated"
                                      " event cards. Put the card on top of the Jihadist hand.")
