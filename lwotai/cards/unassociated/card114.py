import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard


class Card114(UnassociatedCard):

    def __init__(self):
        super(Card114, self).__init__(114, "GTMO", 3, False, False, True, False)

    def do_play_event(self, side, app):
        app.lapsing.append("GTMO")
        app.output_to_history("GTMO in play. No recruit operations or Detainee Release the rest of this turn.", False)
        prestige_rolls = []
        for _ in range(3):
            prestige_rolls.append(random.randint(1, 6))
        prestige_multiplier = -1 if prestige_rolls[0] <= 4 else 1
        app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
