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
            if self.number >= 96:  # Danish Cartoons
                raise Exception("Has subclass")
            return False

    def puts_cell(self):
        """Indicates whether this card places a cell"""
        if self.type == "US":
            return False
        elif self.number == 74:  # Schengen Visas
            return False
        else:
            raise Exception("Has subclass")

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
            if self.number >= 96:  # Danish Cartoons
                raise Exception("Has subclass")
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)
