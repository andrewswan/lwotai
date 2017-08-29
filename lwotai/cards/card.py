import random

from lwotai.governance import POOR, ISLAMIST_RULE
from lwotai.postures.posture import SOFT


class Card(object):
    """A card in the game"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing):
        self.number = number
        self.name = name
        self.type = card_type
        self.ops = ops
        self.remove = remove
        self.mark = mark
        self.lapsing = lapsing

    def playable(self, side, app, ignore_itjihad):
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number == 18:  # Intel Community
                return True
            elif self.number <= 47:  # The door of Itjihad was closed
                raise Exception("Has subclass")
            else:
                raise Exception("Invalid US card %d" % self.number)
        elif self.type == "Jihadist" and side == "Jihadist":
            if "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            elif self.number == 74:  # Schengen Visas
                return True
            else:
                raise Exception("Has subclass")
        else:  # Unassociated Events
            if side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
                return False
            if self.number == 96:  # Danish Cartoons
                raise Exception("Has subclass")
            elif self.number == 97:  # Fatwa
                raise Exception("Has subclass")
            elif self.number == 98:  # Gaza Withdrawl
                raise Exception("Has subclass")
            elif self.number == 99:  # HAMAS Elected
                raise Exception("Has subclass")
            elif self.number == 100:  # His Ut-Tahrir
                raise Exception("Has subclass")
            elif self.number == 101:  # Kosovo
                raise Exception("Has subclass")
            elif self.number == 102:  # Former Soviet Union    #20150312PS
                raise Exception("Has subclass")
            elif self.number == 103:  # Hizballah
                raise Exception("Has subclass")
            elif self.number == 104 or self.number == 105:  # Iran
                raise Exception("Has subclass")
            elif self.number == 106:  # Jaysh al-Mahdi
                raise Exception("Has subclass")
            elif self.number == 107:  # Kurdistan
                raise Exception("Has subclass")
            elif self.number == 108:  # Musharraf
                raise Exception("Has subclass")
            elif self.number == 109:  # Tora Bora
                raise Exception("Has subclass")
            elif self.number == 110:  # Zarqawi
                raise Exception("Has subclass")
            elif self.number == 111:  # Zawahiri
                raise Exception("Has subclass")
            elif self.number == 112:  # Bin Ladin
                raise Exception("Has subclass")
            elif self.number == 113:  # Darfur
                raise Exception("Has subclass")
            elif self.number == 114:  # GTMO
                raise Exception("Has subclass")
            elif self.number == 115:  # Hambali
                raise Exception("Has subclass")
            elif self.number == 116:  # KSM
                raise Exception("Has subclass")
            elif self.number in [117, 118]:  # Oil Price Spike
                raise Exception("Has subclass")
            elif self.number == 119:  # Saleh
                raise Exception("Has subclass")
            elif self.number == 120:  # US Election
                return True
            return False

    def puts_cell(self):
        """Indicates whether this card places a cell"""
        if self.type == "US":
            return False
        elif self.number <= 73:  # Pirates
            raise Exception("Has subclass")
        elif self.number == 74:  # Schengen Visas
            return False
        elif self.number <= 95:  # Wahhabism
            raise Exception("Has subclass")
        elif self.number == 96:  # Danish Cartoons
            raise Exception("Has subclass")
        elif self.number == 97:  # Fatwa
            raise Exception("Has subclass")
        elif self.number == 98:  # Gaza Withdrawl
            raise Exception("Has subclass")
        elif self.number == 99:  # HAMAS Elected
            raise Exception("Has subclass")
        elif self.number == 100:  # His Ut-Tahrir
            raise Exception("Has subclass")
        elif self.number == 101:  # Kosovo
            raise Exception("Has subclass")
        elif self.number == 102:  # Former Soviet Union
            raise Exception("Has subclass")
        elif self.number == 103:  # Hizballah
            raise Exception("Has subclass")
        elif self.number == 104 or self.number == 105:  # Iran
            raise Exception("Has subclass")
        elif self.number == 106:  # Jaysh al-Mahdi
            raise Exception("Has subclass")
        elif self.number == 107:  # Kurdistan
            raise Exception("Has subclass")
        elif self.number == 108:  # Musharraf
            raise Exception("Has subclass")
        elif self.number == 109:  # Tora Bora
            raise Exception("Has subclass")
        elif self.number == 110:  # Zarqawi
            raise Exception("Has subclass")
        elif self.number == 111:  # Zawahiri
            raise Exception("Has subclass")
        elif self.number == 112:  # Bin Ladin
            raise Exception("Has subclass")
        elif self.number == 113:  # Darfur
            raise Exception("Has subclass")
        elif self.number == 114:  # GTMO
            raise Exception("Has subclass")
        elif self.number == 115:  # Hambali
            raise Exception("Has subclass")
        elif self.number == 116:  # KSM
            raise Exception("Has subclass")
        elif self.number == 117 or self.number == 118:  # Oil Price Spike
            raise Exception("Has subclass")
        elif self.number == 119:  # Saleh
            raise Exception("Has subclass")
        elif self.number == 120:  # US Election
            return False
        return False

    def play_event(self, side, app):
        app.output_to_history("Card played for Event.")
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif self.type == "US" and side == "US":
            if self.number <= 17:  # FSB
                raise Exception("Has subclass")
            elif self.number == 18:  # Intel Community
                app.output_to_history("Examine Jihadist hand. Do not change order of cards.", False)
                app.output_to_history("Conduct a 1-value operation (Use commands: alert, deploy, disrupt, reassessment,"
                                      " regime_change, withdraw, or war_of_ideas).", False)
                app.output_to_history(
                    "You may now interrupt this action phase to play another card (Use the u command).", True)
            elif self.number <= 47:  # The door of Itjihad was closed
                raise Exception("Has subclass")
            else:
                raise Exception("Invalid US card %d", self.number)
        elif self.type == "Jihadist" and side == "Jihadist":
            if self.number == 74:  # Schengen Visas
                if app.cells == 15:
                    app.output_to_history("No cells to travel.", False)
                    return
                app.handle_travel(2, False, True)
            else:
                raise Exception("Has subclass")
        else:
            if self.number == 96:  # Danish Cartoons
                raise Exception("Has subclass")
            elif self.number == 97:  # Fatwa
                raise Exception("Has subclass")
            elif self.number == 98:  # Gaza Withdrawl
                raise Exception("Has subclass")
            elif self.number == 99:  # HAMAS Elected
                raise Exception("Has subclass")
            elif self.number == 100:  # His Ut-Tahrir
                raise Exception("Has subclass")
            elif self.number == 101:  # Kosovo
                raise Exception("Has subclass")
            elif self.number == 102:  # Former Soviet Union
                raise Exception("Has subclass")
            elif self.number == 103:  # Hizballah
                raise Exception("Has subclass")
            elif self.number == 104 or self.number == 105:  # Iran
                raise Exception("Has subclass")
            elif self.number == 106:  # Jaysh al-Mahdi
                raise Exception("Has subclass")
            elif self.number == 107:  # Kurdistan
                raise Exception("Has subclass")
            elif self.number == 108:  # Musharraf
                raise Exception("Has subclass")
            elif self.number == 109:  # Tora Bora
                raise Exception("Has subclass")
            elif self.number == 110:  # Zarqawi
                raise Exception("Has subclass")
            elif self.number == 111:  # Zawahiri
                raise Exception("Has subclass")
            elif self.number == 112:  # Bin Ladin
                raise Exception("Has subclass")
            elif self.number == 113:  # Darfur
                raise Exception("Has subclass")
            elif self.number == 114:  # GTMO
                raise Exception("Has subclass")
            elif self.number == 115:  # Hambali
                raise Exception("Has subclass")
            elif self.number == 116:  # KSM
                raise Exception("Has subclass")
            elif self.number == 117 or self.number == 118:  # Oil Price Spike
                raise Exception("Has subclass")
            elif self.number == 119:  # Saleh
                raise Exception("Has subclass")
            elif self.number == 120:  # US Election
                app.execute_card_us_election(random.randint(1, 6))
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)
