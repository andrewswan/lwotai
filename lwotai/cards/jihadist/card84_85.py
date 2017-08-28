import random

from lwotai.cards.jihadist.jihadist_card import JihadistCard


class Card84and85(JihadistCard):

    def __init__(self, number):
        super(Card84and85, self).__init__(number, "Leak", 3, False, False, False, False)

    def _really_playable(self, _side, app, _ignore_itjihad):
        return ("Enhanced Measures" in app.markers) or ("Renditions" in app.markers) or ("Wiretapping" in app.markers)

    def play_event(self, _side, app):
        possibles = []
        if "Enhanced Measures" in app.markers:
            possibles.append("Enhanced Measures")
        if "Renditions" in app.markers:
            possibles.append("Renditions")
        if "Wiretapping" in app.markers:
            possibles.append("Wiretapping")
        target_name = random.choice(possibles)
        app.markers.remove(target_name)
        app.markers.append("Leak-"+target_name)
        app.output_to_history("%s removed and can no longer be played." % target_name, False)
        us_prestige_rolls = []
        for _ in range(3):
            us_prestige_rolls.append(random.randint(1, 6))
        posture_roll = random.randint(1, 6)
        prestige_multiplier = 1
        if us_prestige_rolls[0] <= 4:
            prestige_multiplier = -1
        app.change_prestige(min(us_prestige_rolls[1], us_prestige_rolls[2]) * prestige_multiplier, False)
        if posture_roll <= 4:
            app.us().make_soft()
        else:
            app.us().make_hard()
        app.output_to_history("US Posture now %s" % app.us_posture(), True)
        allies = app.minor_jihad_in_good_fair_choice(1, True)
        if allies:
            target_name = allies[0][0]
            app.get_country(target_name).make_neutral()
            app.output_to_history("%s Alignment shifted to Neutral." % target_name, True)
        else:
            app.output_to_history("No Allies to shift.", True)
