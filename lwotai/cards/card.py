class Card(object):
    """The superclass of all card classes"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing, puts_cell=False):
        self.__puts_cell = puts_cell
        self.lapsing = lapsing
        self.mark = mark
        self.name = name
        self.number = number
        self.ops = ops
        self.remove = remove
        self.type = card_type

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        if self.type == "US" and side == "Jihadist":
            return False
        elif self.type == "Jihadist" and side == "US":
            return False
        elif side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
            return False
        return self._really_playable(side, app, ignore_itjihad)

    @staticmethod
    def _really_playable(_side, _app, _ignore_itjihad):
        """Indicates whether this card is playable, assuming the side is valid; subclasses to override"""
        return True

    def puts_cell(self):
        """Whether this card's event places a cell; not for overriding"""
        return self.__puts_cell

    def play_event(self, side, app):
        """Executes this card's event as the given side (US or Jihadist); not for overriding"""
        app.output_to_history("Card played for Event.")
        self.do_play_event(side, app)
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)

    def do_play_event(self, side, app):
        """Executes the event logic; for subclasses to override"""
        pass

