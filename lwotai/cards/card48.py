from lwotai.cards.abstract_card import AbstractCard


class Card48(AbstractCard):

    def __init__(self):
        super(Card48, self).__init__(48, "Jihadist", "Adam Gadahn", 1, False, False, False, puts_cell=True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        if app.num_cells_available() <= 0:
            return False
        return app.get_yes_no_from_user("Is this the 1st card of the Jihadist Action Phase? (y/n): ")

    def play_event(self, side, app):
        card_num = app.get_card_num_from_user(
            "Enter the number of the next Jihadist card or none if there are none left: ")
        if card_num == "none":
            app.output_to_history("No cards left to recruit to US.")
            return
        ops = app.deck.get(card_num).ops
        rolls = app.randomizer.roll_d6(ops)
        app.execute_recruit("United States", ops, rolls, 2)
