from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card53(JihadistCard):

    def __init__(self):
        super(Card53, self).__init__(53, "Madrassas", 1, False, False, False, True)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return app.get_yes_no_from_user("Is this the 1st card of the Jihadist Action Phase? (y/n): ")

    def play_as_jihadist(self, app):
        app.handle_recruit(self.ops, True)
        next_card_num = app.get_card_num_from_user(
            "Enter the number of the next Jihadist card or 'none' if there are none left: ")
        if isinstance(next_card_num, str) and "none".startswith(next_card_num):
            app.output_to_history("No cards left to recruit.", True)
            return
        ops = app.get_card(next_card_num).ops
        app.handle_recruit(ops, True)
