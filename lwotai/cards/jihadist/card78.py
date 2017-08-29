import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card78(JihadistCard):

    def __init__(self):
        super(Card78, self).__init__(78, "Axis of Evil", 3, False, False, False, False)

    def play_as_jihadist(self, app):
        app.output_to_history("US discards any Iran, Hizballah, or Jaysh al-Mahdi cards from hand.", False)
        if app.us().is_soft():
            app.us().make_hard()
            app.output_to_history("US Posture now Hard.", False)
        prestige_rolls = []
        for i in range(3):
            prestige_rolls.append(random.randint(1, 6))
        prestige_multiplier = 1
        if prestige_rolls[0] <= 4:
            prestige_multiplier = -1
        app.change_prestige(min(prestige_rolls[1], prestige_rolls[2]) * prestige_multiplier)
